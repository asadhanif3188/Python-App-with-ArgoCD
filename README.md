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

### Get the admin password of the ArgoCD app

See the list of secrets

```
kubectl get secrets -n argocd
```

Output:
```
NAME                              TYPE                 DATA   AGE
argocd-initial-admin-secret       Opaque               1      101m
argocd-notifications-secret       Opaque               0      4m28s
argocd-redis                      Opaque               1      101m
argocd-secret                     Opaque               3      4m28s
sh.helm.release.v1.my-argocd.v1   helm.sh/release.v1   1      4m32s
```

We are interested in the secret `argocd-initial-admin-secret` because it contains admin password. 

*Step A:*
```
kubectl get secrets argocd-initial-admin-secret -n argocd -o yaml
```

*Step B:*
```
echo <encoded-password> | base64 -d
```



