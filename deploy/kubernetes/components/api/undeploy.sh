kubectl --kubeconfig ../config.yaml --namespace demo-contry-api-python delete ingress demo-country-api-ingress
kubectl --kubeconfig ../config.yaml --namespace demo-contry-api-python delete service demo-country-api-service
kubectl --kubeconfig ../config.yaml --namespace demo-contry-api-python delete deployment demo-country-api-app
kubectl --kubeconfig ../config.yaml --namespace demo-contry-api-python delete secret demo-country-api-secret
kubectl --kubeconfig ../config.yaml --namespace demo-contry-api-python delete configmap demo-country-api-config



