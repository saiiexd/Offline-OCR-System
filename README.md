# 📄 Offline OCR System: Image-to-JSON Converter

A robust, privacy-focused **Offline OCR (Optical Character Recognition)** application built with Python. This tool allows users to extract text from images and documents without an internet connection, converting the results into a structured JSON format.

---

## 🎯 Project Overview

The **Offline OCR System** is designed for users who need a quick and secure way to digitize physical documents. By leveraging the power of **Tesseract OCR** and **OpenCV**, it provides high-accuracy text extraction while ensuring data privacy by processing everything locally on your machine.

### ✨ Key Features
- **Privacy First:** 100% offline processing. No data ever leaves your device.
- **Smart Preprocessing:** Automatically enhances image quality (Grayscale, Noise Reduction, Thresholding) for better accuracy.
- **Multi-Format Support:** Works with `.png`, `.jpg`, and `.jpeg`.
- **Structured Output:** Download extracted text instantly as a `.json` file.
- **Modern UI:** Built with **Streamlit** for a clean, intuitive user experience.

---

## 🧠 The Logic Behind the System

The application follows a modular pipeline to ensure maximum accuracy:

1.  **Image Upload:** The user selects an image via the Streamlit interface.
2.  **Image Processing (OpenCV):**
    *   **Grayscale Conversion:** Simplifies the image for the OCR engine.
    *   **Adaptive Thresholding (Otsu's Method):** Converts the image to binary (black and white) to highlight text characters against the background.
3.  **OCR Extraction (Tesseract):** The processed binary image is sent to the Tesseract engine, which identifies characters and words based on pre-trained language models.
4.  **JSON Formatting:** The extracted text is bundled with metadata (like filename) and presented as a structured JSON object.

---

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/) (Web UI)
- **OCR Engine:** [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- **Image Processing:** [OpenCV](https://opencv.org/) & [Pillow](https://python-pillow.org/)
- **Programming Language:** Python 3.x

---

## 🚀 Getting Started

Follow these steps to set up the project on your local machine.

### 1. Prerequisites
- **Python:** [Download and install Python](https://www.python.org/downloads/) (v3.10+ recommended).
- **Tesseract OCR:** 
    - Download the installer from [UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki) (for Windows).
    - Install it to the default path: `C:\Program Files\Tesseract-OCR\tesseract.exe`.

### 2. Download/Clone the Project
```bash
git clone https://github.com/saiiexd/Offline-OCR-System.git
cd Offline-OCR-System
```

### 3. Setup Virtual Environment (Recommended)
```bash
python -m venv venv
# Activate on Windows:
.\venv\Scripts\activate
# Activate on Mac/Linux:
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🖥️ How to Run

Once the requirements are installed, launch the application using Streamlit:

```bash
streamlit run app.py
```

After running the command, your browser will open the application at `http://localhost:8501`.

---

## 📁 File Structure
```text
Offline-OCR-System/
├── app.py              # Main entry point
├── core/               # OCR & Processing Logic
│   ├── ocr_processor.py # Tesseract interface
│   ├── utils.py        # Image preprocessing helper
│   └── ...
├── ui/                 # UI components
│   └── web_ui.py       # Streamlit layout
├── requirements.txt    # Library dependencies
└── README.md           # Documentation
```

---

## 🤝 Contributing
Contributions are welcome! If you have suggestions for improvement, please fork the repo and create a pull request.

## 📄 License
This project is licensed under the MIT License.

---
*Developed by [saiiexd](https://github.com/saiiexd)*
