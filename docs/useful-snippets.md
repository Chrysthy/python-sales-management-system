# 🧩 Useful Snippets

Trechos úteis de Streamlit, Pandas e Plotly para consultar durante o desenvolvimento do projeto.

## 📦 Importações principais

```python
import streamlit as st
import pandas as pd
import plotly.express as px
```

## ⚙️ Configurar a página

```python
st.set_page_config(
    page_title="Sistema de Vendas",
    page_icon="📊",
    layout="wide"
)
```

## 🎨 Títulos e mensagens

```python
st.title("Sistema de Vendas")
st.subheader("Vendas cadastradas")

st.success("Venda cadastrada com sucesso!")
st.error("Preencha os campos obrigatórios.")
st.warning("Verifique os dados informados.")
st.info("Cadastre uma nova venda.")
```

## 🎨 Textos com cores

```python
st.markdown(":green[Venda cadastrada com sucesso!]")
st.markdown(":red[Preencha os campos obrigatórios.]")
st.markdown(":blue[Informação]")
st.markdown(":orange[Atenção]")
```

Também é possível usar HTML para personalizar mais:

```python
st.markdown(
    "<p style='color:green;'>Venda cadastrada com sucesso!</p>",
    unsafe_allow_html=True
)
```

## 📌 Campos obrigatórios

O Streamlit não possui `required=True`, então a validação deve ser feita manualmente.

```python
vendedor = st.text_input("Vendedor *")
produto = st.text_input("Produto *")

if st.button("Cadastrar"):
    if not vendedor or not produto:
        st.error("Preencha todos os campos obrigatórios.")
    else:
        st.success("Venda cadastrada!")
```

## 🔢 Limitar valores numéricos

```python
quantidade = st.number_input(
    "Quantidade",
    min_value=1,
    step=1
)

valor = st.number_input(
    "Valor",
    min_value=0.0,
    step=0.01,
    format="%.2f"
)
```

## ☑️ Checkbox

```python
confirmar = st.checkbox("Confirmo os dados informados")

if confirmar:
    st.write("Dados confirmados.")
```

## 🔘 Radio button

```python
forma_pagamento = st.radio(
    "Forma de pagamento",
    ["Pix", "Cartão", "Dinheiro"]
)
```

## 📋 Criar formulário

```python
with st.form("form_venda"):

    vendedor = st.selectbox(
        "Vendedor",
        ["Ana", "Bruno", "Carla"]
    )

    produto = st.selectbox(
        "Produto",
        ["Notebook", "Celular", "Fone"]
    )

    quantidade = st.number_input(
        "Quantidade",
        min_value=1,
        step=1
    )

    valor = st.number_input(
        "Valor",
        min_value=0.0,
        step=0.01
    )

    cadastrar = st.form_submit_button("Cadastrar venda")
```

## 📐 Criar colunas

```python
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Faturamento", "R$ 10.000")

with col2:
    st.metric("Total de vendas", "120")

with col3:
    st.metric("Produtos vendidos", "350")
```

## 📑 Criar abas

```python
tab1, tab2 = st.tabs([
    "Vendas",
    "Dashboard"
])

with tab1:
    st.write("Tabela de vendas")

with tab2:
    st.write("Gráficos")
```

## 📊 Mostrar tabela

```python
st.dataframe(
    tabela,
    use_container_width=True
)
```

## 💰 Criar métrica

```python
faturamento = tabela["valor"].sum()

st.metric(
    "Faturamento total",
    f"R$ {faturamento:,.2f}"
)
```

## 🔍 Filtrar dados

```python
vendedores = tabela["vendedor"].unique()

vendedor_selecionado = st.selectbox(
    "Filtrar por vendedor",
    vendedores
)

tabela_filtrada = tabela[
    tabela["vendedor"] == vendedor_selecionado
]
```

## 📊 Criar gráfico

```python
grafico = px.bar(
    tabela,
    x="vendedor",
    y="valor",
    color="produto"
)

st.plotly_chart(
    grafico,
    use_container_width=True
)
```

## 💾 Ler e salvar CSV

```python
tabela = pd.read_csv("vendas.csv")

tabela.to_csv(
    "vendas.csv",
    index=False
)
```

## ➕ Adicionar nova venda

```python
nova_venda = [
    data,
    vendedor,
    produto,
    quantidade,
    valor
]

tabela.loc[len(tabela)] = nova_venda
```

## 🔄 Atualizar a aplicação

```python
st.rerun()
```

## ▶️ Executar a aplicação

```bash
streamlit run app.py
```

Se o arquivo tiver outro nome:

```bash
streamlit run nome_do_arquivo.py
```