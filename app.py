import streamlit as st 
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

# Create a sidebar for the menu
menu = st.sidebar.selectbox("Menu", ["salmon", "Bar Chart", "Scatter Chart"])

# Create different content based on the selected menu item
if menu == "salmon":
    st.title("Home Page")

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

# Bar chart
elif menu == "Bar Chart":
    st.title("Bar Chart")

    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
    df = pd.read_csv(url)
    df2 = df.groupby('species')['body_mass_g'].mean()
    st.bar_chart(df2)

# Scatter chart
elif menu == "Scatter Chart":
    st.title("Scatter Chart")

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.scatter_chart(chart_data)

# # db
# st.write("DB postgresql")
# # Initialize connection.
# conn = st.connection("postgresql", type="sql")

# # Perform query.
# df = conn.query('SELECT * FROM test;', ttl="10m")

# # Print results.
# for row in df.itertuples():
#     st.write(f"{row.name} has a :{row.gender}:")
