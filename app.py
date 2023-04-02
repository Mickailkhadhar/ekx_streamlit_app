import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from src.plots import Plotter
from src.scorer import Scorer

st.set_page_config(page_title = "See students with difficulties",
                   layout = 'wide')

@st.cache_data
def stylish_page():
    st.sidebar.markdown("# <span style=\"color:white background:#48b4e3\" ><center>Visualize students performances</center></span>", unsafe_allow_html=True)

plotter = Plotter()
scorer = Scorer()


def main():
    stylish_page()
    st.markdown("# <span style=\"color:#48b4e3\">Home</span>", unsafe_allow_html=True)
    st.markdown("***")
    st.sidebar.markdown('***')
    st.sidebar.markdown(" Lets plot some scatter plot based on final grades")
    st.sidebar.markdown(" Which column would you want to plot ??")
    st.sidebar.markdown("***")
    data = pd.read_csv('Recrutement/student_data.csv', sep = ',')
    keyword = st.sidebar.selectbox(label = 'Choose a column', options = data.drop(['StudentID', 'FinalGrade', 'FamilyName', 'FirstName'], axis = 1).columns)
    plot_type = st.sidebar.selectbox(label = 'Choose which plot you want', options = ['Scatter_plot', 'Distplot', "1-feature-correlations"])

    if st.sidebar.button("Plot", key = 'test'):
        st.markdown("### **<span style=\"color:#48b4e3\">PLOTTING</span>**", unsafe_allow_html=True)
        st.subheader(f"Plot distribution of all students by {keyword}")
        if plot_type == 'Scatter_plot':

            st.plotly_chart(plotter.get_scatter_plot(data, 'FinalGrade', 'StudentID', keyword), theme = 'streamlit', use_container_width=True)

        elif plot_type == 'Displot':
            st.subheader(f"Density plot of {keyword} column vs FinalGrade")
            fig = sns.displot(data=data, x="FinalGrade", hue=keyword, kind="kde", multiple = 'stack')
            st.pyplot(fig, theme = 'streamlit', use_container_width = True)
        else: ## 1-ftr correlation matrix here
            st.subheader(f"It is only possible for now to have 1-feature correlation with FinalGrade instead of {keyword}")
            cols_to_drop = ['StudentID', 'FirstName', 'FamilyName']
            ftr = 'FinalGrade'
            st.write(plotter.get_correlations_from_feature(data, cols_to_drop, feature = ftr))

    
    st.subheader("Scoring plot with absences, guardian and FinalGrade columns")
    grade_score=[scorer.set_FinalGradeScore(x) for x in data['FinalGrade']]
    absences_score=[scorer.set_absences_score(x) for x in data['absences']]
    guardian_score=[scorer.set_guardian_score(x) for x in data['guardian']]
    assert len(grade_score) == len(absences_score)
    assert len(grade_score) == len(guardian_score)
    data['score'] = [(grade_score[i] * absences_score[i] * guardian_score[i])/5 for i in range(len(grade_score))]

    st.plotly_chart(plotter.get_scatter_plot(data, 'FinalGrade', 'StudentID', 'score'), theme = 'streamlit', use_container_width=True)


if __name__ == '__main__':
    main()

