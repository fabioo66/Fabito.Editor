import streamlit as st
from PIL import Image
from module import tools

icon = Image.open("assets/icon.png")

st.set_page_config(page_title="Background_remover", page_icon=icon, layout="wide")

st.image("assets/social-remove-background.png", width=800)
st.header("Eliminar fondo de las imagenes y convertirlas en png")
st.subheader("Adjuntar imagen")

upload_image = st.file_uploader("Elegi una imagen...", type=[".jpg", ".jpeg", ".png"])

if upload_image is not None:
    st.image(upload_image, caption="Imagen subida", use_column_width=True)

    remove_button = st.button(label="Quitar fondo")

    if remove_button:
        st.success("Aguarde un momento, este proceso puede tardar un par de segundos")
        processed_image = tools.process_image(upload_image)
        
        st.image(processed_image, caption="Fondo eliminado", use_column_width=True)

        processed_image.save("download_images/processed_image.png")

        with open("download_images/processed_image.png", "rb") as file:
            image_data = file.read()
        st.download_button("Descargar imagen procesada", data=image_data, file_name="processed_image.png")