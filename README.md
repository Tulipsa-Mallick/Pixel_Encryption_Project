# 🖼️ Pixel-Based Image Encryption Tool

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A simple Python tool that encrypts and decrypts images by shifting each pixel's RGB values using a numeric key.  
Built with the Pillow library for image processing and designed for easy command-line interaction.

---

## 💡 Features

- Encrypt or decrypt images by shifting RGB pixel values  
- Supports all common image formats supported by Pillow (PNG, JPEG, BMP, etc.)  
- CLI menu interface for easy operation  
- Handles input validation and errors gracefully  
- Creates output directories automatically if needed

---

## 🚀 Getting Started

### 📦 Prerequisites

- Python 3.8 or higher

### 🛠️ Install Pillow

Install Pillow via pip:

```bash
pip install pillow
````

If you use Python 3 and pip3 is your command:

```bash
pip3 install pillow
```

## ▶️ Running the Tool

```bash
python main.py
```

Follow the on-screen menu:

1. Encrypt an Image
2. Decrypt an Image
3. Encrypt & Decrypt an Image
4. Exit

You'll be prompted to enter image file paths and an integer key for encryption/decryption.

---

## 📸 Supported Image Formats

This tool supports all image formats supported by Pillow, including but not limited to:

* PNG
* JPEG / JPG
* BMP
* GIF (single frame)
* TIFF
* Any picture can be used for reference just use the image entitled under original.png
---

## 🧪 Example Usage

* Encrypt `input.jpg` to `encrypted.png` with key `10`
* Decrypt `encrypted.png` back to `decrypted.png` with the same key `10`

---

## 🧠 How It Works

The tool shifts each pixel's red, green, and blue (RGB) color values by a key value modulo 256.
Encryption adds the key; decryption subtracts it — effectively reversing the process.

For example, if a pixel has RGB (100, 150, 200) and key is 10:

* Encrypted pixel: (110, 160, 210)
* Decrypted pixel: (100, 150, 200)

---

## 📚 References

* [Pillow (PIL Fork) Documentation](https://pillow.readthedocs.io/en/stable/)
* [Python Imaging Library](https://en.wikipedia.org/wiki/Python_Imaging_Library)

---

## 📜 License

This project is licensed under the MIT License.
