<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:f00000,50:8b0000,100:4b0000&height=200&section=header&text=QR%20CODE%20CREATOR&fontSize=40&fontColor=ffffff&animation=fadeIn&fontAlignY=35"/>
</p>

<h3 align="center">
Fast, Lightweight and Professional QR Code Generator built with Python & Tkinter
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

# 🧠 Project Introduction

**QR Code Creator** is a fast, lightweight, and user‑friendly desktop application for generating QR Codes from any text or link.

With a simple and clean graphical interface, this program allows you to:

- Enter any text or URL
- Choose the background color of the QR Code
- Customize the main QR color (foreground)
- Export and save the QR Code as a high‑quality image

The main goal of this project is to create a **simple yet professional tool for generating QR Codes on Windows systems.**

---

# 📥 Download the Application (From Releases Only)

To download the latest version of the application (EXE or Setup file):

👉 **Please download it from the GitHub Releases section**

➡️ **[Download From Releases](../../releases)**

> ⚠️ Note  
> - EXE / Setup files are **not included in the source code**.  
> - They are only published in the **Releases** section.

---

# ✨ Features

✅ Generate QR Codes from text or URLs  
✅ Custom QR background color  
✅ Custom QR foreground color  
✅ Save QR Code as an image automatically  
✅ High speed and lightweight application  
✅ No internet connection required  
✅ Compatible with all Windows systems  
✅ Custom application icon (`icon.ico`)  
✅ Professional installer built using **Inno Setup**

---

# ⚙️ How the System Works

User ➜ GUI (Tkinter) ➜ QR Generator (qrcode) ➜ Output PNG

1. The user enters a text or URL  
2. Selects preferred colors  
3. Clicks the **Generate** button  
4. The **qrcode module** generates the QR Code  
5. The final image is saved as a PNG file  

---

# 📦 Project File Structure

project/
│
├── main.py            # GUI (Tkinter) and main program logic
├── create_module.py   # QR Code generator module using the qrcode library
├── icon.ico           # Application icon
└── images/            # Saved QR Code images
