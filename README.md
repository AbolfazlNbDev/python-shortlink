<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=200&section=header&text=PYTHON%20SHORTLINK&fontSize=40&fontColor=ffffff&animation=fadeIn&fontAlignY=35"/>
</p>

<h3 align="center">🚀 سیستم حرفه‌ای کوتاه‌کننده لینک با امنیت بالا و معماری ماژولار</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask">
  <img src="https://img.shields.io/badge/Database-SQLite-green?style=for-the-badge&logo=sqlite">
  <img src="https://img.shields.io/badge/License-MIT-red?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/AbolfazlNbDeV/python-shortlink?style=for-the-badge">
  <img src="https://img.shields.io/github/forks/AbolfazlNbDeV/python-shortlink?style=for-the-badge">
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=AbolfazlNbDeV&label=بازدید%20پروفایل&color=blueviolet&style=for-the-badge">
</p>

---

# 🧠 معرفی پروژه

**Python Shortlink** یک سیستم سریع، امن و قابل توسعه برای کوتاه‌سازی لینک‌هاست که با استفاده از Flask توسعه داده شده و ساختار آن برای استفاده در محیط Production آماده است.

این پروژه مناسب استفاده شخصی، آموزشی و حتی استقرار روی سرور واقعی می‌باشد.

---

# ✨ ویژگی‌های کلیدی

✅ تولید لینک کوتاه با الگوریتم امن  
✅ جلوگیری از Collision  
✅ ذخیره IP و User-Agent  
✅ سیستم مدیریت ادمین  
✅ تحلیل تعداد کلیک‌ها  
✅ ساختار ماژولار  
✅ آماده برای Docker  
✅ قابلیت توسعه به REST API  

---

# 🏗 معماری سیستم

Client ➜ Flask Backend ➜ Database ➜ Redirect  

1️⃣ کاربر لینک را ارسال می‌کند  
2️⃣ شناسه تصادفی امن تولید می‌شود  
3️⃣ در دیتابیس ذخیره می‌شود  
4️⃣ هنگام باز شدن لینک کوتاه، ریدایرکت انجام می‌شود  

---

# 🚀 نصب سریع

## کلون پروژه

git clone https://github.com/AbolfazlNbDeV/python-shortlink.git  
cd python-shortlink  

## ساخت محیط مجازی

python -m venv .venv  

فعال‌سازی لینوکس:

source .venv/bin/activate  

فعال‌سازی ویندوز:

.venv\Scripts\activate  

## نصب وابستگی‌ها

pip install -r requirements.txt  

## اجرای برنامه

python app.py  

مرورگر:

http://localhost:5000  

---

# 🐳 اجرای پروژه با Docker

ساخت Docker Image:

docker build -t python-shortlink .  

اجرای کانتینر:

docker run -p 5000:5000 python-shortlink  

---

# ⚙️ تنظیمات

فایل:

Config.py  

نمونه:

BASE_URL = "http://localhost:5000"  
SECRET_KEY = "CHANGE_THIS_SECRET_KEY"  
DATABASE = "shortlink.db"  
ADMIN_USERNAME = "admin"  
ADMIN_PASSWORD = "strongpassword"  

---

# 🔐 امنیت در محیط Production

✔ استفاده از Nginx  
✔ اجرای Gunicorn  
✔ فعال‌سازی HTTPS  
✔ استفاده از PostgreSQL  
✔ فعال‌سازی Rate Limiting  
✔ تنظیم Firewall  

---

# 🗺 نقشه راه (Roadmap)

- [x] تولید لینک کوتاه  
- [x] پنل مدیریت  
- [x] ثبت آمار کلیک  
- [ ] اضافه کردن API عمومی  
- [ ] سیستم کاربران و احراز هویت  
- [ ] داشبورد گرافیکی پیشرفته  
- [ ] استفاده از Redis Cache  
- [ ] استقرار خودکار CI/CD  

---

# 📁 ساختار پروژه

python-shortlink  
│  
├── app.py  
├── Config.py  
├── requirements.txt  
├── database.db  
│  
├── templates  
├── static  
└── utils  

---

# 📊 آمار گیت‌هاب

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=AbolfazlNbDeV&show_icons=true&theme=tokyonight">
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=AbolfazlNbDeV&theme=tokyonight">
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=AbolfazlNbDeV&theme=tokyo-night">
</p>

---

# 🤝 مشارکت در پروژه

git checkout -b feature/new-feature  
git commit -m "Add new feature"  
git push origin feature/new-feature  

سپس Pull Request ارسال کنید ✅  

---

# ⭐ حمایت از پروژه

اگر این پروژه برای شما مفید بوده لطفاً ⭐ بدهید:

https://github.com/AbolfazlNbDeV/python-shortlink  

---

# 👨‍💻 توسعه‌دهنده

AbolfazlNbDeV  

https://github.com/AbolfazlNbDeV  

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=120&section=footer"/>
</p>
