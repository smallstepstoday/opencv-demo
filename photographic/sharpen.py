import streamlit as st
import cv2
import numpy as np

st.title("Photographic Filters: Sharpen")
st.markdown("""
        The following filters are demonstrated below:
        - Sharpen
        - Recover Sharpness
        """)
st.header("Step 1: Upload an image")
img_file_buffer = st.file_uploader("Choose a file", type=['jpg', 'jpeg', 'png'])


if img_file_buffer is not None:
    # Create a select box to choose the filter.
    st.header("Step 2: Select a filter")
    filter = st.selectbox("Select a filter", ["Sharpen", "Recover Sharpness"])

    # Read the file and convert it to opencv Image.
    raw_bytes = np.asarray(bytearray(img_file_buffer.read()), dtype=np.uint8)
    # Loads image in a BGR channel order.
    image = cv2.imdecode(raw_bytes, cv2.IMREAD_COLOR)

    # Create placeholders to display input and output images.
    placeholders = st.columns(2)

    # Display Input image in the first placeholder.
    placeholders[0].image(image, channels='BGR')
    placeholders[0].text("Input Image")

    if filter == "Sharpen":
        image_cp_sharp = image.copy()
        
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        sharpened = cv2.filter2D(image, ddepth=-1, kernel=kernel)
        placeholders[1].image(sharpened, channels='BGR')
        placeholders[1].text("Sharpened Image")

    elif filter == "Recover Sharpness":
        gaussian_blur = cv2.GaussianBlur(image, (11, 11), 0, 0)
        sharpened = cv2.addWeighted(image, 1.5, gaussian_blur, -0.5, 0)
        placeholders[1].image(sharpened, channels='BGR')
        placeholders[1].text("Sharpened Image")

        st.html("<small>The input image is blurred using Gaussian Blur and then sharpened using AddWeighted function.</small>")
