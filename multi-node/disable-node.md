kubectl cordon k8s-lab-worker

```sh
kubectl cordon k8s-lab-worker
node/k8s-lab-worker cordoned
mehransaghebifard@PC:~/Desktop/kind-practice/multi-node$ kubectl get nodes
NAME                    STATUS                     ROLES           AGE    VERSION
k8s-lab-control-plane   Ready                      control-plane   103m   v1.35.0
k8s-lab-worker          Ready,SchedulingDisabled   <none>          103m   v1.35.0
k8s-lab-worker2         Ready                      <none>          103m   v1.35.0

```
