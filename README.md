<h1 align="center">
  <font color="#E63946">🔴 PYTHON SHORTLINK 🔴</font>
</h1>

<p align="center">
  <strong>🔥 A Blazing Fast, Enterprise-Ready URL Shortener Built for Speed & Security 🔥</strong>
</p>

<p align="center">
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python_3.8+-E63946.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <a href="https://flask.palletsprojects.com/"><img src="https://img.shields.io/badge/Flask_Backend-111111.svg?style=for-the-badge&logo=flask&logoColor=E63946" alt="Flask"></a>
  <a href="https://sqlite.org/"><img src="https://img.shields.io/badge/SQLite_DB-E63946.svg?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"></a>
  <a href="#"><img src="https://img.shields.io/badge/Status-Highly_Active-111111.svg?style=for-the-badge&logo=fire&logoColor=E63946" alt="Status"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-E63946.svg?style=for-the-badge" alt="License"></a>
</p>

<br>

<blockquote align="center">
  <p>سیستم مدیریت لینک قدرتمند، مجهز به پنل ادمین، احراز هویت دو مرحله‌ای و تحلیل دقیق کلیک‌ها. طراحی شده برای پایداری در ترافیک بالا.</p>
</blockquote>

---

## 📑 فهرست دسترسی سریع
- [🩸 ویژگی‌های کلیدی](#-ویژگیهای-کلیدی)
- [🧠 معماری و جریان داده](#-معماری-و-جریان-داده)
- [🚀 نصب و راه‌اندازی](#-نصب-و-راهاندازی)
- [🛑 تنظیمات امنیتی](#-تنظیمات-امنیتی-و-پیکربندی)
- [📡 مستندات API](#-مستندات-api)
- [📦 دیپلوی در پروداکشن](#-دیپلوی-در-پروداکشن)

---

## 🩸 ویژگی‌های کلیدی

- 🔴 **موتور تولید لینک فوق سریع:** استفاده از الگوریتم‌های بهینه‌سازی شده برای جلوگیری از تداخل (Collision).
- 🔴 **امنیت سطح Enterprise:** محافظت در برابر حملات Brute-Force، مجهز به Captcha سفارشی و سیستم Session Management.
- 🔴 **پنل مدیریت پیشرفته:** مانیتورینگ لحظه‌ای لینک‌ها، کاربران و منابع سیستم.
- 🔴 **سیستم تیکتینگ یکپارچه:** پلتفرم پشتیبانی داخلی برای ارتباط مستقیم کاربران و ادمین.
- 🔴 **ردیابی و آنالیتیکس:** شمارشگر دقیق کلیک‌ها با قابلیت تشخیص IP و User-Agent.

---

## 🧠 معماری و جریان داده

برای درک بهتر نحوه کارکرد بک‌اند، ساختار پردازش درخواست‌ها به شکل زیر مهندسی شده است (بدون نیاز به لود تصاویر خارجی):
```text
 ┌──────────────┐          [ 1. POST /shorten ]           ┌──────────────────┐
 │              ├────────────────────────────────────────▶│                  │
 │ Client/User  │                                         │  Flask App Core  │
 │              │◀────────────────────────────────────────┤                  │
 └──────┬───────┘         [ 2. Returns: short.id ]        └────────┬─────────┘
│                                                          │
│                 [ 3. GET /short.id ]                     │ (Read/Write)
└──────────────────────────────────────────────────────────┤
▼
 ┌──────────────┐         [ 5. HTTP 302 Redirect ]        ┌──────────────────┐
 │ Target URL   │◀────────────────────────────────────────┤   SQLite DB      │
 └──────────────┘                                         └──────────────────┘

---

## 🚀 نصب و راه‌اندازی

برای اجرای این سیستم در محیط لوکال خود، به پایتون `3.8` یا بالاتر نیاز دارید.

**۱. کلون کردن مخزن:**
bash
git clone https://github.com/AbolfazlNbDeV/python-shortlink.git
cd python-shortlink

**۲. ساخت و فعال‌سازی محیط ایزوله (Virtualenv):**
bash
python -m venv .venv
source .venv/bin/activate  # In Windows use: .venv\Scripts\activate

**۳. نصب وابستگی‌های هسته:**
bash
pip install --upgrade pip
pip install -r requirements.txt

---

## 🛑 تنظیمات امنیتی و پیکربندی

⚠️ **هشدار:** پیش از اجرای پروژه، حتماً کلیدهای امنیتی را تغییر دهید! 

فایل `config.py` را باز کرده و مقادیر زیر را به دقت تنظیم کنید:

python
# ----------------------------------
# 🔴 CORE SECURITY SETTINGS 🔴
# ----------------------------------
DOMAIN = "http://127.0.0.1:8000"
SECRET_KEY = "CHANGE_THIS_TO_A_VERY_LONG_RANDOM_STRING"

# ----------------------------------
# 📧 SMTP & MAIL CONFIGURATION
# ----------------------------------
EMAIL_SENDER = "support@yourdomain.com"
EMAIL_PASSWORD = "your_secure_app_password"

# ----------------------------------
# 👑 SUPERADMIN CREDENTIALS
# ----------------------------------
ADMIN_EMAIL = "admin@yourdomain.com"
ADMIN_PASSWORD = "Strong!Password#2024"
سپس برنامه را استارت بزنید:
bash
python app.py

---

## 📡 مستندات API

اگر می‌خواهید این سرویس را به اپلیکیشن‌های دیگر متصل کنید، می‌توانید از API های داخلی استفاده نمایید:

| متد | Endpoint | پارامترها (Body/Query) | توضیحات |
| :--- | :--- | :--- | :--- |
| <kbd>POST</kbd> | `/api/v1/shorten` | `{"url": "https://..."}` | تولید لینک کوتاه جدید |
| <kbd>GET</kbd> | `/api/v1/stats/<id>` | `None` | دریافت آمار کلیک‌های یک لینک |
| <kbd>GET</kbd> | `/<short_id>` | `None` | ریدایرکت به لینک اصلی (هدف) |

---

## 📦 دیپلوی در پروداکشن (Production)

اجرای این پروژه با سرور پیش‌فرض Flask در محیط واقعی **ممنوع** است. برای پرفورمنس بالا حتماً از ترکیب `Gunicorn` و `Nginx` استفاده کنید:

bash
# نصب Gunicorn
pip install gunicorn

# اجرا با ۴ ورکر (Worker) روی پورت ۸۰۰۰
gunicorn --workers 4 --bind 0.0.0.0:8000 app:app

---

## 📂 ساختار مهندسی فایل‌ها

text
📦 python-shortlink
 ┣ 📂 static             # 🎨 Assets (CSS, JS, Fonts)
 ┣ 📂 templates          # 🖼️ Jinja2 HTML Views
 ┣ 📜 app.py             # 🔴 Main App & Router 
 ┣ 📜 captcha.py         # 🛡️ Security & Anti-Bot
 ┣ 📜 config.py          # ⚙️ Environment Variables
 ┗ 📜 requirements.txt   # 📦 Dependencies

---

<p align="center">
  <b>کدنویسی شده با 🩸 و قهوه ☕ توسط <a href="https://github.com/AbolfazlNbDeV">AbolfazlNbDeV</a></b><br><br>
  ⭐️ <b>اگر این پروژه کیفیت کار شما را بالا برد، با دادن یک استار از آن حمایت کنید!</b> ⭐️
</p>
