<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Web%20App-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
</p>

<p align="center">
  <a href="https://github.com/AbolfazlNbDeV/python-shortlink/stargazers">
    <img src="https://img.shields.io/github/stars/AbolfazlNbDeV/python-shortlink?style=for-the-badge&logo=github&logoColor=white" alt="Stars">
  </a>
  <a href="https://github.com/AbolfazlNbDeV/python-shortlink/network/members">
    <img src="https://img.shields.io/github/forks/AbolfazlNbDeV/python-shortlink?style=for-the-badge&logo=github&logoColor=white" alt="Forks">
  </a>
  <a href="https://github.com/AbolfazlNbDeV/python-shortlink/issues">
    <img src="https://img.shields.io/github/issues/AbolfazlNbDeV/python-shortlink?style=for-the-badge&logo=github&logoColor=white" alt="Issues">
  </a>
</p>

<h1 align="center">Python ShortLink</h1>
<p align="center">A clean, fast, and lightweight URL shortener built with Flask and SQLite.</p>

---

<p align="center">
  <b>یک کوتاه‌کننده لینک سبک، سریع و قابل توسعه با Flask و SQLite</b>
</p>

## 📌 معرفی پروژه

این پروژه یک **URL Shortener** حرفه‌ای و سبک است که با **Python / Flask** ساخته شده و از **SQLite** برای ذخیره‌سازی داده‌ها استفاده می‌کند.  
هدف پروژه، ایجاد یک ابزار ساده و سریع برای کوتاه‌سازی لینک‌ها، مدیریت URLها و ارائه‌ی تجربه‌ای تمیز و قابل‌اعتماد است.

---

## 🚀 دسترسی سریع

- [ویژگی‌های کلیدی](#-ویژگی‌های-کلیدی)
- [معماری و جریان داده](#-معماری-و-جریان-داده)
- [نصب و راه‌اندازی](#-نصب-و-راه‌اندازی)
- [تنظیمات امنیتی](#-تنظیمات-امنیتی)
- [مستندات API](#-مستندات-api)
- [استقرار در محیط Production](#-استقرار-در-محیط-production)
- [ساختار فایل‌ها](#-ساختار-فایل‌ها)

---

## ✨ ویژگی‌های کلیدی

- 🔴 کوتاه‌سازی سریع لینک‌ها
- 🔴 مدیریت و ذخیره‌سازی لینک‌ها با SQLite
- 🔴 رابط ساده و سبک
- 🔴 ساختار مناسب برای توسعه و سفارشی‌سازی
- 🔴 مناسب برای اجرا در محیط توسعه و production

---

## 🧠 معماری و جریان داده
```text
+------------------+
|   User / Client  |
+--------+---------+
|
v
+------------------+
|   Flask Routes   |
|  (Request Layer) |
+--------+---------+
|
v
+------------------+
|   App Logic      |
| Validation / Map |
+--------+---------+
|
v
+------------------+
|   SQLite DB      |
|  URL Storage     |
+------------------+

Flow:
User -> Flask Route -> Validation -> Database -> Short Link Response
