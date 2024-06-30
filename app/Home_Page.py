import streamlit as st
import os
from streamlit.components.v1 import components

def main():
    st.set_page_config(
        page_title="Home Page",
        page_icon=":computer:",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.title("Welcome to Homepage :handshake:")
    st.write("Written by : [Atalay Erdogan] :brain:")
    st.markdown("---")
    st.write("Here is my social media: :smiling_face_with_smiling_eyes_and_hand_covering_mouth:")
    st.markdown("<style>h6{color: darkblue;}</style>", unsafe_allow_html=True)
    st.write("LinkedIn: <https://www.linkedin.com/in/atalay-erdoğan-39aba8285>", unsafe_allow_html=True)
    st.write("Github: <https://github.com/atalayerdgn>", unsafe_allow_html=True)
    st.write("Medium:<https://medium.com/@atalayerdgnn>", unsafe_allow_html=True)
    st.markdown("---")

    with st.form("Pages"):
        Pages = st.radio('Pages:', ['My Projects', 'About Me'])
        st.markdown("---")
        submit_button = st.form_submit_button(label='Go to Page')
        if submit_button:
            if Pages == 'My Projects':
                st.switch_page('pages/Projects.py')
            if Pages == 'About Me':
                st.switch_page('pages/AboutMe.py')
            st.markdown("---")
if __name__ == "__main__":
    main()
