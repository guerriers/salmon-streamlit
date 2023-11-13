import streamlit as st 
import pandas as pd
import numpy as np

st.header("Faiy krub")

st.write("Bar Chart")

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"

df = pd.read_csv(url)
df2 = df.groupby('species')['body_mass_g'].mean()
st.bar_chart(df2)

st.write("Scatter Chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.scatter_chart(chart_data)