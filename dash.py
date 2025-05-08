import streamlit as st
import pandas as pd
import plotly.express as px

# 🚨 DEVE SER O PRIMEIRO COMANDO STREAMLIT
st.set_page_config(page_title="Dashboard de Marketing", layout="wide")

# 🎨 Estilo visual com fundo roxo claro
st.markdown("""
    <style>
        /* Fundo da área principal */
        .main {
            background-color: #f3e5f5;
        }

        /* Sidebar preta */
        section[data-testid="stSidebar"] {
            background-color: #111111;
            color: white;
        }

        /* Cor do texto e widgets na sidebar */
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] span,
        section[data-testid="stSidebar"] div,
        section[data-testid="stSidebar"] input,
        section[data-testid="stSidebar"] select {
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# 🔄 Carrega os dados do CSV
def get_data_from_csv():
    df = pd.read_csv("fato_campanha_marketing.csv")
    return df

# 🚀 Função principal do app
def app():
    st.title("📊 Dashboard de Marketing Digital")

    df = get_data_from_csv()

    # 🗓️ Converte o campo de data
    df["data_id"] = pd.to_datetime(df["data_id"], unit='D', origin='2024-01-01')

    # 🎛️ Sidebar com filtros
    st.sidebar.header("🧩 Filtros")

    data_range = st.sidebar.date_input("Período da Campanha", [df["data_id"].min(), df["data_id"].max()])
    clientes = st.sidebar.multiselect("Cliente", df["cliente_id"].unique(), default=df["cliente_id"].unique())
    canais = st.sidebar.multiselect("Canal de Divulgação", df["canal_id"].unique(), default=df["canal_id"].unique())
    campanhas = st.sidebar.multiselect("Campanha", df["campanha_id"].unique(), default=df["campanha_id"].unique())
    cliques_range = st.sidebar.slider("Quantidade de Cliques", int(df["cliques"].min()), int(df["cliques"].max()), (100, 1000))
    custo_range = st.sidebar.slider("Faixa de Custo Total (R$)", float(df["custo_total"].min()), float(df["custo_total"].max()), (100.0, 5000.0))

    # 🔍 Aplica os filtros
    df_filtrado = df[
        (df["data_id"] >= pd.to_datetime(data_range[0])) &
        (df["data_id"] <= pd.to_datetime(data_range[1])) &
        (df["cliente_id"].isin(clientes)) &
        (df["canal_id"].isin(canais)) &
        (df["campanha_id"].isin(campanhas)) &
        (df["cliques"].between(*cliques_range)) &
        (df["custo_total"].between(*custo_range))
    ]

    st.success("✅ Dados carregados com sucesso!")

    # 📊 Layout dos gráficos
    col1, col2 = st.columns(2)

    # Gráfico 1: Cliques por Canal
    col1.subheader("📈 Total de Cliques por Canal")
    cliques_canal = df_filtrado.groupby("canal_id")["cliques"].sum().sort_values(ascending=False)
    fig1 = px.bar(cliques_canal.reset_index(), x="canal_id", y="cliques", color="canal_id",
                  color_discrete_sequence=px.colors.sequential.Viridis, title="Total de Cliques por Canal")
    col1.plotly_chart(fig1, use_container_width=True)

    # Gráfico 2: Conversões por Campanha
    col2.subheader("🎯 Conversões por Campanha")
    conv_campanha = df_filtrado.groupby("campanha_id")["conversoes"].sum().sort_values(ascending=False)
    fig2 = px.bar(conv_campanha.reset_index(), x="campanha_id", y="conversoes", color="campanha_id",
                  color_discrete_sequence=px.colors.sequential.Plasma, title="Conversões por Campanha")
    col2.plotly_chart(fig2, use_container_width=True)

    # Gráfico 3: Custo Total por Cliente
    col1.subheader("💰 Custo Total por Cliente")
    custo_cliente = df_filtrado.groupby("cliente_id")["custo_total"].sum().sort_values(ascending=False)
    fig3 = px.bar(custo_cliente.reset_index(), x="cliente_id", y="custo_total", color="cliente_id",
                  color_discrete_sequence=px.colors.sequential.Magma, title="Custo Total por Cliente")
    col1.plotly_chart(fig3, use_container_width=True)

    # Gráfico 4: Receita Total ao Longo do Tempo
    col2.subheader("📅 Receita Total ao Longo do Tempo")
    receita_tempo = df_filtrado.groupby("data_id")["receita_total"].sum()
    fig4 = px.line(receita_tempo.reset_index(), x="data_id", y="receita_total", markers=True,
                   line_shape="spline", color_discrete_sequence=["#e91e63"], title="Receita Total ao Longo do Tempo")
    col2.plotly_chart(fig4, use_container_width=True)

# ▶️ Executar app
if __name__ == '__main__':
    app()
