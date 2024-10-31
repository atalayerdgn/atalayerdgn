import streamlit as st


class AboutMe:
    def __init__(self) -> None:
        pass
    def AboutMe_() -> None:
        """
        This function is used to show the About Me page.
        """
        st.set_page_config(
        page_title="About Me",
        page_icon=":computer:",
        layout="wide",
        initial_sidebar_state="expanded"
        )
        st.title("Atalay Erdogan")
        st.subheader("Student")
        st.markdown("-----")
        st.subheader("Info")
        col1, col2 = st.columns(2)
        with col1:
            with st.expander("Türkçe"):
                st.write("Merhaba. Lisans düzeyi eğitim öğretim hayatıma Gebze Teknik Üniversitesinde İktisat bölümü okuyarak başladım. Verilen eğitimin yetersiz olduğunu düşünerek okulumu bıraktım. \
                        Sonra 42 Kocaeli ile tanıştım ve kendimi istediğim alanda geliştirme fırsatı buldum. Bu okulda algoritma bazlı C ve C++ eğitimi görüyorum. Açıkcası benim için verimli bir tecrübe oluyor.\
                        Kendimi bu konularda geliştirdikten sonra kendimi keşfetmeye karar verdim ve bir anda kendimi Veri Bilimi alanında buldum. Yakın zamanda bu alanda projeler geliş ediyorum. Şu anda Sakarya Uygulamalı Bilimler Üniversitesi \
                        Büyük Veri Analistliği Bölümünde okuyorum.")
        st.subheader("Skills")
        col3, col4 = st.columns(2)
        with col3:
            st.write("Python")
            st.write("SQL")
            st.write("Docker")
            st.write("C / C++")
            st.write("Data Analysis")
            st.write("Linux")
        with col4:
            st.write("Machine Learning")
            st.write("Socket Programming")
            st.write("Data Science")
            st.write("Data Processing")
            st.write("Big Data")
        st.markdown("-----")

def main():
    AboutMe.AboutMe_()

if __name__ == "__main__":
    main()
