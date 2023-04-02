import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from src.plots import Plotter
from src.scorer import Scorer

st.set_page_config(page_title = "My scneario",
                   layout = 'wide')


plotter = Plotter()
scorer = Scorer()

@st.cache_data
def main():
    st.markdown("# Plotting My Scenario")
    st.sidebar.header("Plotting My Scenario")

    st.sidebar.markdown("***")
    st.markdown("# <span>MY SCENARIO</span>", unsafe_allow_html=True)
    st.markdown("***")

    st.write("This page will show you an example of plots you can do in the app section. This page was not intented do be deployed")


    data = pd.read_csv('./Recrutement/student_data.csv', sep = ',')
    st.subheader("Plot distrubtion of all students by gender")
    st.plotly_chart(plotter.get_scatter_plot(data, 'FinalGrade', 'StudentID', 'sex'), theme = 'streamlit', use_container_width=True)

    st.subheader('Get correlation between all features and final grade')
    cols_to_drop = ['StudentID', 'FirstName', 'FamilyName']
    st.write(plotter.get_matrix_correlation(data, cols_to_drop))

    st.subheader("1-feature correlation")
    cols_to_drop = ['StudentID', 'FirstName', 'FamilyName']
    ftr = 'FinalGrade'
    st.write(plotter.get_correlations_from_feature(data, cols_to_drop, feature = ftr))


    st.subheader("Distribution of grades depending of who is in charge of the child")
    st.plotly_chart(plotter.get_scatter_plot(data, 'FinalGrade', 'StudentID', 'guardian'), theme = 'streamlit', use_container_width=True)
    fig = sns.displot(data=data, x="FinalGrade", hue="guardian", kind="kde", multiple = 'stack')

    st.pyplot(fig)
    st.write("""We can see that when moms are responsible, the student grades are following normal distribution. It seems even when the father is in charge, even if we have fewer examples.
    However, when neither the mom nor the dad is responsible for the child, we can assume in this sample at least, that the child would have a bit more difficulties than the mean""")

    st.subheader("Hue of students with extra courses at home")
    st.plotly_chart(plotter.get_scatter_plot(data, 'FinalGrade', 'StudentID', 'schoolsup'), theme = 'streamlit', use_container_width=True)
    st.write("""  Children with extra educational support seem to need it as most of them have a grade at 10 or lower """)

    st.subheader('Hue of students who want to take higher education')
    st.plotly_chart(plotter.get_scatter_plot(data, 'FinalGrade', 'StudentID', 'higher'), theme = 'streamlit', use_container_width=True)
    st.write(""" I suppose i will have examples of student with grades at 10 or greater with this""")

    st.subheader("Plot some Health status by grades")
    st.plotly_chart(plotter.get_scatter_plot(data, 'FinalGrade', 'StudentID', 'health'), theme = 'streamlit', use_container_width=True)
    fig = sns.displot(data=data, x="FinalGrade", hue="health", kind="kde", multiple = 'stack')
    st.pyplot(fig)
    st.write(""" healthy children can actually attend class so I think they will have better grades""")

    st.subheader("Do absences affect grades ? ")


    st.plotly_chart(plotter.get_scatter_plot(data, 'FinalGrade', 'StudentID', 'absences'), theme = 'streamlit', use_container_width=True)
    fig = sns.displot(data=data, x="FinalGrade", hue="absences", kind="kde", multiple = 'stack')
    st.pyplot(fig)
    st.write(""" you need to attend class to understand it and then have good grades in general""")



    st.subheader("Lets try to plot our first scenario")
    grade_score=[scorer.set_FinalGradeScore(x) for x in data['FinalGrade']]
    absences_score=[scorer.set_absences_score(x) for x in data['absences']]
    guardian_score=[scorer.set_guardian_score(x) for x in data['guardian']]
    assert len(grade_score) == len(absences_score)
    assert len(grade_score) == len(guardian_score)
    data['score'] = [(grade_score[i] * absences_score[i] * guardian_score[i])/5 for i in range(len(grade_score))]

    st.plotly_chart(plotter.get_scatter_plot(data, 'FinalGrade', 'StudentID', 'score'), theme = 'streamlit', use_container_width=True)




if __name__ == "__main__":
    main()