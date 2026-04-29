cat > README.md << 'EOF'
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=200&section=header&text=PYTHON%20SHORTLINK&fontSize=45&fontColor=ffffff&animation=fadeIn&fontAlignY=35"/>
</p>

<h2 align="center">🔗 Ultra Fast & Secure Python Link Shortener</h2>
<h3 align="center">Built with Flask • SQLite • Authentication • CAPTCHA • Admin Panel</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python%203.8+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Framework-Flask-black?style=for-the-badge&logo=flask">
  <img src="https://img.shields.io/badge/Database-SQLite-green?style=for-the-badge&logo=sqlite">
  <img src="https://img.shields.io/github/stars/AbolfazlNbDeV/python-shortlink?style=for-the-badge">
  <img src="https://img.shields.io/github/forks/AbolfazlNbDeV/python-shortlink?style=for-the-badge">
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=AbolfazlNbDeV&label=PROFILE%20VIEWS&color=blueviolet&style=for-the-badge">
</p>

---

# 🧠 معرفی پروژه

Python Shortlink یک سیستم سریع و امن برای کوتاه کردن لینک‌ها است که با Flask ساخته شده و به راحتی روی سرور یا سیستم شخصی اجرا می‌شود.

این پروژه شامل سیستم کامل احراز هویت، پنل کاربری، پنل ادمین، کپچای اختصاصی و دیتابیس SQLite است.

---

# ✨ ویژگی‌ها

✅ تولید لینک کوتاه  
✅ ریدایرکت سریع  
✅ دیتابیس SQLite  
✅ احراز هویت با ایمیل  
✅ تایید ایمیل واقعی  
✅ کپچا دست ساز  
✅ پنل ادمین  
✅ داشبورد کاربران  
✅ سیستم تیکت  
✅ حذف حساب  
✅ تغییر پسورد  
✅ مناسب سرور و لوکال  

---

# 🏗 معماری سیستم

Client ➜ Flask Server ➜ Database ➜ Redirect

1. کاربر لینک را ارسال می‌کند  
2. سیستم یک شناسه کوتاه تولید می‌کند  
3. لینک در دیتابیس ذخیره می‌شود  
4. هنگام باز شدن لینک کوتاه کاربر به لینک اصلی هدایت می‌شود  

---

# 🚀 اجرای پروژه

clone پروژه

\`\`\`bash
git clone https://github.com/AbolfazlNbDeV/python-shortlink.git
\`\`\`

ورود به پوشه پروژه

\`\`\`bash
cd python-shortlink
\`\`\`

ساخت محیط مجازی

\`\`\`bash
python -m venv .venv
\`\`\`

فعال سازی محیط مجازی

Linux / Mac

\`\`\`bash
source .venv/bin/activate
\`\`\`

Windows

\`\`\`bash
.venv\Scripts\activate
\`\`\`

نصب وابستگی ها

\`\`\`bash
pip install --upgrade pip
pip install -r requirements.txt
\`\`\`

اجرای برنامه

\`\`\`bash
python app.py
\`\`\`

باز کردن در مرورگر

\`\`\`
http://localhost:5000
\`\`\`

---

# ⚙️ تنظیمات

فایل زیر را ویرایش کنید

Config.py

نمونه:

\`\`\`python
MAIL_USERNAME = "example@gmail.com"
MAIL_PASSWORD = "your-app-password"
SECRET_KEY = "Im Programmer 2026"
\`\`\`

---

# 📊 آمار گیت‌هاب

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=AbolfazlNbDeV&show_icons=true&theme=tokyonight">
</p>

---

# ⭐ حمایت از پروژه

اگر این پروژه برای شما مفید بود لطفاً در گیت‌هاب ⭐ بدهید

https://github.com/AbolfazlNbDeV/python-shortlink

---

# 👨‍💻 توسعه‌دهنده

AbolfazlNbDeV

https://github.com/AbolfazlNbDeV

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=120&section=footer"/>
</p>
EOF
