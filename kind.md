چند Kind رایج در Kubernetes (خیلی خلاصه):

Pod — کوچک‌ترین واحد اجرا؛ یک یا چند container که باهم روی یک Node اجرا می‌شوند.
Deployment — مدیریت Podهای stateless؛ replica می‌سازد، update و rollback انجام می‌دهد.
StatefulSet — اجرای Podهای stateful با identity و storage ثابت برای هر Pod.
DaemonSet — یک Pod روی هر Node (مثلاً برای log agent یا monitoring).
Job — اجرای یک کار batch که باید کامل شود و بعد تمام می‌شود.
CronJob — اجرای Jobها به‌صورت زمان‌بندی‌شده (مثل cron لینوکس).
Service — یک آدرس پایدار و load balancing برای دسترسی به Podها.
Ingress — مدیریت دسترسی HTTP/HTTPS از بیرون کلاستر به Serviceها.
ConfigMap — نگهداری تنظیمات و configهای اپلیکیشن.
Secret — نگهداری داده‌های حساس مثل password و token.
PersistentVolume (PV) — منبع واقعی storage در کلاستر.
PersistentVolumeClaim (PVC) — درخواست storage توسط Podها.
Namespace — جدا کردن منابع کلاستر به محیط‌های منطقی مختلف.
