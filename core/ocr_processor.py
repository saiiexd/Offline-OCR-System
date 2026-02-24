import pytesseract
from PIL import Image
import numpy as np
import os
from .utils import preprocess_image

def extract_text(image: Image.Image) -> str:
    """
    Extract text from a PIL Image using Tesseract OCR.
    """
    # Configure Tesseract Path if not in PATH
    tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    if not os.path.exists(tesseract_cmd):
        tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    
    # Check if tesseract is in PATH (shutil.which) or at common locations
    import shutil
    if shutil.which("tesseract"):
        pass # It's in PATH
    elif os.path.exists(tesseract_cmd):
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
    
    # Preprocess image
    processed_img = preprocess_image(image)
    
    # Extract text
    text = pytesseract.image_to_string(processed_img)
    
    return text.strip()

def extract_text_to_data(image: Image.Image) -> dict:
    """
    Extract text and return full data dict (if needed later for optimization).
    For now, just wrapping the text extract.
    """
    text = extract_text(image)
    return {"text": text}
