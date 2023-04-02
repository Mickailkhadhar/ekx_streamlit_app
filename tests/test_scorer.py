import unittest
import pandas as pd
from scorer import Scorer


class TestScorer(unittest.TestCase):

    def setUp(self):
        self.scorer = Scorer()
        self.data = pd.DataFrame({
            "StudentID": [1, 2, 3, 4, 5],
            "sex": ["M", "F", "M", "F", "M"],
            "romantic": ["no", "yes", "no", "yes", "no"],
            "famrel": [4, 5, 3, 4, 2],
            "absences": [5, 10, -1, 20, 25],
            "guardian": ["mother", "father", "other", "3", "mother"],
            "FinalGrade": [12, 6, 18, 14, 25]
        })

    def test_processing_data(self):
        processed_data = self.scorer.processing_data(self.data)
        self.assertIsInstance(processed_data, pd.DataFrame)

    def test_set_FinalGradeScore(self):
        self.assertEqual(self.scorer.set_FinalGradeScore(15), 2)
        self.assertEqual(self.scorer.set_FinalGradeScore(20), 1.5)
        self.assertEqual(self.scorer.set_FinalGradeScore(5), 4)
        self.assertEqual(self.scorer.set_FinalGradeScore(3), 4)
        with self.assertRaises(TypeError):
            self.scorer.set_FinalGradeScore("not a number")

    def test_set_absences_score(self):
        self.assertEqual(self.scorer.set_absences_score(5), 1)
        self.assertEqual(self.scorer.set_absences_score(10), 2)
        self.assertEqual(self.scorer.set_absences_score(35), 3)
        with self.assertRaises(TypeError):
            self.scorer.set_absences_score("not a number")

    def test_set_guardian_score(self):
        self.assertEqual(self.scorer.set_guardian_score("mother"), 1)
        self.assertEqual(self.scorer.set_guardian_score("father"), 2)
        self.assertEqual(self.scorer.set_guardian_score("other"), 3)
        with self.assertRaises(TypeError):
            self.scorer.set_guardian_score(123)


if __name__ == '__main__':
    unittest.main()
