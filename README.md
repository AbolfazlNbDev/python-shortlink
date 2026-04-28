# 🚀 Python Shortener | پروژه کوتاه‌ساز لینک پیشرفته

<div align="center">

![GitHub stars](https://img.shields.io/github/stars/AbolfazlNbDeV/python-shortlink?style=social)
![GitHub forks](https://img.shields.io/github/forks/AbolfazlNbDeV/python-shortlink?style=social)
![License](https://img.shields.io/github/license/AbolfazlNbDeV/python-shortlink)
![Python Version](https://img.shields.io/badge/python-3.8+-blue)

</div>

<p align="center">
  یک سیستم کوتاه‌ساز لینک (Shortener) قدرتمند، سبک و قابل دیپلوی که با استفاده از پایتون و گیت‌هاب هاب توسعه یافته است.
  <br>
  <a href="#-قابلیت-ها"><strong>کاوش قابلیت‌ها</strong></a> ·
  <a href="#-نصب-و-راه‌اندازی"><strong>نصب و راه‌اندازی</strong></a> ·
  <a href="#-دیپلوی-روی-گیت‌هاب"><strong>دیپلوی روی گیت‌هاب</strong></a>
</p>

---

## ✨ قابلیت‌ها

این پروژه با هدف ایجاد یک ابزار ساده اما کارآمد برای مدیریت لینک‌ها طراحی شده است:

*   🛠 **تک‌فایل و سبک:** تمام منطق برنامه در یک فایل `app.py` (یا مشابه) پیاده‌سازی شده است.
*   🎨 **رابط کاربری مدرن:** استفاده از HTML/CSS تمیز برای نمایش زیبا.
*   🔗 **اتصال به گیت‌هاب:** ذخیره لینک‌های کوتاه شده به صورت خودکار در مخزن گیت‌هاب (از طریق API).
*   📊 **مدیریت آسان:** امکان مشاهده لیست لینک‌ها و وضعیت آن‌ها.
*   🚀 **دیپلوی آسان:** قابلیت اجرای سریع روی پلتفرم‌های مختلف (Heroku, Vercel, GitHub Pages با سرویس‌دهنده‌های جانبی).

---

## 📦 پیش‌نیازها و کتابخانه‌های مورد نیاز

برای اجرای این پروژه، شما به پایتون نسخه 3.8 یا بالاتر نیاز دارید. کتابخانه‌های زیر در فایل `requirements.txt` قرار گرفته‌اند:

```txt
# محتویات فایل requirements.txt
flask
requests
pillow
beautifulsoup4

git clone https://github.com/AbolfazlNbDeV/python-shortlink.git
cd python-shortlink

python -m venv venv
# در ویندوز:
venv\Scripts\activate
# در مک/لینوکس:
source venv/bin/activate

pip install -r requirements.txt
