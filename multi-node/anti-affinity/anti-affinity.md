✅ 1️⃣ Pod Anti-Affinity
هدف:

هیچ‌وقت دو Pod مشابه روی یک Node نیفتند.

✅ 2️⃣ Topology Spread Constraint
هدف:

توزیع متعادل تضمینی بین Nodeها

فرقش با Anti-Affinity اینه که اینجا می‌گیم اختلاف زیاد نشه، نه اینکه کاملاً جدا باشند.

✅ 3️⃣ PodDisruptionBudget (PDB)
این برای مواقعی است که:

Node drain می‌شود
Rolling update انجام می‌شود
Autoscaler Node حذف می‌کند
می‌خواهیم بگوییم:

حداقل X تا Pod همیشه باید زنده باشند.

فایل: pdb.yaml

```
kubectl get pdb

kubectl drain k8s-lab-worker --ignore-daemonsets --delete-emptydir-data


```
