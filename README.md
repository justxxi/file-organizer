# 📂 File Organizer

**A smart and efficient file sorting script that organizes files into categorized folders based on their extensions.** 

## 🚀 Features
- ✅ **Automatically organizes files** into categories like `Documents`, `Images`, `Videos`, etc.
- ✅ **Safe and efficient file handling** with error logging.
- ✅ **Cross-platform support** (Windows, macOS, Linux).
- ✅ **User-friendly CLI** with `argparse`.
- ✅ **Customizable file categories** via a dictionary.

---

## 📌 Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/justxxi/file-organizer.git
cd file-organizer
```

### 2️⃣ Install Dependencies *(if needed)*
This script runs with Python 3 and does not require additional dependencies.
However, ensure you have Python installed:
```bash
python --version
```

---

## 🛠 Usage
Run the script with the target directory:
```bash
python organizer.py /path/to/directory
```

Example:
```bash
python organizer.py ~/Downloads
```

---

## 📂 How It Works
### 🏗 Before Sorting:
```
/Downloads
  - report.pdf
  - photo.jpg
  - song.mp3
  - script.py
```

### ✅ After Sorting:
```
/Downloads
  /Documents/report.pdf
  /Images/photo.jpg
  /Music/song.mp3
  /Code/script.py
```

---

## ⚙ Customization
You can modify the file categories inside `organizer.py` by editing the `FILE_CATEGORIES` dictionary.

Example:
```python
FILE_CATEGORIES = {
    "Images": {".jpg", ".png", ".gif"},
    "Documents": {".pdf", ".docx", ".txt"},
    "Videos": {".mp4", ".avi"},
}
```

---

## 📜 License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🌟 Show Your Support!
If you find this project helpful, please ⭐ star the repository! 😊
