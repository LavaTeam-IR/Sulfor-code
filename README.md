<div align="center">

```
  ██████  ██    ██ ██      ███████  ██████  ██████  
 ██       ██    ██ ██      ██      ██    ██ ██   ██ 
  ███████  ██    ██ ██      █████   ██    ██ ██████  
       ██  ██    ██ ██      ██      ██    ██ ██   ██ 
  ██████   ██████  ███████ ██       ██████  ██   ██ 
```

**Sulfor Code** — دستیار هوش مصنوعی در ترمینال

![version](https://img.shields.io/badge/version-1.0.0-blueviolet)
![python](https://img.shields.io/badge/python-3.8+-cyan)
![license](https://img.shields.io/badge/license-MIT-green)
![by](https://img.shields.io/badge/by-%40lavateam__IR-orange)

</div>

---

## 🇮🇷 فارسی

### Sulfor Code چیه؟

یه دستیار هوش مصنوعی کاملاً رایگانه که مستقیم توی ترمینال اجرا می‌شه.  
بدون API Key، بدون اینترنت دائمی، بدون هزینه.  
مدل رو یه بار دانلود می‌کنه (~670MB) و بعدش برای همیشه آفلاین کار می‌کنه.

---

### پیش‌نیاز

- **Python 3.8** یا بالاتر
- اینترنت فقط برای بار اول (دانلود مدل)

---

### 🪟 نصب روی ویندوز

**۱. Python رو نصب کن**  
از [python.org](https://python.org/downloads) دانلود کن.  
⚠️ موقع نصب حتماً تیک **"Add Python to PATH"** رو بزن!

**۲. دستور نصب رو توی CMD یا PowerShell اجرا کن:**

```cmd
powershell -Command "Invoke-WebRequest -Uri 'https://lavateam-IR.github.io/sulfor-code/install.bat' -OutFile 'install.bat'" && install.bat
```

**۳. اجرا کن:**

```cmd
sulfor run
```

---

### 🍎 نصب روی macOS

**۱. Python رو نصب کن** (اگه نداری):

```bash
brew install python3
```

یا از [python.org](https://python.org/downloads) دانلود کن.

**۲. دستور نصب رو توی Terminal اجرا کن:**

```bash
curl -sSL https://lavateam-IR.github.io/sulfor-code/install.sh | bash
```

**۳. ترمینال رو ببند و دوباره باز کن، بعد اجرا کن:**

```bash
sulfor run
```

---

### 🐧 نصب روی Linux

**۱. Python رو نصب کن** (اگه نداری):

```bash
# Ubuntu / Debian
sudo apt install python3 python3-pip -y

# Fedora / RHEL
sudo dnf install python3 python3-pip -y

# Arch
sudo pacman -S python python-pip
```

**۲. دستور نصب رو اجرا کن:**

```bash
curl -sSL https://lavateam-IR.github.io/sulfor-code/install.sh | bash
```

**۳. اجرا کن:**

```bash
sulfor run
```

---

### نحوه استفاده

بعد از اجرا، صبر کن مدل لود بشه (بار اول کمی طول می‌کشه).  
بعدش مستقیم سوالت رو بنویس و Enter بزن.

```
sulfor> چطور یه list رو در Python sort کنم؟
sulfor> این باگ چیه؟ ...
sulfor> یه REST API با FastAPI بساز
```

برای خروج:

```
sulfor> bye/
```

---

### فایل‌های پروژه

| فایل | توضیح |
|------|-------|
| `sulfor.py` | کد اصلی برنامه |
| `setup.py` | فایل نصب pip |
| `install.bat` | نصب‌کننده ویندوز |
| `install.sh` | نصب‌کننده Mac / Linux |

---

### مشکلات رایج

**`sulfor` پیدا نشد بعد از نصب:**
```bash
# Mac / Linux
source ~/.bashrc   # یا source ~/.zshrc

# Windows
# ترمینال رو ببند و دوباره باز کن
```

**دانلود مدل قطع شد:**  
دوباره `sulfor run` بزن — دانلود از همون جایی که موند ادامه نمی‌ده، از اول شروع می‌کنه.  
اگه اینترنت ضعیفه، چند بار امتحان کن.

**روی ویندوز رنگ‌ها نمایش داده نمی‌شن:**  
از **Windows Terminal** یا **PowerShell** استفاده کن، نه CMD قدیمی.

---

<div align="center">
made with ❤️ by <b>@lavateam_IR</b>
</div>

---

## 🌐 English

### What is Sulfor Code?

A completely free AI coding assistant that runs directly in your terminal.  
No API key. No permanent internet. No cost.  
Downloads the model once (~670MB) and works fully offline forever after.

---

### Requirements

- **Python 3.8+**
- Internet only for the first run (model download)

---

### 🪟 Windows Installation

**1. Install Python**  
Download from [python.org](https://python.org/downloads).  
⚠️ During install, check **"Add Python to PATH"**!

**2. Run this in CMD or PowerShell:**

```cmd
powershell -Command "Invoke-WebRequest -Uri 'https://lavateam-IR.github.io/sulfor-code/install.bat' -OutFile 'install.bat'" && install.bat
```

**3. Run:**

```cmd
sulfor run
```

---

### 🍎 macOS Installation

**1. Install Python** (if needed):

```bash
brew install python3
```

**2. Run in Terminal:**

```bash
curl -sSL https://lavateam-IR.github.io/sulfor-code/install.sh | bash
```

**3. Restart terminal, then run:**

```bash
sulfor run
```

---

### 🐧 Linux Installation

**1. Install Python:**

```bash
# Ubuntu / Debian
sudo apt install python3 python3-pip -y

# Fedora
sudo dnf install python3 python3-pip -y

# Arch
sudo pacman -S python python-pip
```

**2. Run installer:**

```bash
curl -sSL https://lavateam-IR.github.io/sulfor-code/install.sh | bash
```

**3. Run:**

```bash
sulfor run
```

---

### Usage

After launch, wait for the model to load (first time takes longer).  
Then just type your question and press Enter.

```
sulfor> How do I reverse a string in Python?
sulfor> What's wrong with this code? ...
sulfor> Write a REST API with Express.js
```

To exit:

```
sulfor> bye/
```

---

### Troubleshooting

**`sulfor` command not found after install:**
```bash
# Mac / Linux
source ~/.bashrc    # or source ~/.zshrc

# Windows — close and reopen terminal
```

**Model download interrupted:**  
Run `sulfor run` again. It will restart the download from the beginning.

**Colors not showing on Windows:**  
Use **Windows Terminal** or **PowerShell** instead of the old CMD.

---

<div align="center">
made with ❤️ by <b>@lavateam_IR</b>
</div>
