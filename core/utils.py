import cv2
import numpy as np
from PIL import Image

def preprocess_image(image: Image.Image) -> np.ndarray:
    """
    Convert a PIL Image to a grayscale numpy array for OCR processing.
    """
    # Convert PIL Image to numpy array
    img_array = np.array(image)
    
    # Convert RGB to BGR (OpenCV format) if valid
    if len(img_array.shape) == 3:
        img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
        
        # Convert to grayscale
        gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
    else:
        # Already grayscale?
        gray = img_array

    # Apply simple thresholding to improve contrast
    # Verify if it's really needed, but for now specific "offline" documents usually benefit
    # Using Otsu's binarization
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    return thresh
