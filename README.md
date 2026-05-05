cat > README.md << 'EOF'
<h1 align="center">🚀✨ Python ShortLink ✨🚀</h1>

<p align="center">
  <b>A Modern, Fast & Elegant URL Shortener</b><br>
  Built with Python • Flask • HTML • JavaScript
</p>

<p align="center">
  <a href="https://github.com/AbolfazlNbDev">
    <img src="https://img.shields.io/badge/GitHub-AbolfazlNbDev-black?style=for-the-badge&logo=github">
  </a>
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Flask-Backend-green?style=for-the-badge&logo=flask">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge">
</p>

---

## 🌟 Overview

**Python ShortLink** is a lightweight and powerful URL shortener built using:

• 🐍 Python  
• 🔥 Flask  
• 🌐 HTML  
• ⚡ JavaScript  
• 🔐 Simple CAPTCHA system  

It converts long URLs into short, shareable links instantly.

---

## ✨ Features

✅ Instant short link generation  
✅ Clean and minimal Flask backend  
✅ Beautiful HTML frontend  
✅ JavaScript interaction  
✅ Simple CAPTCHA protection  
✅ Easy to modify and extend  
✅ Lightweight & fast  

---

## 📂 Project Structure

python-shortlink/

app.py  
captcha.py  
templates/  
static/  
README.md  

---

## 🛠 Installation

Install Flask:

pip install flask

---

## ▶️ Run The Application

python app.py

---

## 🌍 Open In Browser

http://127.0.0.1:5000

---

## ⚙️ How It Works

1️⃣ User enters a long URL  
2️⃣ Flask generates a short unique code  
3️⃣ The short link redirects to the original URL  
4️⃣ CAPTCHA protects against bots  

---

## 🧩 API Example

Create short URL:

curl -X POST -d "url=https://google.com" http://127.0.0.1:5000/create

Example redirect:

http://127.0.0.1:5000/abc123

---

## 🚀 Future Improvements

• Add database storage  
• Add click analytics  
• Add user accounts  
• Add QR code generator  
• Improve CAPTCHA system  

---

## 🤝 Contributing

Pull requests are welcome.  
Feel free to fork and improve the project ⭐

---

## ⭐ Support

If you like this project, please give it a Star ⭐  

GitHub Repository:  
https://github.com/AbolfazlNbDev/python-shortlink  

---

<p align="center"><b>✨ Made with Python & Flask by AbolfazlNbDev ✨</b></p>
EOF
