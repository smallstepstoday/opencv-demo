from annotated_types import T
import streamlit as st
import cv2
import numpy as np

st.title("Photographic Filters: Noise")
st.markdown("""
        The following filters are demonstrated below:
        - Sobel Edge Detection
        - Canny Edge Detection
        """)
st.header("Step 1: Upload an image")

img_file_buffer = st.file_uploader("Choose a file", type=['jpg', 'jpeg', 'png'])

if img_file_buffer is not None:
  # Create a select box to choose the filter.
  st.header("Step 2: Select an edge detection method")
  filter = st.selectbox("Select a method", ["Sobel", "Canny"])

  # Read the file and convert it to opencv Image.
  raw_bytes = np.asarray(bytearray(img_file_buffer.read()), dtype=np.uint8)
  # Loads image in a BGR channel order.
  image = cv2.imdecode(raw_bytes, cv2.IMREAD_COLOR)

  # Create placeholders to display input and output images.
  placeholders = st.columns(2)

  # Display Input image in the first placeholder.
  placeholders[0].image(image, channels='BGR')
  placeholders[0].text("Input Image")

  if filter == "Sobel":
      image_cp_sobel = image.copy()

      # Convert to grayscale.
      img_gray = cv2.cvtColor(image_cp_sobel, cv2.COLOR_BGR2GRAY)

      # Create a slider and get the kernel size from the slider.
      ksize = st.slider("SET Kernel size", min_value=1, max_value=7, step=2, value=3)
      horiz = st.checkbox("Horizontal", value=True)
      vert = st.checkbox("Vertical", value=True)

      img_sobel = cv2.Sobel(img_gray, ddepth=-1, dx=int(horiz), dy=int(vert), ksize=ksize)
      placeholders[1].image(img_sobel)


  elif filter == "Canny":
      image_cp_canny = image.copy()

      # Convert to grayscale.
      img_gray = cv2.cvtColor(image_cp_canny, cv2.COLOR_BGR2GRAY)

      # Create a slider and get the kernel size from the slider.
      t1 = st.slider("SET first threshold", min_value=0, max_value=255, step=1, value=180)
      t2 = st.slider("SET second threshold", min_value=0, max_value=255, step=1, value=200)
      aperture = st.slider("SET Sobel Aperture size", min_value=3, max_value=7, step=2, value=3)
      l2gradient = st.checkbox("L2 Gradient", value=False)

      img_canny = cv2.Canny(img_gray, threshold1=t1, threshold2=t2, apertureSize=aperture, L2gradient=l2gradient)
      placeholders[1].image(img_canny)