# pycsw

Helm chart for pycsw service

Debug with:

```bash
helm install --dry-run --debug pycsw .
```

Deploy with:

```bash
helm install pycsw .
```

The server should then be made available at the host/port specified by
`minikube service pycsw --url`.
