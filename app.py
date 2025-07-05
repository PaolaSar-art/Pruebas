import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
df = pd.read_csv('vehicles_us.csv')

st.header('Dashboard de Vehículos en Venta (EE.UU.)')

# Histograma
if st.checkbox('Mostrar histograma de precios'):
    fig = px.histogram(df, x='price')
    st.plotly_chart(fig)

# Dispersión
if st.checkbox('Mostrar diagrama de dispersión precio vs año'):
    fig2 = px.scatter(df, x='model_year', y='price', color='condition')
    st.plotly_chart(fig2)

#Descripción
print('''Panel de Análisis de Vehículos en Venta (EE.UU.)
Esta aplicación web, desarrollada con Streamlit, permite explorar de forma interactiva un conjunto de datos de anuncios de vehículos en Estados Unidos.
Su propósito es ofrecer una herramienta visual para comprender mejor la distribución de precios y la relación entre el precio y el año de fabricación de los automóviles.
Funcionalidades:
- Carga y preprocesamiento automático de un archivo CSV con información de vehículos.
- Histograma de precios configurable mediante casilla de verificación o botón.
- Diagrama de dispersión que muestra la relación entre precio y año de modelo, activable de forma interactiva.
- Plataforma ligera que se ejecuta en un entorno virtual de Python y se despliega fácilmente en Render.
Siempre que actualices el código o datos, recuerda reflejar los cambios en este README para mantener la documentación al día.''')