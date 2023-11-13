import streamlit as st 
import pandas as pd
import numpy as np
import os

# Everything is accessible via the st.secrets dict:
st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])
st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])

# And the root-level secrets are also accessible as environment variables:
st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
)

st.header("salmon")

# db
# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Perform query.
df = conn.query('SELECT * FROM test;', ttl="10m")

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.gender}:")

# bar chart
st.write("Bar Chart")

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"

df = pd.read_csv(url)
df2 = df.groupby('species')['body_mass_g'].mean()
st.bar_chart(df2)

# scatter chart
st.write("Scatter Chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.scatter_chart(chart_data)
