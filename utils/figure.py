import plotly.express as px

from utils.config import COLORS
from utils.config import ORDERS


def plot_family_size_distribution(df):
    """
    Plot the distribution of family sizes on the Titanic.
    """
    fig = px.histogram(df, x="family_size", color="survival", barmode="group",
                       category_orders=ORDERS, color_discrete_map=COLORS,
                       title="Family Size Distribution")
    fig.update_layout(xaxis_title="Family Size", yaxis_title="Count")
    return fig


def plot_outcome(df):
    """
    Plot the survival outcome of passengers on the Titanic.
    """
    fig = px.pie(df, names="survival", color="survival",
                 category_orders=ORDERS, color_discrete_map=COLORS,
                 title="Survival Outcome")
    return fig