import streamlit as st
from PIL import Image
from module import tools

icon = Image.open("assets/icon.png")

st.set_page_config(page_title="Image_compressor", page_icon=icon, layout="wide")

st.image("assets/111backup-compression.jpg", width=500)
st.header("Compresor de imagenes")
st.subheader("Adjuntar imagen")

upload_image = st.file_uploader("Elegi una imagen...", type=[".jpg", ".jpeg", ".png"])

if upload_image is not None:

    compress_button = st.button(label="Comprimir")

    if compress_button:
        compressed_image = tools.compress_image(upload_image)

        compressed_image.save("download_images/compressed_image.png")

        with open("download_images/compressed_image.png", "rb") as file:
            image_data = file.read()
        st.download_button("Descargar imagen comprimida", data=image_data, file_name="compressed_image.jpg")