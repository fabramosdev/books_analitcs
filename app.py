import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("datasets/data_customer_reviews.csv")
df_top100 = pd.read_csv("datasets/data_top_100_trending_books.csv")

price_max = df_top100["book price"].max()
price_mim = df_top100["book price"].min()

max_price = st.sidebar.slider("Price Range", price_mim, price_max, price_max)
df_books = df_top100[df_top100["book price"] <= max_price]

df_books

fig = px.histogram(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])

col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)
