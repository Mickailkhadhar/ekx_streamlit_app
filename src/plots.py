import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd


class Plotter:

    def __init__(self):
        pass

    def get_scatter_plot(self, data, x, y, hue):
        fig = px.scatter(data, x=x, y=y, color=hue)
        return fig

    def get_matrix_correlation(self, data, cols_to_drop):
        fig = plt.figure(figsize=(22, 15))
        tmp_data = data.drop(cols_to_drop, axis=1)
        tmp_data = pd.get_dummies(tmp_data)
        sns.heatmap(tmp_data.corr(), annot=False)
        return fig

    def get_correlations_from_feature(self, data, cols_to_drop, feature):
        fig = plt.figure(figsize=(22, 18))
        tmp_data = data.drop(cols_to_drop, axis=1)
        tmp_data = pd.get_dummies(tmp_data)
        corr = tmp_data.corr()
        corr = corr[[feature]]
        sns.heatmap(corr, annot=False)
        return fig
