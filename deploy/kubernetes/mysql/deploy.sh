kubectl --kubeconfig ../config.yaml --namespace demo-contry-api-python apply -f mysql-configmap.yaml
kubectl --kubeconfig ../config.yaml --namespace demo-contry-api-python apply -f mysql-secret.yaml
kubectl --kubeconfig ../config.yaml --namespace demo-contry-api-python apply -f mysql-pv.yaml
kubectl --kubeconfig ../config.yaml --namespace demo-contry-api-python apply -f mysql-pvc.yaml
kubectl --kubeconfig ../config.yaml --namespace demo-contry-api-python apply -f mysql-deployment.yaml
kubectl --kubeconfig ../config.yaml --namespace demo-contry-api-python apply -f mysql-service.yaml