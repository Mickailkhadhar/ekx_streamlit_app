import pandas as pd


class Scorer:

    def __init__(self):
        pass

    """ We are trying here to obtain a formula which depends on are whole future
    NB:
    the use of correlation here might lead to refactoring code
    if also used in plots.py"""

    def processing_data(self, data):

        data = pd.DataFrame()
        # process our datas here.

        # assert max(finalGrade) <= 20 and min(finalGrade >=0)
        return data

    def set_FinalGradeScore(self, x):
        # match method implemented of python 3.10, cant use it here

        if isinstance(x, (int, float)):
            if x <= 5:
                return 4
            elif x > 5 and x <= 10:
                return 3
            elif x > 10 and x < 16:
                return 2
            elif x > 15 and x <= 20:
                return 1.5
            else:
                return 1
        else:
            raise TypeError

    def set_absences_score(self, x):
        if isinstance(x, (int, float)):  # float for half day of absence
            if x < 10:
                return 1
            elif x >= 10 and x < 30:
                return 2
            elif x >= 30:
                return 3
        else:
            raise TypeError

    def set_guardian_score(self, x):
        if isinstance(x, (str)):
            if x == "mother":
                return 1
            elif x == "father":
                return 2
            elif x == 'other':
                return 3
        else:
            raise TypeError
