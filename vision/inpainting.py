import streamlit as st
import cv2
import numpy as np
from streamlit_drawable_canvas import st_canvas
import io
import base64
from PIL import Image

# Function to create a download link for output image
def get_image_download_link(img, filename, text):
    """Generates a link to download a particular image file."""
    buffered = io.BytesIO()
    img.save(buffered, format='JPEG')
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/txt;base64,{img_str}" download="{filename}">{text}</a>'
    return href



st.title("Image Inpainting")
st.header("Step 1: Upload an image")

"""
Inpainting is the process of reconstructing lost or deteriorated parts of images and videos. It is an advanced form of 
interpolation that can be used to remove scratches, small blotches, and other unwanted objects from images. In this demo, 
we will inpaint an image using OpenCV.
"""

"Select an image that has scratches or small blotches that you want to remove."

img_file_buffer = st.file_uploader("Choose a file", type=['jpg', 'jpeg', 'png'])
img = None
res = None

if img_file_buffer is not None:
    st.header("Step 2: Draw on the image to inpaint")
    
    # Read the file and convert it to opencv Image.
    raw_bytes = np.asarray(bytearray(img_file_buffer.read()), dtype=np.uint8)
    # Loads image in a BGR channel order.
    image = cv2.imdecode(raw_bytes, cv2.IMREAD_COLOR)

    # Create placeholders to display input and output images.
    img_col1, img_col2 = st.columns(2)

    place1 = img_col1.empty()
    place2 = img_col2.empty()

    stroke_width = st.slider("Stroke width: ", 1, 25, 5)
    h, w = image.shape[:2]
    if w > 800:
        h_, w_ = int(h * 800 / w), 800
    else:
        h_, w_ = h, w

    show_mask = st.checkbox("Show mask", value=False)

    img_col1, img_col2 = st.columns(2)

    with img_col1:
        # Create a canvas component.
        canvas_result = st_canvas(
            fill_color='white',
            stroke_width=stroke_width,
            stroke_color='black',
            background_image=Image.open(img_file_buffer).resize((h_, w_)),
            update_streamlit=True,
            height=h_,
            width=w_,
            drawing_mode='freedraw',
            key="canvas",
        )
        stroke = canvas_result.image_data
    with img_col2:
        if stroke is not None:
            if show_mask:
                st.image(stroke)

            mask = cv2.split(stroke)[3]
            mask = np.uint8(mask)
            mask = cv2.resize(mask, (w, h))

    st.header("Step 3: Select the mode for inpainting")
    option = st.selectbox("Mode", ["None", "Telea", "Navier-Stokes", "Compare Both"])
    
    if option == 'Telea':
        st.subheader('Result of Telea')
        res = cv2.inpaint(src=image, inpaintMask=mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)[:,:,::-1]
        st.image(res)
    elif option == 'Navier-Stokes':
        st.subheader('Result of Navier-Stokes')
        res = cv2.inpaint(src=image, inpaintMask=mask, inpaintRadius=3, flags=cv2.INPAINT_NS)[:,:,::-1]
        st.image(res)
    elif option == 'Compare Both':
        col1, col2 = st.columns(2)
        res1 = cv2.inpaint(src=image, inpaintMask=mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)[:,:,::-1]
        res2 = cv2.inpaint(src=image, inpaintMask=mask, inpaintRadius=3, flags=cv2.INPAINT_NS)[:,:,::-1]

        with col1:
            st.subheader('Result of Telea')
            st.image(res1)
            if res1 is not None:
                # Display link.
                result1 = Image.fromarray(res1)
                st.markdown(get_image_download_link(result1, 'output-telea.jpg', 'Download Output of Telea'), unsafe_allow_html=True)

        with col2:
            st.subheader('Result of Navier-Stokes')
            st.image(res2)
            if res2 is not None:
                # Display link.
                result2 = Image.fromarray(res2)
                st.markdown(get_image_download_link(result2, 'output-navier-stokes.jpg', 'Download Output of Navier-Stokes'), unsafe_allow_html=True)
    else:
        pass

    if res is not None:
        # Display link.
        result = Image.fromarray(res)
        st.markdown(get_image_download_link(result, 'output.jpg', 'Download Output'), unsafe_allow_html=True)