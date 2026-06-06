import streamlit as st
import pandas as pd
import plotly.express as px

# Dados de exemplo

df = pd.DataFrame({
    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
    "Vendas": [120, 145, 98, 200, 175, 230],
    "Clientes": [40, 55, 35, 80, 70, 95]
})

st.title("Painel de Vendas")
st.write("Resumo dos últimos 6 meses")

# Exibe o dataframe 
st.subheader("Dados brutos")
st.dataframe(df, use_container_width=True)

st.subheader("Dados filtrados por mês")
st.write("Selecione o mês desejado na caixa abaixo.")

# Cira a caixa de seleção de mês específico
mes = st.selectbox("Mês", df["Mês"].unique()) # unique serve para não ter duplicações
df_filtrado = df[df["Mês"] == mes]
st.dataframe(df_filtrado)

st.subheader("Vendas por mês")
fig_bar = px.bar(df_filtrado, x="Mês", y="Vendas", text="Vendas")
st.plotly_chart(fig_bar, use_container_width=True)

# Cria um slider, uma outra forma de exibição gráfica
minimo = st.slider(
    "Vendas Mínimas",
    min_value=0,
    max_value=230,
    value=100 # valor inicial
)

# Usa o valor para filtrar o DataFrame
filtrado = df[df["Vendas"] >= minimo]
st.dataframe(filtrado)

st.subheader("Vendas por mês - Filtro Slider")
fig_bar_slider = px.bar(filtrado, x="Mês", y="Vendas", text="Vendas")
st.plotly_chart(fig_bar_slider, use_container_width=True)


# Cria o multiselect, para ser possível escolher vários meses
meses = st.multiselect(
    "Selecione os meses",
    options = df["Mês"].tolist(),
    default = ["Jan", "Fev"]
)

if meses:   # só filtra se tiver algo selecionado
    filtrado = df[df["Mês"].isin(meses)]
    st.dataframe(filtrado)
else:
    st.warning("Selecione ao menos um mês!")