# ⚡ Python ShortLink | Ultra Advanced URL Shortener

<div align="center">

![Stars](https://img.shields.io/github/stars/AbolfazlNbDeV/python-shortlink?style=for-the-badge)
![Forks](https://img.shields.io/github/forks/AbolfazlNbDeV/python-shortlink?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-Fast%20%26%20Light-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success?style=for-the-badge)

<img src="https://readme-typing-svg.herokuapp.com/?font=Fira+Code&size=22&duration=3000&color=00F7FF&center=true&vCenter=true&width=600&lines=Powerful+URL+Shortener;Fast+%7C+Secure+%7C+Scalable;Built+with+Flask+%F0%9F%94%A5" />

</div>

---

## 🧠 معرفی پروژه

> یک سیستم حرفه‌ای و کامل برای کوتاه‌سازی لینک با قابلیت‌های پیشرفته، طراحی شده برای اجرا در دنیای واقعی 🚀

این پروژه فقط یک کوتاه‌کننده لینک ساده نیست —
یک **پلتفرم کامل مدیریت لینک + احراز هویت + پشتیبانی + پنل ادمین** است.

---

## ✨ قابلیت‌های خفن

<div align="center">

| 💡 قابلیت         | توضیح                      |
| ----------------- | -------------------------- |
| 🔗 Short Links    | ساخت لینک کوتاه با کد یکتا |
| 📊 Analytics      | شمارش کلیک و مدیریت        |
| 👤 Auth System    | ثبت‌نام، ورود، تایید ایمیل |
| 🔐 Security       | ریست پسورد + کپچا          |
| 🧑‍💻 Admin Panel | مدیریت کامل کاربران        |
| 📩 Support System | سیستم تیکت حرفه‌ای         |
| ⚡ Fast DB         | دیتابیس سبک و سریع         |
| 🔄 Auto Clean     | حذف خودکار لینک‌ها         |

</div>

---

## 🎯 چرا این پروژه خاصه؟

✔ بدون پیچیدگی اضافی
✔ مناسب برای دیپلوی سریع
✔ قابل توسعه برای استارتاپ
✔ ساختار تمیز و قابل فهم
✔ همه چیز در یک بک‌اند سبک

---

## 🛠️ تکنولوژی‌ها

<div align="center">

Python 🐍 • Flask 🌶️ • SQLite 🗄️ • Pillow 🎨 • SMTP 📧

</div>

---

## 📦 Requirements

```txt
flask
requests
beautifulsoup4
pillow
```

---

## ⚙️ نصب و اجرا

### 🚀 1. کلون پروژه

```bash
git clone https://github.com/AbolfazlNbDeV/python-shortlink.git
cd python-shortlink
```

---

### 🧪 2. ساخت محیط مجازی

```bash
python -m venv venv
```

فعال‌سازی:

```bash
# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

---

### 📥 3. نصب کتابخانه‌ها

```bash
pip install -r requirements.txt
```

---

### ⚙️ 4. تنظیم config

```python
admin = "your_admin_password"
emaill = "your_email"
passw = "your_email_app_password"
admin_email = "admin@domain.com"
domain = "yourdomain.com"
secret_key = "super_secret_key"
```

---

### ▶️ 5. اجرا

```bash
python app.py
```

🌐 اجرا روی:

```
http://127.0.0.1:8000
```

---

## 🧬 ساختار پروژه

```bash
python-shortlink/
│
├── app.py          # هسته اصلی پروژه
├── captcha.py      # تولید کپچا
├── config.py       # تنظیمات
├── database.db     # دیتابیس
├── requirements.txt
├── templates/
└── static/
```

---

## 🚀 اجرای حرفه‌ای (Production)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

---

## 🔥 ایده برای توسعه بیشتر

* 🌍 API عمومی
* 🎯 لینک سفارشی
* 📈 داشبورد آماری حرفه‌ای
* 🔐 هش کردن پسوردها
* ⚡ محدودسازی درخواست‌ها (Rate Limit)

---

## ❤️ سازنده

<div align="center">

**AbolfazlNbDeV**

</div>

---

## ⭐ حمایت

<div align="center">

اگر این پروژه برات مفید بود، یه ⭐ بده 🚀

</div>

---
