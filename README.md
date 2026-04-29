<h1 align="center">
  <font color="#E63946">PYTHON SHORTLINK</font>
</h1>

<p align="center">
  <strong>🔥 A Blazing Fast, Enterprise‑Ready URL Shortener Built for Speed & Security 🔥</strong>
</p>

<p align="center">
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python_3.8+-E63946.svg?style=for-the-badge&logo=python&logoColor=white"></a>
  <a href="https://flask.palletsprojects.com/"><img src="https://img.shields.io/badge/Flask_Backend-111111.svg?style=for-the-badge&logo=flask&logoColor=E63946"></a>
  <a href="https://sqlite.org/"><img src="https://img.shields.io/badge/SQLite_DB-E63946.svg?style=for-the-badge&logo=sqlite&logoColor=white"></a>
  <a href="#"><img src="https://img.shields.io/badge/Status-Highly_Active-111111.svg?style=for-the-badge&logo=fire&logoColor=E63946"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-E63946.svg?style=for-the-badge"></a>
  <a href="https://github.com/AbolfazlNbDeV/python-shortlink/stargazers"><img src="https://img.shields.io/github/stars/AbolfazlNbDeV/python-shortlink?style=social"></a>
</p>

<br>

<blockquote align="center">
  <p>یک سیستم بسیار سریع و بهینه کوتاه کننده لینک با معماری ماژولار و امنیت بالا</p>
</blockquote>

---

# 🩸 ویژگی‌های کلیدی

- موتور تولید لینک فوق سریع با جلوگیری از Collision
- امنیت بالا در برابر Brute Force
- سیستم Captcha سفارشی
- مدیریت Session ایمن
- پنل مدیریت کامل برای ادمین
- سیستم تیکت پشتیبانی
- آنالیز کلیک‌ها و آمار کاربران
- ذخیره IP و User-Agent
- معماری ماژولار برای توسعه راحت

---

# 🧠 معماری و جریان داده

 ┌──────────────┐           POST /shorten            ┌──────────────────┐
 │              ├────────────────────────────────────▶│                  │
 │ Client/User  │                                     │  Flask App Core  │
 │              │◀────────────────────────────────────┤                  │
 └──────┬───────┘        Returns short link           └────────┬─────────┘
        │                                                       │
        │                     GET /short.id                     │
        └───────────────────────────────────────────────────────┤
                                                                ▼
                                                      ┌──────────────────┐
                                                      │    SQLite DB     │
                                                      └────────┬─────────┘
                                                               │
                                                               ▼
                                                     HTTP 302 Redirect
                                                               │
                                                               ▼
                                                        Target Website

---

# 🚀 نصب و راه‌اندازی

برای اجرای این پروژه به Python 3.8 یا بالاتر نیاز دارید.

Clone Project

git clone https://github.com/AbolfazlNbDeV/python-shortlink.git
cd python-shortlink

---

Create Virtual Environment

python -m venv .venv

Linux / Mac

source .venv/bin/activate

Windows

.venv\Scripts\activate

---

Install Requirements

pip install --upgrade pip
pip install -r requirements.txt

---

# ⚙️ Configuration

فایل زیر را باز کنید:

Config.py

نمونه تنظیمات:

BASE_URL = "http://localhost:5000"
SECRET_KEY = "CHANGE_THIS_SECRET_KEY"
DATABASE = "shortlink.db"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "strongpassword"

---

# ▶️ Run Application

python app.py

یا

python3 app.py

باز کردن در مرورگر:

http://localhost:5000

---

# 🧪 Test Example

https://your-domain.com/aB3Xk9

با باز کردن این لینک کاربر به لینک اصلی هدایت می‌شود.

---

# 📁 Project Structure

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

# ⚡ Advanced Features

- Secure Random ID Generation
- Collision Prevention Algorithm
- Rate Limiting Ready
- Session Security
- Click Tracking System
- Modular Architecture
- Production Ready Structure

---

# 🔐 Production Security Tips

- Use Nginx Reverse Proxy
- Run with Gunicorn
- Enable HTTPS
- Add Rate Limiting
- Use PostgreSQL or Redis

---

# 🧩 Contributing

git checkout -b feature/new-feature
git commit -m "Add new feature"
git push origin feature/new-feature

سپس Pull Request ارسال کنید.

---

# ⭐ Support Project

اگر این پروژه برای شما مفید بود لطفاً در GitHub به آن Star بدهید.

https://github.com/AbolfazlNbDeV/python-shortlink

---

# 👨‍💻 Developer

AbolfazlNbDeV

https://github.com/AbolfazlNbDeV

---

# 📜 License

MIT License
