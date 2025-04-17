# Python-App-with-ArgoCD

Endpoints will be available at:
- GET `http://localhost:5000/health`
- GET `http://localhost:5000/info`
- GET `http://localhost:5000/time`


## ArgoCD Deployment 
To deploy the ArgoCD with helm, we need to run following command to get the dependencies for our chart.

```
helm dependency build charts/argocd
```

Now install our ArgoCD helm chart to execute the ArgoCD App. 

```
helm install my-argocd charts\argocd --values charts\argocd\values-argo.yaml --namespace argocd --create-namespace
```

To apply the updated helm chart.
```
helm upgrade my-argocd charts\argocd --values charts\argocd\values-argo.yaml --namespace argocd 
```

To unintall helm chart 
```
helm uninstall my-argocd  --namespace argocd
```

To see the pods of ArgoCD.

```
kubectl get po -n argocd
```

