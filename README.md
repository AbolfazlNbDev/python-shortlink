<h1 align="center">
  🔗 Python ShortLink
</h1>

<p align="center">
  <strong>A High-Performance, Lightweight URL Shortener Built with Flask and SQLite.</strong>
</p>

<p align="center">
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.8+-blue.svg?style=flat-square&logo=python&logoColor=white" alt="Python"></a>
  <a href="https://flask.palletsprojects.com/"><img src="https://img.shields.io/badge/Flask-2.x-black.svg?style=flat-square&logo=flask&logoColor=white" alt="Flask"></a>
  <a href="https://sqlite.org/"><img src="https://img.shields.io/badge/Database-SQLite-003B57.svg?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite"></a>
  <a href="https://github.com/AbolfazlNbDeV/python-shortlink/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg?style=flat-square" alt="License"></a>
  <a href="https://github.com/AbolfazlNbDeV/python-shortlink/stargazers"><img src="https://img.shields.io/github/stars/AbolfazlNbDeV/python-shortlink?style=flat-square&color=yellow" alt="Stars"></a>
</p>

<br>

پروژه **Python ShortLink** یک پلتفرم کامل و مستقل برای کوتاه کردن لینک‌ها، مدیریت کاربران و بررسی آمار است. این سیستم با تمرکز بر سرعت، امنیت و سادگی توسعه داده شده و به راحتی روی هر سروری قابل پیاده‌سازی است.

