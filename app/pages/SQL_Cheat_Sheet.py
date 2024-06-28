import streamlit as st
import streamlit_pdf_viewer as stf
import os
def main() -> None:
    """
    This function is used to show the SQL Cheat Sheet.
    """
    st.set_page_config(
        page_title="SQL Cheat Sheet",
        page_icon=":computer:",
        layout="centered",
        initial_sidebar_state="expanded"
    )
    st.title("SQL Cheat Sheet")
    st.markdown("---")
    stf.pdf_viewer('app/doc/CheatSheets/SQL-cheat-sheet.pdf', height=800, width=1200,pages_vertical_spacing=1)
    st.markdown("---")

if __name__ == "__main__":
	main()
