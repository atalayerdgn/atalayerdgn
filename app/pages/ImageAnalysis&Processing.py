import streamlit as st
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt




class Image:
    def __init__(self):
        self.image = None
        self.image_path = None
        self.image_array = None
    def set_background() -> None:
        st.set_page_config(
        page_title="Image Analysis & Processing",
        page_icon=":computer:",
        layout="wide",
        initial_sidebar_state="expanded"
        )
        st.markdown(
            """
            <style>
            body {
                background-image: url("https://www.transparenttextures.com/patterns/sakura.png");
                background-size: cover;
                color: #333;
                font-family: Arial, sans-serif;
            }
            .stTextInput > div > div > input {
                background-color: #f0f0f0;
                color: #333;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #ccc;
            }
            .stButton > button {
                background-color: #4CAF50;
                color: white;
                padding: 12px 24px;
                text-align: center;
                display: inline-block;
                font-size: 18px;
                margin: 6px 3px;
                cursor: pointer;
                border-radius: 8px;
                border: none;
                transition: all 0.3s ease;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            .stButton > button:hover {
                background-color: #45a049;
            }
            .data-container {
                display: flex;
                justify-content: space-between;
            }
            .data-section {
                background-color: #ffffff;
                border-radius: 5px;
                padding: 15px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px;
                flex: 1;
                margin-right: 10px;
            }
            .data-section:last-child {
                margin-right: 0;
            }
            .data-section h3 {
                color: #4CAF50;
                font-size: 18px;
                margin-bottom: 10px;
                border-bottom: 1px solid #ccc;
                padding-bottom: 5px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    def load_image(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)
        self.image_array = np.array(self.image)
    def show_image(self):
        st.image(self.image)
    def run(self):
        st.title("Image Analysis & Processing")
        st.markdown("---")
        with st.form("image_analysis"):
            st.markdown("### Upload an image")
            uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
            st.markdown("---")
            submit_button = st.form_submit_button(label='Analyze Image')
            if submit_button and uploaded_file is not None:
                self.load_image(uploaded_file)
                self.show_image()
                st.markdown("---")
                st.markdown("### Image Information")
                st.markdown(f"**Image Path:** {self.image_path}")
                st.markdown(f"**Image Shape:** {self.image_array.shape}")
                st.markdown("---")
                st.markdown("### Image Analysis")
                st.markdown("#### Image Histogram")
                self.show_histogram()
                st.markdown("#### Image Channels")
                self.show_channels()
                st.markdown("#### Image Grayscale")
                self.show_grayscale()
                st.markdown("#### Image Thresholding")
                self.show_thresholding()
                st.markdown("#### Image Blurring")
                self.show_blurring()
                st.markdown("#### Image Edge Detection")
                self.show_edge_detection()