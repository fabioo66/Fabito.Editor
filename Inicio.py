import streamlit as st
from PIL import Image
from module import tools
from streamlit_lottie import st_lottie

# Configuración de la página
icon = Image.open("assets/icon.png")
st.set_page_config(page_title="Fabito.editor", page_icon=icon, layout="wide")

# Título y descripción de la página
st.title("Bienvenido a Fabito.Editor")

# Agrego animacion
lottie_hello = tools.load_lottieflie("lottie_files/hello.json")
st_lottie(
    lottie_hello,
    loop=True,
    reverse=False,
    quality="low",
    height=150,
    width=150,
    key=None
)

st.write("Esta aplicación web te permite realizar dos acciones principales con tus imágenes: eliminar el fondo y comprimir el tamaño.")

# Sección de eliminación de fondo
st.header("Eliminar Fondo de Imágenes")
st.write("Con esta funcionalidad, puedes eliminar el fondo de tus imágenes y guardarlas en formato PNG.")

# Sección de compresión de imágenes
st.header("Comprimir Imágenes")
st.write("Aquí puedes comprimir el tamaño de tus imágenes para reducir su espacio de almacenamiento.")