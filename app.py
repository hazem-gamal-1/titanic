
import pandas as pd

import plotly.express as px
import streamlit as st

df = pd.read_csv("data/titanic.csv")
df.columns = df.columns.str.lower()
df["class"] = df["pclass"].map({1: "First", 2: "Second", 3: "Third"})
df["survival"] = df["survived"].map({0: "Died", 1: "Survived"})
df["port"] = df["embarked"].map({"C": "Cherbourg", "Q": "Queenstown", "S": "Southampton"})
df["family_size"] = df["sibsp"] + df["parch"] + 1
df["title"] = df["name"].str.extract(r",\s*([^\.]+)\.", expand=False)
df["age_group"] = pd.cut(df["age"], [0, 12, 18, 35, 60, 80],
                         labels=["child", "teen", "young adult", "adult", "senior"])

ORDERS = {"class": ["First", "Second", "Third"], "survival": ["Died", "Survived"],
          "age_group": ["child", "teen", "young adult", "adult", "senior"]}
COLORS = {"Died": "#D95D4A", "Survived": "#0F766E"}

st.title("Titanic Data Analysis")
st.caption("This app is a simple data analysis of the Titanic dataset. The dataset is available on [Kaggle](https://www.kaggle.com/c/titanic/data).")
st.image('https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcQINOG1yj9-cUowefr5MyHeQe0_xPzyvE90-V6T70xyMed-Hl2kwIH4PkzKOXzWt6kNGPXz4RzyCbkKHvjK1F6BUxTQ1DaUcr9PqVJ7SNg4mx0E3H3YFrjr&usqp=CAc',width='stretch')
show_data = st.checkbox("Show raw data")

if show_data:
    st.dataframe(df,hide_index=True)


classes = st.multiselect("Select class", options=ORDERS["class"], default=ORDERS["class"])
genders = st.multiselect("Select gender", options=df["sex"].unique(), default=df["sex"].unique())


data = df[(df["class"].isin(classes)) & (df["sex"].isin(genders))]

c1,c2=st.columns(2)


with c1:
    fig = px.histogram(data, x="family_size", nbins=11, labels={"family_size": "Family size (incl. the passenger)"},
                   title="How big were the families on board?")
    fig.update_layout(bargap=0.1, yaxis_title="Passengers")
    st.plotly_chart(fig, use_container_width=True)
with c2:
    fig2=data['survived'].value_counts().reset_index()
    fig2.columns=['survived','count']
    fig = px.pie(fig2, values='count', names='survived', title="Survival rate")
    st.plotly_chart(fig, use_container_width=True)