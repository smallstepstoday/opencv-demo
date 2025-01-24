from scipy.datasets import face
import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(
    page_title="Cataluma OpenCV Demo App",
    page_icon=":camera:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# AI Operations
face_detection = st.Page("face-detection/face-detection.py", title="Face Detection")

# Photographic Filters
blur = st.Page("photographic/blur.py", title="Blur")
sharp = st.Page("photographic/sharpen.py", title="Sharpen")

pg = st.navigation({
    "AI Operations": [face_detection],
    "Photographic Filters": [blur, sharp]
})
pg.run()

