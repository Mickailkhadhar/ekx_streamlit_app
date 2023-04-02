import pandas as pd
import unittest
from src.plots import Plotter

data = pd.DataFrame({
    "StudentID": [1, 2, 3, 4, 5],
    "sex": ["M", "F", "M", "F", "M"],
    "romantic": ["no", "yes", "no", "yes", "no"],
    "famrel": [4, 5, 3, 4, 2],
    "FinalGrade": [12, 6, 18, 14, 8],
    "FirstName": ["Antoine", "Henri", "Juliette", "Julien", "Emilie"],
    "FamilyName": ["Dupond", "Dupont", "Thomas", "Martin", "Henri"]
})


class TestPlotter(unittest.TestCase):

    def setUp(self):
        self.plotter = Plotter()
        self.data = data
        self.cols_to_drop = ["FirstName", 'FamilyName']
        self.x_col = 'FinalGrade'
        self.y_col = "StudentID"
        self.hue_col = "sex"
        self.feature_col = "FinalGrade"

    def test_get_scratter_plot(self):
        fig = self.plotter.get_scatter_plot(self.data, self.x_col, self.y_col, self.hue_col)
        self.assertIsNotNone(fig)

    def test_get_matrix_correlation(self):
        fig = self.plotter.get_matrix_correlation(self.data, self.cols_to_drop)
        self.assertIsNotNone(fig)

    def test_get_correlations_from_feature(self):
        fig = self.plotter.get_correlations_from_feature(self.data, self.cols_to_drop, self.feature_col)
        self.assertIsNotNone(fig)


if __name__ == '__main__':
    unittest.main()
