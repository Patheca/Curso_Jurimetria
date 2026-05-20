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

st.markdown("<br><br>", unsafe_allow_html=True)


tese_columns = [
    'Tese:_Legalidade_do_Teto_de_Custo_Fiscal_(Art._4º-A_Lei_14.148/21)',
    'Tese:_Legalidade_do_Ato_Declaratório_Executivo_RFB_02/2025',
    'Tese:_Inexistência_de_Isenção_Onerosa_(Art._178_CTN)',
    'Tese:_Observância_da_Anterioridade_Tributária',
    'Tese:_Ausência_de_Direito_Adquirido_a_Regime_Jurídico'
]

accepted_counts = {}
total_counts = {}
for col in tese_columns:
    if col in df.columns:
        accepted_counts[col] = df[df[col] == 'Aceito'].shape[0]
        total_counts[col] = df[col].dropna().shape[0] # Count non-NaN values

# Create a DataFrame for plotting
accepted_df = pd.DataFrame(list(accepted_counts.items()), columns=['Tese', 'Contagem de Aceitos'])
accepted_df['Total de Teses'] = accepted_df['Tese'].map(total_counts)
accepted_df['Percentual Aceito'] = (accepted_df['Contagem de Aceitos'] / accepted_df['Total de Teses']) * 100

# Shorten thesis names for better readability on the plot
accepted_df['Tese Curta'] = accepted_df['Tese'].str.replace('Tese:_', '').str.replace('_(Art._4º-A_Lei_14.148/21)', '').str.replace('_(Art._178_CTN)', '').str.replace('RFB_02/2025', '').str.replace('_', ' ').str.strip()

# Sort by 'Contagem de Aceitos' for better visualization
accepted_df = accepted_df.sort_values(by='Contagem de Aceitos', ascending=False)

# Create a custom palette starting with the requested color
custom_palette = sns.light_palette("#942234", n_colors=len(accepted_df), reverse=True)

plt.figure(figsize=(12, 8))
ax = sns.barplot(
    x='Contagem de Aceitos',
    y='Tese Curta',
    data=accepted_df,
    palette=custom_palette
)

plt.title('GRÁFICO 2 - Aderência às Teses de Defesa - 1ª Instância (Fazenda Nacional)')
plt.xlabel('Quantidade de Teses Aceitas')
plt.ylabel('Teses - 1ª Instância')

# Loop para adicionar os percentuais dentro da barra
for i, (index, row) in enumerate(accepted_df.iterrows()):
    bar = ax.patches[i]
    width = bar.get_width()
    y = bar.get_y() + bar.get_height() / 2

    # Cor da barra (RGB)
    r, g, b, _ = bar.get_facecolor()

    # Cálculo de luminosidade (percepção humana)
    luminosidade = (0.299*r + 0.587*g + 0.114*b)

    # Escolha automática da cor do texto
    text_color = 'white' if luminosidade < 0.5 else 'black'

    # Texto perto da borda direita, mas dentro da barra
    plt.text(
        width - 0.1,   # deslocamento pequeno e fixo
        y,
        f"{row['Percentual Aceito']:.1f}%",
        va='center',
        ha='right',
        color=text_color,
        fontsize=11
    )

plt.tight_layout()
st.pyplot(plt)
plt.show()


st.markdown("""
<div style="
    padding: 15px;
    background-color: #f0f2f6;
    border-left: 5px solid #0c326f;
    border-radius: 5px;
">
<b>Aderência às Teses de Defesa por Percentual - 1ª Instância (Fazenda Nacional)</b><br>
Este gráfico de barras apresenta o percentual de vezes que cada tese de defesa da Fazenda Nacional foi Aceita 
em relação ao total de vezes que foi avaliada. Ele complementa o gráfico anterior, fornecendo uma visão proporcional 
do sucesso de cada tese.
</div>
""", unsafe_allow_html=True)


import numpy as np
import matplotlib.pyplot as plt

labels = [
    "Art. 178 CTN",
    "Teto Orçamentário",
    "ADE 02/2025",
    "Anterioridade",
    "Direito Adquirido"
]

inst1 = [90, 89, 85, 75, 88]
inst2 = [100, 100, 100, 98, 100]

angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
inst1 += inst1[:1]
inst2 += inst2[:1]
angles += angles[:1]

plt.figure(figsize=(7,7))
ax = plt.subplot(111, polar=True)

ax.plot(angles, inst1, linewidth=2, label="1ª Instância", color="#942234")
ax.fill(angles, inst1, alpha=0.2, facecolor="#942234")

ax.plot(angles, inst2, linewidth=2, label="2ª Instância", color="#aa8424")
ax.fill(angles, inst2, alpha=0.2, facecolor="#aa8424")

ax.set_thetagrids(np.degrees(angles[:-1]), labels)
plt.title("GRÁFICO 4 - Comparação da Aceitação das Teses — 1ª x 2ª Instância", fontsize=14, pad=25)
plt.legend(loc="upper left", bbox_to_anchor=(1.2, 1))
st.pyplot(plt)
plt.show()


