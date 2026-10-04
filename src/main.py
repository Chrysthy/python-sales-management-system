import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Sales System",
    page_icon="📊"
)

tabela_vendas = pd.read_csv("data/vendas.csv")

st.write("# Sistema de Vendas")

st.sidebar.write("## Cadastrar Vendas")

with st.sidebar.form(key="formulario_vendas", clear_on_submit=True):

    data = st.sidebar.date_input("Data", min_value="2027-01-01")
    vendedor = st.sidebar.selectbox("Vendedor", ["Noob", "Leon", "Collin"], index=None, placeholder="Selecione um vendedor")
    produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"], index=None, placeholder="Selecione um produto")
    quantidade = st.sidebar.number_input("Quantidade", step=1)
    valor = st.sidebar.number_input("Valor")
    botao_cadastrar = st.sidebar.button("Cadastrar Venda")

if botao_cadastrar:

    if valor <= 0 or quantidade == 0 or vendedor is None or produto is None:
        st.warning("Venda com erros de preenchimento")

    else:
        nova_venda = [str(data), vendedor, produto, quantidade, valor]
        ultima_linha = len(tabela_vendas)

        tabela_vendas.loc[ultima_linha] = nova_venda
        tabela_vendas.to_csv("data/vendas.csv", index=False)

        st.success("Venda Cadastrada!")



st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)


st.write("## Dashboard")
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento total", f"R$ {faturamento}")

grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)

grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.5) 
st.plotly_chart(grafico2)