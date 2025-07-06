
import streamlit as st

# Título de la app
st.title("👋 ¡Bienvenido a mi app sencilla!")

# Entrada de texto
nombre = st.text_input("Escribe tu nombre:")

# Botón para generar saludo
if st.button("Saludar"):
    st.success(f"Hola, {nombre}! Qué gusto tenerte aquí 😊")
