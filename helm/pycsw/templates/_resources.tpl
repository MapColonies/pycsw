{{/*
Create service name as used by the service name label.
*/}}
{{- define "pycsw.service.fullname" -}}
{{- printf "%s-%s-%s" .Release.Name (include "pycsw.name" .) "service" }}
{{- end }}

{{/*
Create configmap name as used by the service name label.
*/}}
{{- define "pycsw.configmap.fullname" -}}
{{- printf "%s-%s-%s" .Release.Name (include "pycsw.name" .) "configmap" | indent 1 }}
{{- end }}

{{/*
Create pycsw nginx configmap name as used by the service name label.
*/}}
{{- define "pycsw.nginx-configmap.fullname" -}}
{{- printf "%s-%s-%s" .Release.Name (include "pycsw.name" .) "nginx-configmap" | indent 1 }}
{{- end }}

{{/*
Create deployment name as used by the service name label.
*/}}
{{- define "pycsw.deployment.fullname" -}}
{{- printf "%s-%s-%s" .Release.Name (include "pycsw.name" .) "deployment" | indent 1 }}
{{- end }}


{{/*
Create route name as used by the service name label.
*/}}
{{- define "pycsw.route.fullname" -}}
{{- printf "%s-%s-%s" .Release.Name (include "pycsw.name" .) "route" | indent 1 }}
{{- end }}

{{/*
Create ingress name as used by the service name label.
*/}}
{{- define "pycsw.ingress.fullname" -}}
{{- printf "%s-%s-%s" .Release.Name (include "pycsw.name" .) "ingress" | indent 1 }}
{{- end }}
