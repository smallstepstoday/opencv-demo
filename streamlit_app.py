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

# Computer Vision
face_detection = st.Page("vision/face-detection.py", title="Face Detection")
edge = st.Page("vision/edge.py", title="Edge Detection")
inpaint = st.Page("vision/inpainting.py", title="Image Inpainting")
classify = st.Page("vision/classify.py", title="Image Classification")

# Photographic Filters
blur = st.Page("photographic/blur.py", title="Blur")
sharp = st.Page("photographic/sharpen.py", title="Sharpen")
noise = st.Page("photographic/noise.py", title="Noise")

pg = st.navigation({
    "Computer Vision": [classify, face_detection, edge, inpaint],
    "Transformations": [],
    "Photographic Filters": [blur, sharp, noise]
})
pg.run()

