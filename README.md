<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:f00000,50:8b0000,100:4b0000&height=200&section=header&text=QR%20CODE%20CREATOR&fontSize=40&fontColor=ffffff&animation=fadeIn&fontAlignY=35"/>
</p>

<h3 align="center">
سیستم ساخت QR Code سریع، سبک و حرفه‌ای با Python و Tkinter
</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-red?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Tkinter-UI-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/QR%20Generator-qrcode-black?style=for-the-badge">
  <img src="https://img.shields.io/badge/Windows-Installer-blue?style=for-the-badge&logo=windows">
  <img src="https://img.shields.io/github/stars/AbolfazlNbDev/python-shortlink?style=for-the-badge">
  <img src="https://img.shields.io/github/forks/AbolfazlNbDev/python-shortlink?style=for-the-badge">
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=YOUR_USERNAME&label=Profile%20Views&color=red&style=for-the-badge">
</p>

---

# 🧠 معرفی پروژه

**QR Code Creator** یک نرم‌افزار دسکتاپی سریع، سبک و کاربرپسند برای ساخت QR Code از هر متن یا لینک است.

این برنامه با رابط کاربری ساده و ظاهر جذاب، به شما اجازه می‌دهد:

- متن یا لینک مورد نظر را وارد کنید  
- رنگ پس‌زمینه QR را انتخاب کنید  
- رنگ اصلی QR (بردر) را تنظیم کنید  
- خروجی را به صورت تصویر باکیفیت ذخیره کنید  

هدف اصلی این پروژه، ساخت یک ابزار ساده، تمیز و در عین حال حرفه‌ای برای ساخت QR Code روی ویندوز است.

---

# 📥 دانلود برنامه (فقط از بخش Releases)

برای دانلود آخرین نسخه برنامه (فایل exe یا Setup):

👉 **حتماً از بخش Releases گیت‌هاب استفاده کنید:**

➡️ **[Download From Releases](../../releases)**

> ⚠️ توجه:  
> - فایل‌های exe / setup داخل سورس قرار داده نشده‌اند.  
> - فقط در بخش **Releases** منتشر می‌شوند.  

---

# ✨ ویژگی‌ها

✅ ساخت QR Code از متن یا لینک  
✅ انتخاب رنگ پس‌زمینه QR  
✅ انتخاب رنگ QR (Foreground/Border)  
✅ ذخیره خودکار تصویر QR در پوشه مخصوص (مثلاً `images`)  
✅ سرعت بالا و بسیار سبک  
✅ بدون نیاز به اینترنت  
✅ مناسب استفاده روی همه سیستم‌های ویندوز  
✅ دارای آیکون اختصاصی برنامه (`icon.ico`)  
✅ نسخه نصبی (Installer) حرفه‌ای ساخته شده با Inno Setup  

---

# 🏗 نحوه عملکرد سیستم

User ➜ GUI (Tkinter) ➜ QR Generator (qrcode) ➜ Output PNG

1. کاربر متن یا لینک را وارد می‌کند  
2. رنگ‌ها را انتخاب می‌کند  
3. دکمه ساخت را می‌زند  
4. ماژول qrcode یک QR Code تولید می‌کند  
5. فایل نهایی به صورت تصویر ذخیره می‌شود  

---

# 📦 ساختار فایل‌های پروژه
```bash
main.py               # رابط کاربری (Tkinter) و منطق اصلی برنامه
create_moudle.py      # ماژول ساخت QR Code با استفاده از کتابخانه qrcode
icon.ico              # آیکون رسمی و اختصاصی برنامه
