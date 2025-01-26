import streamlit as st
import cv2
import numpy as np

st.title("Photographic Filters: Noise")
st.markdown("""
        The following filters are demonstrated below:
        - Median Filtering
        - Bilateral Filtering
        """)
st.header("Step 1: Upload an image")

img_file_buffer = st.file_uploader("Choose a file", type=['jpg', 'jpeg', 'png'])

if img_file_buffer is not None:
  # Create a select box to choose the filter.
  st.header("Step 2: Select a filter")
  filter = st.selectbox("Select a filter", ["Median Filtering", "Bilateral Filtering"])

  # Read the file and convert it to opencv Image.
  raw_bytes = np.asarray(bytearray(img_file_buffer.read()), dtype=np.uint8)
  # Loads image in a BGR channel order.
  image = cv2.imdecode(raw_bytes, cv2.IMREAD_COLOR)

  # Create placeholders to display input and output images.
  placeholders = st.columns(2)

  # Display Input image in the first placeholder.
  placeholders[0].image(image, channels='BGR')
  placeholders[0].text("Input Image")

  if filter == "Median Filtering":
      image_cp_median = image.copy()

      # Create a slider and get the kernel size from the slider.
      ksize = st.slider("SET Kernel size", min_value=3, max_value=30, step=2, value=9)

      median_blur = cv2.medianBlur(image_cp_median, ksize)
      placeholders[1].image(median_blur, channels='BGR')
      placeholders[1].text(f"Median Blur {ksize}x{ksize} kernel")


  elif filter == "Bilateral Filtering":
      image_cp_bilateral = image.copy()

      # Create a slider and get the kernel size from the slider.
      ksize = st.slider("SET Neighborhood size", min_value=5, max_value=30, step=2, value=9)
      sigmaColor = st.slider("SET Sigma Color", min_value=1, max_value=200, step=1, value=75)
      sigmaSpace = st.slider("SET Sigma Space", min_value=1, max_value=200, step=1, value=75)

      bilateral_blur = cv2.bilateralFilter(image_cp_bilateral, ksize, sigmaColor, sigmaSpace)
      placeholders[1].image(bilateral_blur, channels='BGR')