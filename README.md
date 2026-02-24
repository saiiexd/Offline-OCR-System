# Offline OCR System: Image-to-JSON Converter

A robust, privacy-focused Offline Optical Character Recognition (OCR) application built with Python. This tool allows users to extract text from images and documents without an internet connection, converting the results into a structured JSON format.

## Project Overview

The Offline OCR System is designed for high-security environments and users who require a secure way to digitize physical documents. By leveraging Tesseract OCR and OpenCV, it provides high-accuracy text extraction while ensuring data privacy by processing all information locally on the host machine.

### Key Features
- Privacy Focused: 100 percent offline processing. No data is transmitted to external servers.
- Advanced Preprocessing: Utilizes OpenCV for adaptive thresholding and noise reduction to improve character recognition accuracy.
- Multiple Format Support: Compatible with standard image formats including PNG, JPG, and JPEG.
- Structured Output: Generates JSON files containing extracted text and metadata for easy integration with other systems.
- Intuitive Interface: Streamlit-based web interface for efficient document management and preview.

## System Architecture and Logic

The application implements a modular pipeline to transform raw image data into structured text:

1.  Image Ingestion: The user provides a document image through the web interface.
2.  Image Preprocessing (OpenCV):
    *   Grayscale Conversion: Reduces complexity by removing color information.
    *   Noise Reduction: Uses Gaussian blurring to eliminate pixel-level artifacts.
    *   Adaptive Thresholding: Employs Otsu's method to differentiate text from the background based on local pixel intensity, creating a high-contrast binary image.
3.  Character Recognition (Tesseract OCR): The Tesseract engine analyzes the binary image, mapping pixel patterns to known character sets using pre-trained neural network models.
4.  Data Structuring: The extracted string is cleaned and mapped into a JSON object along with the source metadata.

## Technology Stack

- Frontend Framework: Streamlit
- OCR Engine: Tesseract OCR (v5.x recommended)
- Image Processing Libraries: OpenCV (cv2) and Pillow (PIL)
- Implementation Language: Python 3.10+

## Installation and Configuration

Follow these instructions to deploy the application on a local environment.

### 1. Prerequisites
- Python 3.10 or higher.
- Tesseract OCR Engine:
    - Windows: Download the installer from the official UB Mannheim repository.
    - Path Configuration: Ensure the installation path (typically C:\Program Files\Tesseract-OCR\tesseract.exe) is correctly referenced in the core/ocr_processor.py file.

### 2. Repository Setup
Clone the repository to your local machine:
```bash
git clone https://github.com/saiiexd/Offline-OCR-System.git
cd Offline-OCR-System
```

### 3. Environment Configuration
It is recommended to use a virtual environment to manage dependencies:
```bash
python -m venv venv
# Windows activation:
.\venv\Scripts\activate
# Unix/macOS activation:
source venv/bin/activate
```

### 4. Dependency Installation
Install the required Python packages:
```bash
pip install -r requirements.txt
```

## Application Execution

To launch the system, execute the following command from the project root:

```bash
streamlit run app.py
```

Upon execution, the interface will be accessible via the local host address, typically http://localhost:8501.

## Project Structure

```text
Offline-OCR-System/
├── app.py              # Main application entry point
├── core/               # Backend logic and processing
│   ├── ocr_processor.py # Tesseract engine interface
│   ├── preprocess.py    # OpenCV image manipulation
│   └── utils.py         # Utility functions
├── ui/                 # User interface components
│   └── web_ui.py       # Streamlit layout and logic
├── requirements.txt    # List of project dependencies
└── README.md           # System documentation
```

## Contributing
Project contributors should submit pull requests for review. Ensure that any modifications to the OCR core are accompanied by relevant test cases.

## License
This project is released under the MIT License.

---
Developed by saiiexd
