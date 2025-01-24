from scipy.datasets import face
import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
import base64

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

