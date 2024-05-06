import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
from module import tools

icon = Image.open("assets/icon.png")
st.set_page_config(page_title="Acerca de mi", page_icon=icon, layout="wide")

with st.container():
    st.subheader("Hola, soy Fabio :wave:")
    st.title("Un estudiante de informatica en la UNLP")
    st.write(
        "Tengo 20 años y actualmente me encuentro en segundo año de la carrera Lic. en sistemas"
    )

lottie_programming_computer = tools.load_lottieflie("lottie_files/programming_computer.json")
st_lottie(
    lottie_programming_computer,
    loop=True,
    reverse=False,
    quality="low",
    height=500,
    width=500,
    key=None
)

st.subheader("📬Conecta conmigo")

st.markdown("[Instagram](https://www.instagram.com/fabio_torrejon/)")
st.markdown("[Github](https://github.com/fabioo66)")
