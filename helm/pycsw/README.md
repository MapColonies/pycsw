# pycsw common chart

Common Helm chart for the MapColonies pycsw service. It is not deployed directly;
each team consumes it as a dependency from its own deployment repository and injects
its team-specific configuration.

## Consuming the chart

In your team deployment repo, create a thin wrapper chart (see `examples/team-wrapper`
in this repository for a complete working example):

```yaml
# Chart.yaml
dependencies:
  - name: pycsw
    version: 6.6.1
    repository: oci://acrarolibotnonprod.azurecr.io/helm
```

## Team configuration contract

The chart does **not** ship `pycsw.cfg` or `mappings.py` — these are team-specific.
Your wrapper chart must provide a ConfigMap containing both keys and pass its name
via `existingConfigmap` (the value may be a template):

```yaml
# wrapper values.yaml
pycsw:
  existingConfigmap: '{{ .Release.Name }}-pycsw-team-config'
```

```yaml
# wrapper templates/configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-pycsw-team-config
data:
  pycsw.cfg: {{ tpl (.Files.Get "config/pycsw.cfg") . | quote }}
  mappings.py: {{ .Files.Get "config/mappings.py" | quote }}
```

Rendering fails with a clear error when `existingConfigmap` is not set.

### Environment variables available to pycsw.cfg

pycsw expands `${VAR}` placeholders in `pycsw.cfg` at runtime, so the team config
file needs no Helm helpers from this chart. The chart provides:

| Variable | Content |
|---|---|
| `PYCSW_SERVER_URL` | public server URL derived from the nginx route values |
| `PYCSW_MAPPINGS_FILEPATH` | mount path of the team `mappings.py` |
| `PYCSW_DATABASE_CONNECTION` | full postgres connection string (user/password from the DB secret, host/port/name/SSL params from `db`/`global.db` values) |
| `DB_SCHEMA` | value of `env.db.schema` |

A minimal `[repository]` section in a team `pycsw.cfg`:

```ini
[repository]
database=${PYCSW_DATABASE_CONNECTION}
mappings=${PYCSW_MAPPINGS_FILEPATH}
table=${DB_SCHEMA}.records
```

### Values teams are expected to set

| Value | Meaning |
|---|---|
| `existingConfigmap` | name of the team ConfigMap (required) |
| `env.db.schema` | catalog schema, e.g. `RasterCatalogManager` |
| `mclabels.owner`, `mclabels.gisDomain` | team labels |
| `nginx.authorization.domain` | OPA authorization domain |
| `nginx.route.routesMapping` | exposed route paths |
| `replicaCount`, `resources` | scale |

### Multiple instances in one release

When consuming this chart more than once in the same release (aliased
dependencies, e.g. a filtered and an unfiltered catalog), each extra instance
must set:

| Value | Meaning |
|---|---|
| `nameOverride` | distinct pycsw resource names and selector labels |
| `existingConfigmap` | its own team ConfigMap |
| `nginx.nameOverride` | distinct nginx selector labels (nginx >=2.2.1 derives pod selectors from it — identical values make services select each other's pods) |
| `nginx.fullnameOverride` | distinct nginx resource names |
| `nginx.extraVolumes` | point at the instance's own nginx configmap: `{{ .Release.Name }}-<nameOverride>-nginx-configmap` |

## Nginx

Nginx uses the modular extension layout: this chart ships generic
`pycsw-server.conf` / `pycsw-location.conf` snippets mounted into the nginx
subchart's `extensions` directory. Team-specific nginx behavior is driven by
values (`nginx.authorization`, `nginx.route.routesMapping`); additional snippets
can be added through the nginx subchart's own values.

## Config changes and pod restarts

The deployment checksums only the chart-owned ConfigMap (env vars, uwsgi.ini).
Changes to the team ConfigMap (`pycsw.cfg`, `mappings.py`) do **not** restart pods
automatically — run a rollout restart after changing team config:

```bash
kubectl rollout restart deployment <release>-pycsw-deployment
```
