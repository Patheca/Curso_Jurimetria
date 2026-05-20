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

st.markdown("<br><br>", unsafe_allow_html=True)

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

st.markdown("""
<div style="
    padding: 15px;
    background-color: #f0f2f6;
    border-left: 5px solid #0c326f;
    border-radius: 5px;
">
<b>Contagem de Processos por Resultado (Mérito = Sim)</b><br>
Este gráfico de barras horizontais mostra a contagem de processos para cada categoria de resultado 
(Improcedente, Procedente em parte, Procedente), apenas para aqueles processos onde a coluna 'Mérito' é igual a 'Sim'. 
Ele é útil para entender a distribuição dos desfechos dos processos com mérito avaliado.
</div>
""", unsafe_allow_html=True)


