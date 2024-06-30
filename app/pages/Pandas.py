import streamlit as st
import pandas as pd

class Pandas:
    def __init__(self) -> None:
        pass
    
    def set_background(self) -> None:
        st.set_page_config(
            page_title="Pandas",
            page_icon=":computer:",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        st.markdown(
            """
            <style>
            body {
                background-image: url("https://www.transparenttextures.com/patterns/sakura.png");
                background-size: cover;
                color: #333;
                font-family: Arial, sans-serif;
            }
            .stTextInput > div > div > input {
                background-color: #f0f0f0;
                color: #333;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #ccc;
            }
            .stButton > button {
                background-color: #4CAF50;
                color: white;
                padding: 12px 24px;
                text-align: center;
                display: inline-block;
                font-size: 18px;
                margin: 6px 3px;
                cursor: pointer;
                border-radius: 8px;
                border: none;
                transition: all 0.3s ease;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            .stButton > button:hover {
                background-color: #45a049;
            }
            .data-container {
                display: flex;
                justify-content: space-between;
            }
            .data-section {
                background-color: #ffffff;
                border-radius: 5px;
                padding: 15px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    
    def Pandas_doc(self) -> None:
        st.title("Pandas")
        st.markdown("Pandas kütüphanesinin çok kullanışlı bir çok özelliği bulunur. İşte bunlardan bazıları ;\n \
                - Sayısal ve sayısal olmayan verilerinde **eksik verilerin** (NaN olarak temsil edilir) kolay bir şekilde işlenmesi.\n \
                - DataFrame objelerden sütunlar **eklenebilmesi ve silinebilmesi**.\n\
                - Veri kümelerini toplayarak ve dönüştürerek üzerinde bölme-uygulama-birleştirme işlemleri gerçekleştirmek için verileri **gruplaması**.\n\
                - Diğer Python ve NumPy veri yapılarındaki düzensiz, farklı şekillerde indexlenmiş verileri DataFrame nesnelerine **dönüştürmeyi kolaylaştırması**.\n\
                - Akıllı **etiket tabanlı bölümlendirme**, **indeksleme** ve büyük veri kümelerinin **subsetlenmesi**.\n\
                - Veri kümelerinin **birleştirebilmesi**.\n\
                - Excel dosyalarından, veritabanlarından veri yüklemek ve ultra hızlı HDF5 formatından veri kaydetmek/yüklemek için **güçlü IO araçları** olması.\n")
        st.markdown("---")
        st.code("import pandas as pd \nimport numpy as np \n\
                columns = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status', \n\
                        'occupation', 'relationship', 'ethnicity', 'gender','capital_gain', \n\
                        'capital_loss', 'hours_per_week', 'country_of_origin','income'] \n\n\n\
                df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data', names=columns)")

def main() -> None:
    pandas_instance = Pandas()
    pandas_instance.set_background()
    pandas_instance.Pandas_doc()

if __name__ == "__main__":
    main()
