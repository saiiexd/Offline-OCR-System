import streamlit as st
from PIL import Image
import json
import io
from core.ocr_processor import extract_text

def launch_app():
    st.set_page_config(page_title="Offline OCR to JSON", page_icon="📄")
    
    st.title("📄 Offline OCR to JSON Converter")
    st.markdown("Upload an image to extract text and download as JSON.")

    # Custom CSS for "App-like" feel (Offline focus)
    st.markdown("""
        <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
        </style>
    """, unsafe_allow_html=True)


    # Sidebar for instructions or settings
    with st.sidebar:
        st.header("Instructions")
        st.markdown("1. Upload an image (PNG, JPG, JPEG).")
        st.markdown("2. View the extracted text.")
        st.markdown("3. Download the result as a JSON file.")
        st.info("Ensure the image is clear for best results.")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        try:
            # Display uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", width="stretch")  # Updated from use_container_width=True
            
            with st.spinner("Extracting text..."):
                # Extract text
                extracted_text = extract_text(image)

            # Layout with tabs for Text and JSON
            tab1, tab2 = st.tabs(["📝 Extracted Text", "📋 JSON Preview"])
            
            with tab1:
                if extracted_text.strip():
                    st.text_area("Text Content", value=extracted_text, height=300)
                else:
                    st.warning("No text extracted! The image might be too blurry or contain no text. Please try another image.")

            # Prepare JSON
            json_data = {
                "filename": uploaded_file.name,
                "text": extracted_text.strip() # Ensure stripped text
            }
            json_string = json.dumps(json_data, indent=4)

            with tab2:
                st.json(json_data)

            # Download button (Only if text was found, or allow anyway but warn?)
            # Allowing anyway is better for debugging, but let's highlight it
            col1, col2 = st.columns([1, 2])
            with col1:
                st.download_button(
                    label="Download JSON",
                    data=json_string,
                    file_name=f"{uploaded_file.name.split('.')[0]}_ocr.json",
                    mime="application/json",
                    type="primary"
                )

        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.error("Please ensure Tesseract-OCR is installed and configured correctly on your system.")

if __name__ == "__main__":
    launch_app()
