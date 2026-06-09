✅ سؤال مهمت: Nginx لازم دارم یا Service؟
داخل کلاستر:
ارتباط چه چیزی load balance می‌کند؟
User → Frontend ✅ Service
Frontend → Backend ✅ Service
❗ برای این سناریو اصلاً nginx لازم نداری

Service خودش load balancing L4 انجام می‌دهد.

Nginx فقط وقتی لازم می‌شود که:

routing بر اساس path بخواهی
TLS termination بخواهی
از بیرون cluster ترافیک بیاید
