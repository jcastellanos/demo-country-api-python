kubectl --kubeconfig ../config.yaml --namespace demo-contry-api-python delete service mysql-service
kubectl --kubeconfig ../config.yaml --namespace demo-contry-api-python delete deployment mysql-app
kubectl --kubeconfig ../config.yaml --namespace demo-contry-api-python delete pvc mysql-pvc
# kubectl --kubeconfig ../config.yaml --namespace demo-contry-api-python delete pv mysql-pv
kubectl --kubeconfig ../config.yaml --namespace demo-contry-api-python delete secret mysql-secret
kubectl --kubeconfig ../config.yaml --namespace demo-contry-api-python delete configmap mysql-config
