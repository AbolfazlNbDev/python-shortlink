# 🚀 Python ShortLink | سیستم حرفه‌ای کوتاه‌ساز لینک

<div align="center">

![GitHub stars](https://img.shields.io/github/stars/AbolfazlNbDeV/python-shortlink?style=social)
![GitHub forks](https://img.shields.io/github/forks/AbolfazlNbDeV/python-shortlink?style=social)
![License](https://img.shields.io/github/license/AbolfazlNbDeV/python-shortlink)
![Python Version](https://img.shields.io/badge/python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-Lightweight-red)

</div>

<p align="center">
سیستم کوتاه‌کننده لینک پیشرفته، سریع و قابل توسعه با پایتون و Flask 🔥  
<br>
<a href="#-قابلیت‌ها"><strong>قابلیت‌ها</strong></a> ·
<a href="#-نصب-و-راه‌اندازی"><strong>نصب</strong></a> ·
<a href="#-دیپلوی"><strong>دیپلوی</strong></a>
</p>

---

## ✨ قابلیت‌ها

🔗 ساخت لینک کوتاه با کد یونیک
📊 شمارش تعداد کلیک هر لینک
👤 ثبت‌نام و ورود کاربران
📧 تایید ایمیل با توکن
🔐 بازیابی رمز عبور
🛡️ سیستم کپچا ضد ربات
🧑‍💻 پنل مدیریت ادمین
📩 سیستم تیکت (پشتیبانی داخلی)
🗑️ حذف خودکار لینک‌ها
⚡ عملکرد سریع با SQLite
🎯 ساختار ساده و قابل توسعه

---

## 🧠 توضیح پروژه

این پروژه یک **URL Shortener کامل** است که امکانات زیر را در اختیار شما قرار می‌دهد:

* تبدیل لینک‌های طولانی به لینک کوتاه
* مدیریت لینک‌ها توسط کاربر
* سیستم احراز هویت کامل
* ریدایرکت سریع کاربران
* پنل ادمین برای کنترل کاربران و تیکت‌ها
* سیستم پشتیبانی داخلی

---

## 📦 پیش‌نیازها

* Python 3.8+
* pip

---

## 📚 کتابخانه‌های مورد نیاز

```txt
flask
requests
beautifulsoup4
pillow
```

---

## ⚙️ نصب و راه‌اندازی

### 1️⃣ کلون پروژه

```bash
git clone https://github.com/AbolfazlNbDeV/python-shortlink.git
cd python-shortlink
```

---

### 2️⃣ ساخت محیط مجازی

```bash
python -m venv venv
```

🔹 ویندوز:

```bash
venv\Scripts\activate
```

🔹 لینوکس / مک:

```bash
source venv/bin/activate
```

---

### 3️⃣ نصب وابستگی‌ها

```bash
pip install -r requirements.txt
```

---

### 4️⃣ تنظیم config

```python
admin = "your_admin_password"
emaill = "your_email"
passw = "your_email_app_password"
admin_email = "admin@domain.com"
domain = "yourdomain.com"
secret_key = "super_secret_key"
```

---

### 5️⃣ اجرای پروژه

```bash
python app.py
```

📍 آدرس اجرا:

```
http://127.0.0.1:8000
```

---

## 🚀 دیپلوی

### 🔹 اجرای ساده (سرور)

```bash
sudo apt update
sudo apt install python3-pip
pip install -r requirements.txt
python3 app.py
```

---

### 🔹 اجرای حرفه‌ای (Production)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

---

## 📂 ساختار پروژه

```bash
python-shortlink/
│
├── app.py
├── captcha.py
├── config.py
├── requirements.txt
├── database.db
├── templates/
└── static/
```

---

## 🔐 امنیت

❗ قبل از Public کردن پروژه:

```txt
config.py
__pycache__/
*.db
```

* فایل `config.py` را در `.gitignore` قرار بده
* اطلاعات ایمیل و پسورد را منتشر نکن
* در محیط واقعی از HTTPS استفاده کن

---

## 💡 توسعه‌های آینده

🚀 API اختصاصی
🎨 رابط کاربری پیشرفته‌تر
📊 داشبورد آماری
🔐 رمزنگاری پسورد (bcrypt)
⚡ Rate Limiting

---

## ❤️ سازنده

**AbolfazlNbDeV**

---

## ⭐ حمایت

اگر پروژه برات مفید بود، یه ⭐ بده 😉
