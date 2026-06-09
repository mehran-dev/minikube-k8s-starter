✅ Service چکار کرد؟
Service:

یک IP ثابت ساخت ✅
Podهایی که label app: nginx-demo دارند را پیدا کرد ✅
بین آن‌ها Load Balancing انجام می‌دهد ✅

---

بفهمیم:

DNS داخل کلاستر چطور کار می‌کند
چرا می‌توانیم فقط بنویسیم nginx-service
FQDN کامل سرویس چیست
Namespace چه نقشی دارد

kubectl get pods -n kube-system

3️⃣ FQDN کامل سرویس چیست؟
complete format:
<service-name>.<namespace>.svc.cluster.local
yours :
nginx-service.default.svc.cluster.local

test this:
nslookup nginx-service.default.svc.cluster.local

---

4️⃣ نکته مهم (مصاحبه‌ای 😎)
چرا وقتی فقط می‌نویسیم:

text
curl nginx-service
کار می‌کند؟

چون داخل هر Pod فایل زیر تنظیم شده:

text
/etc/resolv.conf
اگر داخل busybox بزنی:

bash
cat /etc/resolv.conf
می‌بینی search domain دارد:

text
search default.svc.cluster.local svc.cluster.local cluster.local
پس وقتی فقط می‌نویسی:

text
nginx-service
سیستم خودش کاملش می‌کند به:

text
nginx-service.default.svc.cluster.local

---

✅ نکته مهم مصاحبه‌ای
Service load balancing:

L4 (TCP/UDP) است
Stateless است
Session-aware نیست (مگر sessionAffinity فعال شود)
