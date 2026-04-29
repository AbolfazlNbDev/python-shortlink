<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=200&section=header&text=PYTHON%20SHORTLINK&fontSize=40&fontColor=ffffff&animation=fadeIn&fontAlignY=35"/>
</p>

<h3 align="center">🚀 سیستم کوتاه کننده لینک سریع و امن با Python و Flask</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask">
  <img src="https://img.shields.io/badge/Database-SQLite-green?style=for-the-badge&logo=sqlite">
  <img src="https://img.shields.io/github/stars/AbolfazlNbDeV/python-shortlink?style=for-the-badge">
  <img src="https://img.shields.io/github/forks/AbolfazlNbDeV/python-shortlink?style=for-the-badge">
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=AbolfazlNbDeV&label=Profile%20Views&color=blueviolet&style=for-the-badge">
</p>

---

# 🧠 معرفی پروژه

**Python Shortlink** یک سیستم سریع برای کوتاه کردن لینک‌ها است که با استفاده از Flask ساخته شده و می‌تواند به راحتی روی سیستم شخصی یا سرور اجرا شود.

هدف پروژه ایجاد یک سرویس ساده، سریع و امن برای تبدیل لینک‌های طولانی به لینک‌های کوتاه است.

---

# ✨ ویژگی‌ها

✅ تولید لینک کوتاه  
✅ سرعت بالا  
✅ ذخیره لینک‌ها در دیتابیس  
✅ ریدایرکت سریع  
✅ قابلیت توسعه  

---

# 🏗 نحوه کار سیستم

Client ➜ Flask Server ➜ Database ➜ Redirect

1. کاربر لینک را ارسال می‌کند  
2. سیستم یک شناسه کوتاه تولید می‌کند  
3. لینک در دیتابیس ذخیره می‌شود  
4. هنگام باز شدن لینک کوتاه، کاربر به لینک اصلی هدایت می‌شود  

---

# 🚀 اجرای پروژه

برای اجرای پروژه مراحل زیر را انجام دهید:

git clone https://github.com/AbolfazlNbDeV/python-shortlink.git

cd python-shortlink

python -m venv .venv

# فعال سازی محیط مجازی

# لینوکس / مک
source .venv/bin/activate

# ویندوز
.venv\Scripts\activate

# نصب وابستگی ها
pip install --upgrade pip
pip install -r requirements.txt

# اجرای برنامه
python app.py

# باز کردن در مرورگر
http://localhost:5000

---

# ⚙️ تنظیمات

فایل زیر را ویرایش کنید:

Config.py

نمونه تنظیمات:

BASE_URL = "http://localhost:5000"  
SECRET_KEY = "CHANGE_THIS_SECRET_KEY"  
DATABASE = "shortlink.db"  

---

# 📊 آمار گیت‌هاب

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=AbolfazlNbDeV&show_icons=true&theme=tokyonight">
</p>

---

# ⭐ حمایت از پروژه

اگر این پروژه برای شما مفید بود لطفاً در گیت‌هاب ⭐ بدهید:

https://github.com/AbolfazlNbDeV/python-shortlink

---

# 👨‍💻 توسعه‌دهنده

AbolfazlNbDeV

https://github.com/AbolfazlNbDeV

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=120&section=footer"/>
</p>
