kubectl --kubeconfig ../config.yaml --namespace demo-contry-api-python apply -f configmap.yaml
kubectl --kubeconfig ../config.yaml --namespace demo-contry-api-python apply -f secret.yaml
kubectl --kubeconfig ../config.yaml --namespace demo-contry-api-python apply -f deployment.yaml
kubectl --kubeconfig ../config.yaml --namespace demo-contry-api-python apply -f service.yaml
kubectl --kubeconfig ../config.yaml --namespace demo-contry-api-python apply -f ingress.yaml