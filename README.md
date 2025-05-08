# 📊 Dashboard de Marketing Digital

Este projeto cria um **dashboard interativo** para análise de campanhas de marketing digital utilizando o **Streamlit**. O dashboard permite filtrar os dados com base em diversos critérios e exibe gráficos interativos como cliques, conversões, custos e receitas ao longo do tempo.

## Funcionalidades 🚀

- **Filtros interativos** 🔍: O usuário pode filtrar os dados de campanhas com base em:
  - 🗓️ Período da campanha
  - 👥 Cliente
  - 📢 Canal de divulgação
  - 🎯 Tipo de campanha
  - 💻 Quantidade de cliques
  - 💰 Faixa de custo total
  
- **Gráficos interativos** 📈:
  - **Total de Cliques por Canal** 📊: Um gráfico de barras mostrando o total de cliques por canal.
  - **Conversões por Campanha** 🎯: Um gráfico de barras mostrando o número de conversões por campanha.
  - **Custo Total por Cliente** 💸: Um gráfico de barras mostrando o custo total por cliente.
  - **Receita Total ao Longo do Tempo** 📅: Um gráfico de linha mostrando a receita total ao longo do tempo.

## Pré-requisitos ⚙️

Para rodar este projeto, é necessário ter o **Python 3.x** instalado em seu ambiente. Além disso, o projeto utiliza as seguintes bibliotecas:

- `streamlit` - Para a criação da interface interativa.
- `pandas` - Para manipulação de dados.
- `plotly` - Para gráficos interativos.

Você pode instalar as dependências necessárias com o seguinte comando:

```bash
pip install streamlit pandas plotly

## Como usar 🛠️

Clone este repositório para a sua máquina local:
git clone https://github.com/seu-usuario/dash-marketing.git

Navegue até o diretório do projeto:

bash
cd dash-marketing

Execute o aplicativo Streamlit:

bash
streamlit run app.py

Estrutura do Projeto 📁
app.py: Script principal que contém a lógica do dashboard.

fato_campanha_marketing.csv: Arquivo CSV contendo os dados da campanha de marketing.

Personalização 🎨
Estilo visual: O dashboard possui um fundo roxo claro e uma sidebar preta. Você pode personalizar as cores diretamente no código, modificando os valores no bloco de estilos CSS.

Gráficos: Os gráficos são gerados usando a biblioteca plotly. Você pode personalizar os tipos de gráficos, cores e interatividade.

Contribuições 💡
Se você quiser contribuir para este projeto, sinta-se à vontade para enviar um pull request ou abrir uma issue no GitHub.
