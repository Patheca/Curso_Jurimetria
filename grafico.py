#!pip install streamlit
#!pip install pandas
#!pip install seaborn
#!pip install matplotlib

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")


url = "https://docs.google.com/spreadsheets/d/1M2t-eR0NE_vAPtjl9CBS7RINxaY3POcVoO4xQvCZnL8/export?format=xlsx"

df = pd.read_excel(url, sheet_name="SENTENÇAS")

# Visualizar primeiras linhas
df.head()
st.header('ESTUDO JURIMÉTRICO SOBRE CORRELAÇÃO ARGUMENTATIVA NO MACROLITÍGIO FISCAL')

df.columns = (
    df.columns.str.replace(" ", "_")
)



df_merito_sim = df[df['Mérito'] == 'Sim'].copy()

plt.figure(figsize=(10, 6))
sns.countplot(y=df_merito_sim['Resultado'], order=df_merito_sim['Resultado'].value_counts().index, palette=['#942234', '#aa8424', '#0c326f'])
plt.title('GRÁFICO 1 - Contagem de Processos por Resultado (Mérito = Sim)')
plt.xlabel('Quantidade de Processos')
plt.ylabel('Resultado da Sentença')
st.pyplot(plt)
plt.show()

