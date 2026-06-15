import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    layout="wide"
)

st.title("🛍 Customer Segmentation Dashboard")

uploaded_file = st.file_uploader(
    "Upload Customer Dataset",
    type=["csv"]
)

if uploaded_file:

    try:
        df = pd.read_csv(uploaded_file, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(uploaded_file, encoding='latin1')

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Statistics")
    st.write(df.describe())

    if 'Genre' in df.columns:

        genre_fig = px.histogram(
            df,
            x="Genre",
            title="Genre Distribution"
        )

        st.plotly_chart(
            genre_fig,
            use_container_width=True
        )

    income_fig = px.histogram(
        df,
        x='Annual Income (k$)',
        title='Income Distribution'
    )

    st.plotly_chart(
        income_fig,
        use_container_width=True
    )

    spending_fig = px.histogram(
        df,
        x='Spending Score (1-100)',
        title='Spending Score Distribution'
    )

    st.plotly_chart(
        spending_fig,
        use_container_width=True
    )

    if 'Cluster' in df.columns:

        cluster_fig = px.scatter(
            df,
            x='Annual Income (k$)',
            y='Spending Score (1-100)',
            color='Cluster',
            title='Customer Segments'
        )

        st.plotly_chart(
            cluster_fig,
            use_container_width=True
        )