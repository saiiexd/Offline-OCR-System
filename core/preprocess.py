import cv2
import numpy as np


def load_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Unable to load image")
    return image


def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def remove_noise(gray_image):
    return cv2.GaussianBlur(gray_image, (5, 5), 0)


def apply_threshold(gray_image):
    return cv2.adaptiveThreshold(
        gray_image,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )


def preprocess_image(image_path):
    image = load_image(image_path)
    gray = convert_to_grayscale(image)
    noise_removed = remove_noise(gray)
    thresholded = apply_threshold(noise_removed)
    return thresholded
