<h1 align="center">🚀 PYTHON SHORTLINK</h1>

<p align="center">
  <b>سیستم حرفه‌ای و سریع کوتاه‌کننده لینک با امنیت بالا</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask">
  <img src="https://img.shields.io/badge/Database-SQLite-green?style=for-the-badge&logo=sqlite">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/AbolfazlNbDeV/python-shortlink?style=for-the-badge">
</p>

---

## 🧠 معرفی پروژه

**Python Shortlink** یک سیستم سریع و امن برای کوتاه کردن لینک‌ها است که با استفاده از Flask توسعه داده شده و ساختاری ماژولار و قابل توسعه دارد.

این پروژه مناسب استفاده شخصی، آموزشی و حتی پیاده‌سازی روی سرور واقعی می‌باشد.

---

## ✨ ویژگی‌های کلیدی

✅ تولید لینک کوتاه با الگوریتم امن  
✅ جلوگیری از Collision  
✅ ذخیره IP و User-Agent  
✅ سیستم مدیریت ادمین  
✅ ثبت و تحلیل تعداد کلیک‌ها  
✅ ساختار ماژولار برای توسعه راحت  
✅ آماده برای Deploy روی سرور  

---

## 🏗 معماری سیستم

Client ➜ Flask Backend ➜ Database ➜ Redirect

1. کاربر لینک را ارسال می‌کند  
2. سیستم یک شناسه تصادفی امن تولید می‌کند  
3. در دیتابیس ذخیره می‌شود  
4. هنگام باز شدن لینک کوتاه، کاربر به لینک اصلی هدایت می‌شود  

---

## 🚀 نصب و اجرا

### 1️⃣ کلون کردن پروژه

git clone https://github.com/AbolfazlNbDeV/python-shortlink.git  
cd python-shortlink  

---

### 2️⃣ ساخت محیط مجازی

python -m venv .venv  

فعال‌سازی در لینوکس / مک:

source .venv/bin/activate  

در ویندوز:

.venv\Scripts\activate  

---

### 3️⃣ نصب وابستگی‌ها

pip install --upgrade pip  
pip install -r requirements.txt  

---

## ⚙️ تنظیمات پروژه

فایل زیر را باز کنید:

Config.py  

نمونه تنظیم:

BASE_URL = "http://localhost:5000"  
SECRET_KEY = "CHANGE_THIS_SECRET_KEY"  
DATABASE = "shortlink.db"  
ADMIN_USERNAME = "admin"  
ADMIN_PASSWORD = "strongpassword"  

---

## ▶️ اجرای برنامه

python app.py  

سپس مرورگر را باز کنید:

http://localhost:5000  

---

## 📁 ساختار پروژه

python-shortlink  
│  
├── app.py  
├── Config.py  
├── requirements.txt  
├── database.db  
│  
├── templates  
│   ├── index.html  
│   ├── admin.html  
│   └── login.html  
│  
├── static  
│   ├── css  
│   ├── js  
│   └── images  
│  
└── utils  
    ├── generator.py  
    ├── security.py  
    └── analytics.py  

---

## 🔐 پیشنهاد برای اجرای روی سرور

برای استفاده حرفه‌ای پیشنهاد می‌شود:

✔ استفاده از Nginx  
✔ اجرای پروژه با Gunicorn  
✔ فعال‌سازی HTTPS  
✔ استفاده از PostgreSQL  
✔ فعال کردن Rate Limiting  

---

## 🤝 مشارکت در پروژه

git checkout -b feature/new-feature  
git commit -m "Add new feature"  
git push origin feature/new-feature  

سپس Pull Request ارسال کنید ✅  

---

## ⭐ حمایت از پروژه

اگر این پروژه برای شما مفید بوده لطفاً در گیت‌هاب به آن ⭐ بدهید:

https://github.com/AbolfazlNbDeV/python-shortlink  

---

## 📊 آمار گیت‌هاب

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=AbolfazlNbDeV&show_icons=true&theme=radical">
</p>

---

## 👨‍💻 توسعه‌دهنده

AbolfazlNbDeV  

https://github.com/AbolfazlNbDeV  

---

## 📜 لایسنس

این پروژه تحت لایسنس MIT منتشر شده است.
