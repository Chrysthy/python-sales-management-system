# 🔄 Workflow de Desenvolvimento

O projeto será desenvolvido passo a passo, começando pela criação da interface do sistema e finalizando com um dashboard interativo de vendas.

## 1. Criar a interface do sistema
- Construir a interface da aplicação utilizando Streamlit.
- Criar a página principal do sistema de vendas.
- Carregar os dados existentes de um arquivo CSV utilizando Pandas.

## 2. Criar o formulário de cadastro de vendas
- Adicionar um formulário na barra lateral para cadastrar novas vendas.
- Coletar informações como:
  - Data
  - Vendedor
  - Produto
  - Quantidade
  - Valor da venda

## 3. Salvar os dados da venda
- Capturar as informações preenchidas no formulário.
- Adicionar cada nova venda à base de dados existente.
- Salvar os dados atualizados novamente no arquivo CSV.

## 4. Exibir as vendas cadastradas
- Mostrar todas as vendas registradas diretamente na aplicação.
- Utilizar um DataFrame do Pandas para organizar e exibir os dados.

## 5. Criar o dashboard de vendas
- Calcular o faturamento total com base nos dados das vendas.
- Exibir métricas utilizando Streamlit.
- Criar gráficos interativos com Plotly, incluindo:
  - Valor das vendas por vendedor
  - Distribuição das vendas por produto

## 6. Executar e testar a aplicação
- Iniciar a aplicação Streamlit localmente.
- Testar o cadastro de novas vendas.
- Verificar se os dados estão sendo salvos corretamente.
- Confirmar se as novas vendas aparecem na tabela e nos gráficos do dashboard.