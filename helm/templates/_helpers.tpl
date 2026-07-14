{{/*
Expand the name of the chart. nameOverride allows deploying multiple instances
of this chart in the same release (e.g. as aliased dependencies) without
resource name collisions.
*/}}
{{- define "pycsw.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "pycsw.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "pycsw.labels" -}}
helm.sh/chart: {{ include "pycsw.chart" . }}
{{ include "pycsw.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{ include "mclabels.labels" . }}
{{- end }}

{{/*
Returns the tag of the chart.
*/}}
{{- define "pycsw.tag" -}}
{{- default (printf "v%s" .Chart.AppVersion) .Values.image.tag }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "pycsw.selectorLabels" -}}
app.kubernetes.io/name: {{ include "pycsw.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{ include "mclabels.selectorLabels" . }}
{{- end }}

{{/*
Returns the environment from global if exists or from the chart's values, defaults to development
*/}}
{{- define "pycsw.environment" -}}
{{- if .Values.global.environment }}
    {{- .Values.global.environment -}}
{{- else -}}
    {{- .Values.environment | default "development" -}}
{{- end -}}
{{- end -}}

{{/*
Returns the pycsw server url based on the provided values, default localhost.
Host and path are taken from nginx.route.host/path when set, otherwise from
the first nginx.route.routesMapping entry.
*/}}
{{- define "pycsw.serverURL" -}}
    {{- $route := .Values.nginx.route -}}
    {{- $first := (first ($route.routesMapping | default list)) | default dict -}}
    {{- $host := $route.host | default $first.host -}}
    {{- $path := $route.path | default $first.path -}}
    {{- if not $host }}
        {{- printf "http://localhost:8000" -}}
    {{- else -}}
        {{- $protocol := ternary "https" "http" $route.tls.enabled -}}
        {{- printf "%s://%s" $protocol $host -}}
        {{- if $path -}}
            {{- printf "%s" $path -}}
        {{- end -}}
    {{- end -}}
{{- end -}}

{{/*
Returns the cloud provider name from global if exists or from the chart's values, defaults to minikube
*/}}
{{- define "pycsw.cloudProviderFlavor" -}}
{{- if .Values.global.cloudProvider.flavor }}
    {{- .Values.global.cloudProvider.flavor -}}
{{- else if .Values.cloudProvider -}}
    {{- .Values.cloudProvider.flavor | default "minikube" -}}
{{- else -}}
    {{ "minikube" }}
{{- end -}}
{{- end -}}

{{/*
Returns the cloud provider docker registry url from global if exists or from the chart's values
*/}}
{{- define "pycsw.cloudProviderDockerRegistryUrl" -}}
{{- if .Values.global.cloudProvider.dockerRegistryUrl }}
    {{- printf "%s/" .Values.global.cloudProvider.dockerRegistryUrl -}}
{{- else if .Values.cloudProvider.dockerRegistryUrl -}}
    {{- printf "%s/" .Values.cloudProvider.dockerRegistryUrl -}}
{{- else -}}
{{- end -}}
{{- end -}}

{{/*
Returns the cloud provider image pull secret name from global if exists or from the chart's values
*/}}
{{- define "pycsw.cloudProviderImagePullSecretName" -}}
{{- if .Values.global.cloudProvider.imagePullSecretName }}
    {{- .Values.global.cloudProvider.imagePullSecretName -}}
{{- else if .Values.cloudProvider.imagePullSecretName -}}
    {{- .Values.cloudProvider.imagePullSecretName -}}
{{- end -}}
{{- end -}}

{{/*
Returns the tracing url from global if exists or from the chart's values
*/}}
{{- define "pycsw.tracingUrl" -}}
{{- if .Values.global.tracing.url }}
    {{- .Values.global.tracing.url -}}
{{- else if .Values.cloudProvider -}}
    {{- .Values.env.tracing.url -}}
{{- end -}}
{{- end -}}

{{/*
Returns the tracing url from global if exists or from the chart's values
*/}}
{{- define "pycsw.metricsUrl" -}}
{{- if .Values.global.metrics.url }}
    {{- .Values.global.metrics.url -}}
{{- else -}}
    {{- .Values.env.metrics.url -}}
{{- end -}}
{{- end -}}

{{/*
Returns the name of the ConfigMap provided by the consuming chart, holding
the pycsw.cfg and mappings.py keys. The value may itself be a template.
Fails rendering when not provided.
*/}}
{{- define "pycsw.teamConfigmapName" -}}
{{- $name := include "common.tplvalues.render" (dict "value" .Values.existingConfigmap "context" .) -}}
{{- required "existingConfigmap is required: set it to the name of a ConfigMap containing the keys pycsw.cfg and mappings.py (provided by the consuming chart)" $name -}}
{{- end -}}

{{/*
Returns the postgres connection string as an environment variable value.
Uses Kubernetes dependent-variable syntax $(VAR) so it is resolved at container
start from DB_USER/DB_PASSWORD (secret) and DB_HOST/DB_PORT/DB_NAME (configmap).
Consumed by the team-provided pycsw.cfg via database=${PYCSW_DATABASE_CONNECTION}.
*/}}
{{- define "pycsw.connectionStringEnv" -}}
{{- $db := (include "common.db.merged" .) | fromYaml }}
{{- "postgresql://$(DB_USER)" -}}
{{- if .Values.env.db.requirePassword -}}
{{- ":$(DB_PASSWORD)" -}}
{{- end -}}
{{- "@$(DB_HOST):$(DB_PORT)/$(DB_NAME)" -}}
{{- if $db.sslEnabled -}}
{{- "?sslmode=require" -}}
{{- if $db.secrets.caFileKey -}}
{{- "&sslrootcert=/.postgresql/ca.pem" -}}
{{- end -}}
{{- if $db.secrets.certFileKey -}}
{{- "&sslcert=/.postgresql/cert.pem" -}}
{{- end -}}
{{- if $db.secrets.keyFileKey -}}
{{- "&sslkey=/.postgresql/key.pem" -}}
{{- end -}}
{{- end -}}
{{- end -}}

{{- define "pycsw.cors.allowedHeaders" -}}
{{- $authentication := (include "common.authentication.merged" .) | fromYaml }}
{{- $headerList := list -}}
{{- if ne .Values.env.cors.allowedHeaders "" -}}
{{- range $k, $v := (split "," .Values.env.cors.allowedHeaders) -}}
{{- $headerList = append $headerList $v -}}
{{- end -}}
{{- $headerList = uniq $headerList -}}
{{-  quote (join "," $headerList) -}}
{{- end -}}
{{- end -}}
