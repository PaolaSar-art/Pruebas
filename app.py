import streamlit as st

# Título de la app
st.title("👋 Bienvenido a mi app Streamlit")

# Entrada de texto
nombre = st.text_input("¿Cuál es tu nombre?")

# Mostrar saludo si se ingresa un nombre
if nombre:
    st.write(f"¡Hola, {nombre}! ¿Cómo estas?")   




    import pandas