<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=00F7FF&height=250&section=header&text=⚡%20Python%20ShortLink&fontSize=50&animation=fadeIn&fontAlignY=38&desc=Ultra%20Advanced%20URL%20Shortener&descAlignY=58&descAlign=62" />

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-Fast%20%26%20Light-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Fast%20DB-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org/)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-2EA043?style=for-the-badge&logo=github&logoColor=white)](#)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

<br>

<img src="https://readme-typing-svg.herokuapp.com/?font=Fira+Code&size=22&duration=3000&color=00F7FF&center=true&vCenter=true&width=600&lines=Powerful+URL+Shortener+🚀;Fast+%7C+Secure+%7C+Scalable+🔒;Built+with+Flask+%F0%9F%94%A5;Manage+Links+Like+a+Pro!+✨" />

**یک پلتفرم کامل و بی‌نقص برای مدیریت لینک، احراز هویت، پشتیبانی و پنل ادمین**

[گزارش باگ](https://github.com/AbolfazlNbDeV/python-shortlink/issues) · [درخواست قابلیت جدید](https://github.com/AbolfazlNbDeV/python-shortlink/issues) · [مشارکت در پروژه](#-مشارکت)

</div>

---

## 📑 فهرست مطالب
- [معرفی پروژه](#-معرفی-پروژه)
- [قابلیت‌های کلیدی](#-قابلیت‌های-کلیدی-و-خفن)
- [چرا این پروژه؟](#-چرا-این-پروژه-خاصه)
- [پیش‌نیازها و نصب](#-پیش‌نیازها-و-نصب)
- [ساختار فایل‌ها](#-ساختار-پروژه)
- [اجرا در پروداکشن](#-اجرای-حرفه‌ای-production)
- [ارتباط با سازنده](#-ارتباط-با-سازنده)

---

## 🧠 معرفی پروژه

> این پروژه فراتر از یک کوتاه‌کننده لینک ساده است! سیستمی کاملاً حرفه‌ای طراحی شده برای اجرای واقعی (Production-Ready) که تمامی نیازهای مدیریت لینک، کاربران و پشتیبانی را در یک بک‌اند سبک و سریع به شما ارائه می‌دهد.

---

## ✨ قابلیت‌های کلیدی و خفن

<details open>
<summary><b>نمایش لیست قابلیت‌ها (کلیک کنید)</b></summary>
<br>

| 💡 قابلیت | 📝 توضیحات | 🛠 تکنولوژی / ابزار |
| :--- | :--- | :--- |
| 🔗 **Short Links** | ساخت لینک‌های کوتاه با کدهای یکتا و غیرقابل حدس | `Flask Routing` |
| 📊 **Analytics** | شمارش دقیق کلیک‌ها و مدیریت آمار هر لینک | `SQLite` |
| 👤 **Auth System** | سیستم کامل ثبت‌نام، ورود و تاییدیه ایمیل | `SMTP & Sessions` |
| 🔐 **Security** | بازیابی رمز عبور + سیستم امنیتی کپچا (Captcha) | `Pillow` |
| 🧑‍💻 **Admin Panel** | پنل مدیریت قدرتمند برای کنترل کاربران و لینک‌ها | `Jinja2` |
| 📩 **Support System** | سیستم تیکتینگ حرفه‌ای برای ارتباط کاربران و ادمین | `DB Relational` |
| ⚡ **Fast DB** | دیتابیس سبک و بی‌نهایت سریع با کانکشن‌های بهینه | `SQLAlchemy / SQLite` |
| 🔄 **Auto Clean** | کرون‌جاب داخلی برای حذف خودکار لینک‌های منقضی شده | `Python Scripts` |

</details>

---

## 🎯 چرا این پروژه خاصه؟

* **بدون پیچیدگی اضافی:** کدهای تمیز (Clean Code) و معماری قابل فهم برای همه.
* **دیپلوی سریع:** آماده اجرا روی انواع سرورها (VPS, PaaS) در کمتر از ۵ دقیقه.
* **مقیاس‌پذیری:** پایه‌ای قدرتمند برای تبدیل شدن به یک استارتاپ بزرگ.
* **All-in-One:** همه‌چیز (بک‌اند، فرانت‌اند، دیتابیس) بهینه‌شده در یک پکیج.

---

## 🚀 پیش‌نیازها و نصب

برای اجرای این پروژه روی سیستم خود، مراحل زیر را به ترتیب دنبال کنید:

### ۱. دریافت سورس کد
```bash
git clone https://github.com/AbolfazlNbDeV/python-shortlink.git
cd python-shortlink

### ۲. ساخت و فعال‌سازی محیط مجازی (Virtual Env)
<details>
<summary><b>راهنمای سیستم‌عامل‌های مختلف</b></summary>

**ویندوز:**
bash
python -m venv venv
venv\Scripts\activate

**لینوکس / مک:**
bash
python3 -m venv venv
source venv/bin/activate
</details>

### ۳. نصب کتابخانه‌ها
bash
pip install -U pip
pip install -r requirements.txt

### ۴. پیکربندی (Config)
فایل `config.py` را باز کرده و مقادیر زیر را با اطلاعات خود جایگزین کنید:
python
admin = "your_admin_password"         # رمز عبور پنل ادمین
emaill = "your_email@gmail.com"       # ایمیل فرستنده (برای تاییدیه و پشتیبانی)
passw = "your_email_app_password"     # App Password ایمیل شما
admin_email = "admin@domain.com"      # ایمیل مدیر
domain = "http://127.0.0.1:8000"      # دامنه پروژه شما
secret_key = "super_secret_key_here"  # کلید امنیتی (یک رشته طولانی و تصادفی)

### ۵. اجرای پروژه
bash
python app.py
> 🌐 پروژه شما اکنون در `http://127.0.0.1:8000` در دسترس است!

---

## 🧬 ساختار پروژه

text
📦 python-shortlink
 ┣ 📂 templates/       # فایل‌های HTML و فرانت‌اند
 ┣ 📂 static/          # فایل‌های CSS, JS و تصاویر
 ┣ 📜 app.py           # هسته اصلی و روتینگ پروژه
 ┣ 📜 captcha.py       # ماژول تولید تصاویر کپچا
 ┣ 📜 config.py        # متغیرهای پیکربندی
 ┣ 📜 database.db      # دیتابیس لوکال
 ┗ 📜 requirements.txt # لیست وابستگی‌ها

---

## ⚡ اجرای حرفه‌ای (Production)

برای اجرای پروژه در محیط واقعی و سرورهای اصلی، استفاده از وب‌سرورهای قدرتمند مثل Gunicorn پیشنهاد می‌شود:

bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
*نکته: عدد ۴ نمایانگر تعداد Worker ها می‌باشد (معمولاً ۲ برابر تعداد هسته‌های CPU).*

---

## 🔥 نقشه راه توسعه (Roadmap)

- [ ] 🌍 طراحی API عمومی (RESTful) برای توسعه‌دهندگان
- [ ] 🎯 قابلیت ثبت لینک‌های سفارشی (Custom Alias)
- [ ] 📈 ساخت داشبورد آماری گرافیکی با نمودار (Chart.js)
- [ ] 🔐 پیاده‌سازی سیستم هشینگ پیشرفته (Bcrypt) برای پسوردها
- [ ] ⚡ اضافه کردن Rate Limit برای جلوگیری از حملات DDoS و اسپم

---

## 🤝 مشارکت

از مشارکت شما استقبال می‌کنیم! برای اضافه کردن قابلیت‌های جدید:
1. پروژه را Fork کنید.
2. یک Branch جدید بسازید (`git checkout -b feature/AmazingFeature`).
3. تغییرات را Commit کنید (`git commit -m 'Add some AmazingFeature'`).
4. پوش کنید (`git push origin feature/AmazingFeature`).
5. یک Pull Request ثبت کنید.

---

<div align="center">

## ❤️ ارتباط با سازنده

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AbolfazlNbDeV)

**توسعه داده شده با ☕ و ❤️ توسط AbolfazlNbDeV**

اگر این پروژه برات مفید بود، با دادن یک ⭐ (Star) به این ریپازیتوری از من حمایت کن!

<img src="https://media.giphy.com/media/WUlplcMpM1XPNpDMoN/giphy.gif" width="60">

</div>
