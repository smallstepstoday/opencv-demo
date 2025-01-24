import streamlit as st
import cv2
import numpy as np

st.title("Photographic Filters: Blur")
st.markdown("""
        The following filters are demonstrated below:
        - Box Blur
        - Gaussian Blur
        """)
st.header("Step 1: Upload an image")

img_file_buffer = st.file_uploader("Choose a file", type=['jpg', 'jpeg', 'png'])


if img_file_buffer is not None:
    # Create a select box to choose the filter.
    st.header("Step 2: Select a filter")
    filter = st.selectbox("Select a filter", ["Box Blur", "Gaussian Blur"])

    # Read the file and convert it to opencv Image.
    raw_bytes = np.asarray(bytearray(img_file_buffer.read()), dtype=np.uint8)
    # Loads image in a BGR channel order.
    image = cv2.imdecode(raw_bytes, cv2.IMREAD_COLOR)

    # Create placeholders to display input and output images.
    placeholders = st.columns(2)

    # Display Input image in the first placeholder.
    placeholders[0].image(image, channels='BGR')
    placeholders[0].text("Input Image")

    if filter == "Box Blur":
        image_cp_box = image.copy()

        # Create a slider and get the kernel size from the slider.
        ksize = st.slider("SET Kernel size", min_value=5, max_value=15, step=2, value=11)
        kernel = (ksize, ksize)

        box_blur = cv2.blur(image_cp_box, kernel)
        placeholders[1].image(box_blur, channels='BGR')
        placeholders[1].text(f"Blur {ksize}x{ksize} kernel")


    elif filter == "Gaussian Blur":
        image_cp_gauss = image.copy()

        # Create a slider and get the kernel size from the slider.
        ksize = st.slider("SET Kernel size", min_value=5, max_value=15, step=2, value=11)
        kernel = (ksize, ksize)

        gaussian_blur = cv2.GaussianBlur(image_cp_gauss, kernel, 0, 0)
        placeholders[1].image(gaussian_blur, channels='BGR')
        placeholders[1].text(f"Blur {ksize}x{ksize} kernel")
