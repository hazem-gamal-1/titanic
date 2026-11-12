
import pandas as pd

import plotly.express as px
import streamlit as st
from utils.data import load_data
from utils.figure import plot_family_size_distribution, plot_outcome
from utils.config import COLORS, ORDERS
df = load_data("data/titanic.csv")
df.columns = df.columns.str.lower()
df["class"] = df["pclass"].map({1: "First", 2: "Second", 3: "Third"})
df["survival"] = df["survived"].map({0: "Died", 1: "Survived"})
df["port"] = df["embarked"].map({"C": "Cherbourg", "Q": "Queenstown", "S": "Southampton"})
df["family_size"] = df["sibsp"] + df["parch"] + 1
df["title"] = df["name"].str.extract(r",\s*([^\.]+)\.", expand=False)
df["age_group"] = pd.cut(df["age"], [0, 12, 18, 35, 60, 80],
                         labels=["child", "teen", "young adult", "adult", "senior"])


st.title("Titanic Data Analysis")
st.caption("This app is a simple data analysis of the Titanic dataset. The dataset is available on [Kaggle](https://www.kaggle.com/c/titanic/data).")
st.image('https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcQINOG1yj9-cUowefr5MyHeQe0_xPzyvE90-V6T70xyMed-Hl2kwIH4PkzKOXzWt6kNGPXz4RzyCbkKHvjK1F6BUxTQ1DaUcr9PqVJ7SNg4mx0E3H3YFrjr&usqp=CAc',width='stretch')
show_data = st.checkbox("Show raw data")

if show_data:
    st.dataframe(df,hide_index=True)


classes = st.multiselect("Select class", options=ORDERS["class"], default=ORDERS["class"])
genders = st.multiselect("Select gender", options=df["sex"].unique(), default=df["sex"].unique())


data = df[(df["class"].isin(classes)) & (df["sex"].isin(genders))]

c1,c2,c3,c4= st.columns(4)

with c1:
    st.metric(label="Total Passengers", value=len(data))

with c2:
    st.metric(label="Survival Rate", value=f"{len(data[data['survival'] == 'Survived'])/len(data)*100:.2f}%")

with c3:
    st.metric(label="Median Age", value=f"{data['age'].median():.2f}")

with c4:
    st.metric(label="Median Fare", value=f"${data['fare'].median():.2f}")



c1,c2=st.columns(2)


with c1:
    fig1 = plot_family_size_distribution(data)
    st.plotly_chart(fig1, use_container_width=True)
with c2:
    fig2 = plot_outcome(data)
    st.plotly_chart(fig2, use_container_width=True)