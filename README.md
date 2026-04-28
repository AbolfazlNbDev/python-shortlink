<div align="center">

<h1>🚀 Python ShortLink</h1>

<h3>Fast • Secure • Minimal URL Shortener</h3>

<p>
A lightweight URL shortener built with <b>Python</b> and <b>Flask</b>
</p>

<img src="https://img.shields.io/badge/python-3.10+-blue?style=for-the-badge">
<img src="https://img.shields.io/badge/flask-web%20framework-black?style=for-the-badge">
<img src="https://img.shields.io/badge/status-active-success?style=for-the-badge">
<img src="https://img.shields.io/github/stars/AbolfazlNbDeV/python-shortlink?style=for-the-badge">

</div>

<br>

<hr>

<h2 dir="rtl">📌 معرفی پروژه</h2>

<p dir="rtl">

Python ShortLink یک سرویس ساده اما قدرتمند برای **کوتاه کردن لینک‌ها** است که با استفاده از فریم‌ورک Flask توسعه داده شده است.

این پروژه برای افرادی مناسب است که می‌خواهند:

• یک سرویس کوتاه‌کننده لینک شخصی داشته باشند  
• نحوه ساخت URL Shortener با Flask را یاد بگیرند  
• یک پروژه سبک برای Deploy روی سرور داشته باشند  

ساختار پروژه ساده، قابل توسعه و مناسب برای استفاده در پروژه‌های واقعی است.

</p>

<hr>

<h2 dir="rtl">✨ قابلیت‌ها</h2>

<ul dir="rtl">

<li>🔗 تولید لینک کوتاه برای هر URL</li>

<li>⚡ ریدایرکت سریع و بهینه</li>

<li>🛡️ سیستم CAPTCHA برای جلوگیری از اسپم</li>

<li>🔐 امنیت مناسب و جلوگیری از abuse</li>

<li>📦 ساختار ماژولار و تمیز</li>

<li>⚙️ تنظیمات جداگانه در فایل config</li>

<li>🚀 مناسب برای Deploy روی VPS یا Cloud</li>

<li>💡 قابل توسعه برای اضافه کردن پنل مدیریت</li>

</ul>

<hr>

<h2 dir="rtl">🧠 نحوه کار سیستم</h2>

<p dir="rtl">

مراحل عملکرد سیستم به شکل زیر است:

1️⃣ کاربر لینک اصلی را وارد می‌کند  
2️⃣ سیستم یک شناسه کوتاه تولید می‌کند  
3️⃣ لینک کوتاه در دیتابیس ذخیره می‌شود  
4️⃣ هنگام باز کردن لینک کوتاه، کاربر به لینک اصلی ریدایرکت می‌شود  

</p>

<hr>

<h2 dir="rtl">📂 ساختار پروژه</h2>

<pre>

python-shortlink
│
├── app.py
├── config.py
├── captcha.py
├── README.md
│
├── templates/
│
└── static/

</pre>

<p dir="rtl">

توضیح فایل‌ها:

<b>app.py</b>  
هسته اصلی برنامه Flask

<b>config.py</b>  
تنظیمات پروژه

<b>captcha.py</b>  
سیستم تولید کپچا

</p>

<hr>

<h2 dir="rtl">⚙️ پیش‌نیازها</h2>

<ul dir="rtl">

<li>Python 3.10 یا جدیدتر</li>
<li>pip</li>
<li>Git</li>

</ul>

<hr>

<h2 dir="rtl">📦 نصب پروژه</h2>

<pre>
git clone https://github.com/AbolfazlNbDeV/python-shortlink

cd python-shortlink
</pre>

ساخت محیط مجازی:

<pre>
python -m venv venv
</pre>

فعال‌سازی:

Linux / Mac

<pre>
source venv/bin/activate
</pre>

Windows

<pre>
venv\Scripts\activate
</pre>

نصب کتابخانه‌ها:

<pre>
pip install -r requirements.txt
</pre>

اجرای پروژه:

<pre>
python app.py
</pre>

سپس در مرورگر:

<pre>
http://localhost:5000
</pre>

<hr>

<h2 dir="rtl">📜 فایل requirements.txt</h2>

این فایل را در پروژه قرار بده:

<pre>

Flask
Pillow
Werkzeug
itsdangerous
Jinja2

</pre>

در صورت نیاز می‌توانی اضافه کنی:

<pre>

gunicorn
python-dotenv

</pre>

<hr>

<h2 dir="rtl">🚀 دیپلوی پروژه</h2>

<h3>Deploy روی VPS</h3>

نصب Python:

<pre>
sudo apt install python3
</pre>

کلون پروژه:

<pre>
git clone https://github.com/AbolfazlNbDeV/python-shortlink
</pre>

نصب وابستگی‌ها:

<pre>
pip install -r requirements.txt
</pre>

اجرای پروژه:

<pre>
python app.py
</pre>

برای اجرای دائمی بهتر است از:

<pre>
gunicorn
</pre>

استفاده شود.

<hr>

<h3>Deploy با Gunicorn</h3>

<pre>
pip install gunicorn
</pre>

اجرای سرور:

<pre>
gunicorn app:app
</pre>

<hr>

<h3>Deploy روی Render</h3>

1️⃣ پروژه را در GitHub قرار بده  
2️⃣ وارد Render شو  
3️⃣ New Web Service بزن  
4️⃣ ریپازیتوری را انتخاب کن  

Build Command:

<pre>
pip install -r requirements.txt
</pre>

Start Command:

<pre>
gunicorn app:app
</pre>

<hr>

<h3>Deploy روی Railway</h3>

1️⃣ پروژه را Push کن در GitHub  
2️⃣ Railway را باز کن  
3️⃣ Deploy from GitHub  
4️⃣ repository را انتخاب کن  

<hr>

<h2 dir="rtl">🔐 امنیت</h2>

<ul dir="rtl">

<li>اطلاعات حساس در سورس قرار نگرفته است</li>

<li>تنظیمات قابل مدیریت در config.py هستند</li>

<li>برای امنیت بیشتر می‌توان environment variable اضافه کرد</li>

</ul>

<hr>

<h2 dir="rtl">💡 ایده برای توسعه پروژه</h2>

<ul dir="rtl">

<li>پنل مدیریت</li>

<li>آمار کلیک لینک</li>

<li>API کوتاه‌کننده لینک</li>

<li>سیستم کاربران</li>

<li>QR Code برای لینک‌ها</li>

</ul>

<hr>

<div align="center">

<h2>⭐ Support</h2>

اگر این پروژه برایت مفید بود  
یک ⭐ به ریپازیتوری بده

<br><br>

<b>GitHub</b>

<br>

<a href="https://github.com/AbolfazlNbDeV">
AbolfazlNbDeV
</a>

</div>
