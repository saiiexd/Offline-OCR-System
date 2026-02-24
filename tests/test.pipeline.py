from core.ocr_engine import extract_text
from core.json_formatter import text_to_json

image_path = "assets/sample_images/test.jpg"

text = extract_text(image_path)
json_data = text_to_json(text)

print(json_data)