## 📑 فهرست مطالب
- [✨ ویژگی‌ها](#-ویژگیها)
- [🏗 معماری سیستم](#-معماری-سیستم)
- [🚀 شروع سریع](#-شروع-سریع)
- [⚙️ پیکربندی](#️-پیکربندی)
- [📦 استقرار (Deployment)](#-استقرار-در-محیط-واقعی)
- [🤝 مشارکت](#-مشارکت)

---

## ✨ ویژگی‌ها

- **تولید لینک‌های یکتا:** الگوریتم سریع برای تولید شناسه‌های کوتاه و غیرتکراری.
- **سیستم احراز هویت جامع:** ثبت‌نام، ورود، تاییدیه ایمیل و بازیابی رمز عبور.
- **داشبورد مدیریت (Admin Panel):** کنترل کامل روی کاربران، لینک‌ها و تنظیمات سیستم.
- **سیستم پشتیبانی:** امکان ارسال تیکت توسط کاربران و پاسخ‌دهی توسط ادمین.
- **امنیت بالا:** پیاده‌سازی کپچا (Captcha) اختصاصی و مدیریت امن نشست‌ها (Sessions).
- **آمار و تحلیل:** شمارش دقیق کلیک‌ها برای هر لینک کوتاه شده.

---

## 🏗 معماری سیستم

جریان کاری پروژه به شکل زیر طراحی شده است:
```mermaid
sequenceDiagram
participant User
participant FlaskApp as Flask Backend
participant DB as SQLite / SQLAlchemy

User->>FlaskApp: ارسال لینک طولانی (POST /shorten)
FlaskApp->>FlaskApp: تولید شناسه یکتا (Unique Hash)
FlaskApp->>DB: ذخیره شناسه و لینک اصلی
DB-->>FlaskApp: تایید ذخیره‌سازی
FlaskApp-->>User: بازگرداندن لینک کوتاه (short.link/xyz)

User->>FlaskApp: کلیک روی لینک کوتاه (GET /xyz)
FlaskApp->>DB: جستجوی شناسه + ثبت 1 کلیک
DB-->>FlaskApp: بازگرداندن لینک اصلی
FlaskApp-->>User: ریدایرکت (302 Redirect) به هدف
*(نکته: گیت‌هاب به صورت خودکار نمودار بالا را رندر کرده و نمایش می‌دهد که جلوه بسیار حرفه‌ای به پروژه می‌بخشد).*

---

## 🚀 شروع سریع

برای اجرای این پروژه در محیط توسعه (Local Development)، مراحل زیر را دنبال کنید.

### ۱. دریافت پروژه
bash
git clone https://github.com/AbolfazlNbDeV/python-shortlink.git
cd python-shortlink

### ۲. تنظیم محیط مجازی (Virtual Environment)
bash
python -m venv venv
# در ویندوز:
venv\Scripts\activate
# در لینوکس/مک:
source venv/bin/activate

### ۳. نصب وابستگی‌ها
bash
pip install --upgrade pip
pip install -r requirements.txt

---

## ⚙️ پیکربندی

پروژه برای اجرا نیازمند تنظیم متغیرهای محیطی و پیکربندی‌های اولیه است. فایل `config.py` را باز کرده و مقادیر زیر را تنظیم کنید:

python
# config.py

DOMAIN = "http://127.0.0.1:8000"
SECRET_KEY = "your-super-secret-key"

# تنظیمات ایمیل (برای تاییدیه و پشتیبانی)
EMAIL_SENDER = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"

# تنظیمات ادمین
ADMIN_EMAIL = "admin@domain.com"
ADMIN_PASSWORD = "secure_admin_password"

پس از انجام تنظیمات، دیتابیس را مقداردهی اولیه کرده و پروژه را اجرا کنید:

bash
python app.py
سرور در آدرس `http://127.0.0.1:8000` در دسترس خواهد بود.

---

## 📦 استقرار در محیط واقعی (Production)

برای اجرای پایدار در سرورهای اصلی، استفاده از `Gunicorn` به شدت توصیه می‌شود. هرگز از سرور داخلی Flask برای محیط Production استفاده نکنید.

bash
# نصب Gunicorn
pip install gunicorn

# اجرای پروژه با 4 پردازشگر موازی
gunicorn -w 4 -b 0.0.0.0:8000 app:app

---

## 🛡 ساختار فایل‌ها

ساختار دایرکتوری‌ها بر اساس استانداردهای فریم‌ورک Flask چیده شده است:

text
.
├── app.py                 # نقطه ورود (Entry Point) و روت‌های اصلی برنامه
├── captcha.py             # ماژول تولید و اعتبارسنجی تصاویر امنیتی
├── config.py              # تنظیمات و متغیرهای سراسری
├── requirements.txt       # لیست پکیج‌های پایتون
├── static/                # فایل‌های استاتیک (CSS, JS, Images)
└── templates/             # قالب‌های Jinja2 (HTML)

---

## 🤝 مشارکت

ما از Pull Request ها استقبال می‌کنیم. برای تغییرات بزرگ، لطفاً ابتدا یک Issue باز کنید تا در مورد آنچه می‌خواهید تغییر دهید بحث کنیم.

1. پروژه را Fork کنید.
2. برنچ ویژگی جدید خود را بسازید (`git checkout -b feature/NewFeature`).
3. تغییرات خود را Commit کنید (`git commit -m 'Add some NewFeature'`).
4. برنچ را Push کنید (`git push origin feature/NewFeature`).
5. یک Pull Request باز کنید.

---

<p align="center">
  ساخته شده با ❤️ توسط <a href="https://github.com/AbolfazlNbDeV">AbolfazlNbDeV</a>
  <br>
  اگر این پروژه برای شما مفید بود، دادن یک ⭐️ فراموش نشود!
</p>


### چرا این نسخه بسیار حرفه‌ای‌تر (و به اصطلاح خفن‌تر) است؟
1. **طراحی تخت (Flat Design):** به جای بدج‌های پلاستیکی و براق، از بدج‌های `flat-square` استفاده شده که در پروژه‌های سطح بالا (مثل داکر، ری‌اکت و...) استفاده میشه.
2. **نمودار معماری (Mermaid):** بخش `معماری سیستم` با یک کد `mermaid` نوشته شده. گیت‌هاب این کد رو به یک **فلوچارت گرافیکی فوق‌العاده زیبا** تبدیل میکنه. دولوپرها وقتی این فلوچارت رو تو یه ریپازیتوری میبینن، بلافاصله متوجه میشن که سازنده یه برنامه‌نویس سطح بالاست.
3. **فاصله‌گذاری استاندارد (Whitespace):** تگ‌های HTML اضافی حذف شدن و به جای اون از خطوط جداکننده (`---`) و فاصله‌های استاندارد مارک‌داون استفاده شده تا هیچ‌چیزی تو هم نره.
4. **لحن اینترپرایز:** کلماتی که استفاده شده (مثل استقرار، مقداردهی اولیه، محیط مجازی) دقیقاً کلماتی هستن که در شرکت‌های بزرگ نرم‌افزاری به کار میرن.
5. **ساختار درختی فایل‌ها (Tree View):** به جای استفاده از ایموجی‌های پوشه که ممکنه روی هر سیستمی یه شکل باشه، از کاراکترهای استاندارد ASCII-Art برای نمایش فایل‌ها استفاده شده که به شدت بین هکرها و دولوپرهای بک‌اند محبوبه.
