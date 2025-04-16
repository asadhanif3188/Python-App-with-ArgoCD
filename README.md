# Python-App-with-ArgoCD

Endpoints will be available at:
- GET `http://localhost:5000/health`
- GET `http://localhost:5000/info`
- GET `http://localhost:5000/time`


## ArgoCD Deployment 
To deploy the ArgoCD with helm, we need to run following command to get the dependencies.

```
helm dependency build charts/argocd
```

