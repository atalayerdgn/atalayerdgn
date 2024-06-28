import streamlit as st
import streamlit_pdf_viewer as stf
import os
def main() -> None:
    st.set_page_config(
        page_title="Maths For ML Cheat Sheet",
        page_icon=":computer:",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.title("Maths For ML Cheat Sheet")
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        stf.pdf_viewer('app/doc/CheatSheets/JeBOVhsKEeibhw72l5cNxg_264774001b0a11e8aa0cf1e466b4007b_maths4ml-mvc-cheatsheet.pdf', height=800, width=800,pages_vertical_spacing=1)
    with col2:
        stf.pdf_viewer('app/doc/CheatSheets/PoPGwxvuEein8Q5msPYVqg_3edb0e701bee11e8a3bbdda3bd061ec3_maths4ml-linearalgebra-formula.pdf', height=800, width=800,pages_vertical_spacing=1)
    with col3:
        stf.pdf_viewer('app/doc/CheatSheets/9o8_wRzIEeiYVg4zL1pCXA_f6bda2201cc811e89078cbf6a5cb072b_Mathematics_for_Machine_Learning_PCA_Lecture_Slides.pdf', height=800, width=800,pages_vertical_spacing=1)
    st.markdown("---")

if __name__ == "__main__":
	main()
