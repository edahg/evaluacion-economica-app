# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data

# Read the data
df = load_data('costos_ingresos.xlsx')

df = df.groupby(['MES', 'GRUPO', 'GRUPO_PP'])['Valor'].sum().reset_index()

# Ensure MES is string or categorical for proper ordering
df['MES'] = df['MES'].astype(str)

# Pivot the data for stacked/grouped bar chart
fig = px.bar(
    df,
    x='MES',
    y='Valor',
    color='GRUPO',
    barmode='stack',
    facet_col='GRUPO_PP'
)

fig.update_layout(
    title='Ingresos y Costos por Mes',
    xaxis_title='Mes',
    yaxis_title='Valor',
    legend_title='GRUPO',
    bargap=0.2
)

st.title("Ingresos y Costos UCE")
st.plotly_chart(fig, use_container_width=True)