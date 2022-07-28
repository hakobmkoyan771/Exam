resource "helm_release" "argocd" {
  name       = "argo-cd"
  chart      = "argo-cd"
  repository = "https://charts.bitnami.com/bitnami"
  namespace  = "default"
}
