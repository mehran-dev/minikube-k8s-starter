/etc/kubernetes/admin.conf
/opt/kube/configs/prod.conf

```bash
kubectl --kubeconfig /etc/kubernetes/admin.conf get pods
//permanent access
export KUBECONFIG=/etc/kubernetes/admin.conf

```

```bash

// more output logs
kubectl get pods -o wide
// also you can use
kubectl get pods -o yaml
kubectl get pods -o json
kubectl get pods -o custom-columns=...

```

```bash
kubectl get svc

```

```bash
kubectl get pods

```

```bash
kubectl scale deployment nginx-deployment --replicas=10

```

```bash
kubectl describe deployment nginx-deployment | grep Image
```

```bash
kubectl get rs
kubectl describe deployment nginx-deployment | grep Image
kubectl rollout history deployment/nginx-deployment


```

```bash

kubectl get deployment nginx-deployment -o yaml | grep revisionHistoryLimit
  revisionHistoryLimit: 10

```

```
kubectl apply -f secret.yaml
================================

kubectl get secrets
kubectl describe secret db-secret


```

kubectl get storageclass

kubectl logs -n local-path-storage local-path-provisioner-67b8995b4b-vf5zv

kubectl patch pvc nginx-pvc -p '{"metadata":{"finalizers":null}}'

kubectl delete pvc nginx-pvc --force --grace-period=0

kubectl patch pv nginx-pv -p '{"spec":{"claimRef": null}}'

kubectl config view

docker rm -f $(docker ps -aq --filter ancestor=kindest/node)
