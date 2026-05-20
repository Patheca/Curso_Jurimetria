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

