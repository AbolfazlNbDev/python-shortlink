<h1 align="center">
  <font color="#E63946">PYTHON SHORTLINK</font>
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
  <a href="https://github.com/AbolfazlNbDeV/python-shortlink/stargazers"><img src="https://img.shields.io/github/stars/AbolfazlNbDeV/python-shortlink?style=social" alt="Stars"></a>
</p>

<br>

<blockquote align="center">
  <p>یک سیستم بسیار سریع و بهینه، کوتاه کننده لینک</p>
</blockquote>

---
## 🩸 ویژگی‌های کلیدی

- 🔴 موتور تولید لینک فوق سریع: استفاده از الگوریتم‌های بهینه‌سازی شده برای جلوگیری از تداخل (Collision).
- 🔴 امنیت سطح Enterprise: محافظت در برابر حملات Brute-Force، مجهز به Captcha سفارشی و سیستم Session Management.
- 🔴 پنل مدیریت پیشرفته: مانیتورینگ لحظه‌ای لینک‌ها، کاربران و منابع سیستم.
- 🔴 سیستم تیکتینگ یکپارچه: پلتفرم پشتیبانی داخلی برای ارتباط مستقیم کاربران و ادمین.
- 🔴 ردیابی و آنالیتیکس: شمارشگر دقیق کلیک‌ها با قابلیت تشخیص IP و User-Agent.

---

## 🧠 معماری و جریان داده

برای درک بهتر نحوه کارکرد بک‌اند، ساختار پردازش درخواست‌ها به شکل زیر مهندسی شده است (بدون نیاز به لود تصاویر خارجی):


 ┌──────────────┐           1. POST /shorten            ┌──────────────────┐
 │              ├────────────────────────────────────────▶│                  │
 │ Client/User  │                                         │  Flask App Core  │
 │              │◀────────────────────────────────────────┤                  │
 └──────┬───────┘          2. Returns: short.id         └────────┬─────────┘
│                                                          │
│                  3. GET /short.id                      │ (Read/Write)
└──────────────────────────────────────────────────────────┤
▼
 ┌──────────────┐          5. HTTP 302 Redirect         ┌──────────────────┐
 │ Target URL   │◀────────────────────────────────────────┤   SQLite DB      │
 └──────────────┘                                         └──────────────────┘

---

## 🚀 نصب و راه‌اندازی

برای اجرای این سیستم در محیط لوکال خود، به پایتون `3.8` یا بالاتر نیاز دارید.

۱. کلون کردن مخزن:
```bash
git clone https://github.com/AbolfazlNbDeV/python-shortlink.git
cd python-shortlink
```

۲. ساخت و فعال‌سازی محیط ایزوله (Virtualenv):
```bash
python -m venv .venv
source .venv/bin/activate  # In Windows use: .venv\Scripts\activate
```
۳. نصب وابستگی‌های هسته:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
---

## 🛑 اموزش ادیت کردن و ران کردن:
ابتدا فایل Config.py باز میکنید و تمام جاهایی که خالی هست یا من بهتون گفتم چی بزارید رو تکمیل میکنید و سیو میکنید و با توجه به مطالب بالا تر با دستور
```bash
python app.py
```
یا :
```bash
python3 app.py
```


