import streamlit as st
import os
import streamlit_pdf_viewer as stf
def main() -> None:
    """
    This function is used to show the Cheat Sheets.
    """
    st.set_page_config(
        page_title="Web Application for Data Science",
        page_icon=":computer:",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.title("Cheat Sheets")
    st.markdown("---")
    with st.form("cheatsheets"):
        cheatsheets = st.radio('Select a cheat sheet:', ['SQL','Maths For ML','Pandas','Numpy','Linear Regression','Logistic Regression','Regression Problems'])
        st.markdown("---")
        submit_button = st.form_submit_button(label='Show Cheat Sheet')
        if submit_button and cheatsheets == 'SQL':
            st.switch_page('pages/SQL_Cheat_Sheet.py')
        elif submit_button and cheatsheets == 'Maths For ML':
            st.switch_page('pages/MathsForMachineLearning.py')
        elif submit_button and cheatsheets == 'Pandas':
            st.switch_page('pages/Pandas.py')
if __name__ == "__main__":
    main()
