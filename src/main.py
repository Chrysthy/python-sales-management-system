import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Sales System",
    page_icon="📊"
)

tabela_vendas = pd.read_csv("data/vendas.csv")

st.write("# Sistema de Vendas")

st.write("## Cadastrar Vendas")
data = st.date_input("Data")
vendedor = st.selectbox("Vendedor", ["Chrystine", "Noob", "Leon"])
produto = st.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.number_input("Quantidade", step=1)
valor = st.number_input("Valor")
botao_cadastar = st.button("Cadastrar Venda")


st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)


st.write("## Dashboard")
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento total", f"R$ {faturamento}")

grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)

grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.5) 
st.plotly_chart(grafico2)