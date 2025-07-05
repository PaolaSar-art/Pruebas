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