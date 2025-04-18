# Python-App-with-ArgoCD

Endpoints will be available at:
- GET `python-app.test.com/health`
- GET `python-app.test.com/info`
- GET `python-app.test.com/time`

More endpoints for app specific:
- GET `python-app.test.com/api/v1/details`

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

## Settinng Up Actions Runner Controller (Self-hosted)

For official documentation visit [this](#https://github.com/actions/actions-runner-controller/blob/master/docs/quickstart.md).


### Step 1: Install cert-manager in your cluster.

```
helm repo add cert-manager https://charts.jetstack.io
helm install my-cert-manager cert-manager/cert-manager --version 1.17.1
```

OR 

```
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.17.1/cert-manager.yaml
```

### Step 2: Generate a Personal Access Token (PAT) for ARC to authenticate with GitHub.

- Login to your GitHub account and Navigate to **[Create new Token](#https://github.com/settings/tokens/new)**.
- Select repo.
- Click Generate Token and then copy the token locally ( we’ll need it later).

### Step 3: Deploy and configure ARC on your K8s cluster.

**Add repository**
```
helm repo add actions-runner-controller https://actions-runner-controller.github.io/actions-runner-controller
```

**Install Helm chart**

```
helm upgrade --install --namespace actions-runner-system --create-namespace\
  --set=authSecret.create=true\
  --set=authSecret.github_token="REPLACE_YOUR_TOKEN_HERE"\
  --wait actions-runner-controller actions-runner-controller/actions-runner-controller
```

**note:-** Replace REPLACE_YOUR_TOKEN_HERE with your PAT that was generated previously.

Verifly runner Pods are up and running.

```
kubectl get pod -n actions-runner-system
```

### Step 4: Create the GitHub self hosted runners and configure to run against your repository.

Create a `runnerdeployment.yaml` file and copy the following YAML contents into it:

```
apiVersion: actions.summerwind.dev/v1alpha1
kind: RunnerDeployment
metadata:
  name: example-runnerdeploy
spec:
  replicas: 1
  template:
    spec:
      repository: mumoshu/actions-runner-controller-ci
```

***note:-** Replace "mumoshu/actions-runner-controller-ci" with the name of the GitHub repository the runner will be associated with.

Apply this file to your K8s cluster.
```
kubectl apply -f runnerdeployment.yaml -n actions-runner-system
```

Important:

We can performing above steps using followinv manifest.

```
cat << EOF | kubectl apply -n actions-runner-system -f -
apiVersion: actions.summerwind.dev/v1alpha1
kind: RunnerDeployment
metadata:
  name: self-hosted-runner
spec:
  replicas: 1
  template:
    spec:
      repository: asadhanif3188/Python-App-with-ArgoCD
EOF
```

### Step 5: Verify that your setup is successful:

```
kubectl get runners
kubectl get pods
```


