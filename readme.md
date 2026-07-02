# HEIC to JPEG Converter

A lightweight, automated Python CLI tool that seamlessly converts HEIC (`.heic`) images into high-quality JPEG (`.jpg`) format. It includes built-in virtual environment (`venv`) automation, dependency auto-verification, and precise conversion controls.

## 🚀 Features

- **Automated Virtual Environment Execution:** Designed via shebang configurations to execute automatically inside its dedicated `venv` without manual activation steps.
- **Robust Dependency Verification:** Pre-checks system environment for `Pillow` and `pillow-heif`, displaying clean active version diagnostics or helpful setup guides instead of messy tracebacks.
- **Flexible Quality Controls:** Fine-tune image optimization using explicit CLI quality attributes.
- **Zero Configuration Overhead:** Run directly from any path once permissions are granted.

---

## 📋 Requirements & Dependencies

The script relies on the following Python packages:
- **Pillow** (PIL) - Core image processing engine
- **pillow-heif** - HEIF/HEIC standard extension plugin

*Note: The script dynamically detects missing dependencies and provides copy-paste ready installation flags if your environment is unconfigured.*

---

## 🔧 Installation & Environment Setup

Follow these quick steps to isolate your environment and configure the script to run seamlessly:

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/heic-to-jpeg-converter.git](https://github.com/your-username/heic-to-jpeg-converter.git)
cd heic-to-jpeg-converter

mkdir -p ~/tools/heic
python3 -m venv ~/tools/heic

~/tools/heic/bin/pip install pillow pillow-heif
chmod +x heic_to_jpg.py
```

### Usage
```bash
./heic_to_jpg.py input_image.heic
./heic_to_jpg.py photo.heic -o archives/photo_compressed.jpg -q 85
./heic_to_jpg.py --help
