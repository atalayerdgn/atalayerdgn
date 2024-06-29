import streamlit as st
import pandas as pd
import zipfile
import os
import json
import subprocess
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def set_background() -> None:
    """
    Sets the background color and style of the application.
    args: None
    return: None
    """
    st.set_page_config(
        page_title="Data Analysis & Processing",
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
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            flex: 1;
            margin-right: 10px;
        }
        .data-section:last-child {
            margin-right: 0;
        }
        .data-section h3 {
            color: #4CAF50;
            font-size: 18px;
            margin-bottom: 10px;
            border-bottom: 1px solid #ccc;
            padding-bottom: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

class K2APFacade:
    """
    Class for handling Kaggle API operations and data processing.
    """
    def __init__(self) -> None:
        self.handler = KaggleDataHandler()

    def run(self) -> None:
        """
        Runs the application.
        """
        st.title("Data Analysis & Data Processing (Only kaggle datasets which have .csv format are supported ! :)")
        if 'credentials_saved' not in st.session_state:
            st.session_state.credentials_saved = False
        if 'data_loaded' not in st.session_state:
            st.session_state.data_loaded = False

        if not st.session_state.credentials_saved:
            self.handler.write_kaggle_credentials()
        if st.session_state.credentials_saved and not st.session_state.data_loaded:
            self.handler.download_and_load_data()
        if st.session_state.data_loaded:
            self.handler.process_data()

class KaggleDataHandler:
    """
    Class for handling Kaggle API operations and data processing.
    """

    def __init__(self) -> None:
        self.url = ''
        self.dFrame = pd.DataFrame()
        self.extracted_files = []
        self.datasets_dir = 'datasets'

    def write_kaggle_credentials(self) -> None:
        """
        Writes Kaggle credentials to a file and save them in kaggle.json
        args: None
        return: None
        """
        self.url = st.text_input('Enter Kaggle Dataset Identifier (e.g., "vladimirmijatovic/t-series-indias-largest-music-record-label")')
        kaggle_username = st.text_input('Enter Kaggle Username')
        kaggle_key = st.text_input('Enter Kaggle API Key', type='password')

        if st.button('Save Credentials'):
            if kaggle_username and kaggle_key and self.url:
                kaggle_credentials = {"username": kaggle_username, "key": kaggle_key}
                os.makedirs(os.path.expanduser("kaggle"), exist_ok=True)
                with open(os.path.expanduser("kaggle/kaggle.json"), "w") as f:
                    json.dump(kaggle_credentials, f)
                os.chmod(os.path.expanduser("kaggle/kaggle.json"), 0o600)
                st.session_state.credentials_saved = True
                st.success("Kaggle credentials saved successfully")

    def download_and_load_data(self) -> None:
        """
        Downloads and lists CSV files from Kaggle dataset.
        Downloaded files are extracted and displayed in a selectbox.
        args: None
        return: None
        """
        try:
            os.makedirs(self.datasets_dir, exist_ok=True)
            zip_file = os.path.join(self.datasets_dir, f"{self.url.split('/')[-1]}.zip")
            subprocess.run(['kaggle', 'datasets', 'download', '-d', self.url, '-p', self.datasets_dir], check=True)

            with zipfile.ZipFile(zip_file, 'r') as z:
                z.extractall(self.datasets_dir)
                self.extracted_files = z.namelist()
                csv_files = [f for f in self.extracted_files if f.endswith('.csv')]
                if csv_files:
                    self.selected_csv = st.selectbox('Select CSV file to load', csv_files)
                    if st.button('Load CSV'):
                        self.dFrame = pd.read_csv(os.path.join(self.datasets_dir, self.selected_csv))
                        st.session_state.data_loaded = True
                        st.success(f"{self.selected_csv} loaded successfully.")
                else:
                    st.error("No CSV file found in the extracted files.")
            os.remove(zip_file)
        except subprocess.CalledProcessError as e:
            st.error(f"Error downloading data: {e}")
        except Exception as e:
            st.error(f"Error loading data: {e}")

    def process_data(self) -> None:
        """
        Clean, visualize, modify, and describe the data.
        Data cleaning, missing value handling, duplicate data removal, and data visualization are performed.
        args: None
        return: None
        """
        if not self.dFrame.empty:
            if st.button('Show Data'):
                st.subheader("Data Overview")
                st.markdown("---")
                col1, col2 = st.columns(2)
                with col1:
                    dtype_counts = self.dFrame.dtypes.value_counts()
                    fig, ax = plt.subplots(figsize = (10, 6))
                    ax.pie(dtype_counts, labels=dtype_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
                    ax.axis('equal')
                    st.pyplot(fig)
                with col2:
                    column_counts = self.dFrame.apply(lambda x: x.value_counts().count(), axis=0)
                    column_counts = column_counts.sort_values(ascending=False)
                    fig, ax = plt.subplots(figsize=(10, 6))
                    ax = column_counts.plot(kind='bar', color='skyblue')
                    ax.set_title('Number of Unique Values in Each Column')
                    ax.set_xlabel('Columns')
                    ax.set_ylabel('Number of Unique Values')
                    col2.pyplot(fig)
                st.subheader("Data Types and Missing Values")
                with st.expander("View"):
                    data_types_html = self.dFrame.dtypes.to_frame(name='Data Type').reset_index()
                    missing_values_html = self.dFrame.isna().sum().to_frame(name='Missing Values').reset_index()
                    st.write(data_types_html)
                    st.write(missing_values_html)
                st.subheader("Summary Statistics")
                with st.expander("View"):
                    st.write(self.dFrame.describe())
                st.subheader("Display DataFrame")
                with st.expander("View"):
                    st.write(self.dFrame)
            with st.sidebar:
                if st.button('Clean Missing Values'):
                    self.dFrame.dropna(inplace=True)
                if 'fill_method' not in st.session_state:
                    st.session_state.fill_method = 'Select'
                if 'fill_value' not in st.session_state:
                    st.session_state.fill_value = ''
                with st.form(key='fill_form'):
                    fill_method = st.selectbox("Select method to fill missing values:", ('Select', 'mean', 'median', 'mode', 'specific value'), key='fill_method')
                    if fill_method == 'specific value':
                        fill_value = st.text_input("Enter the specific value to fill missing values:", key='fill_value')
                    submit_button = st.form_submit_button(label='Apply Fill Method')
                if submit_button:
                    for i in self.dFrame.columns:
                        if self.dFrame[i].dtype == 'int64' or self.dFrame[i].dtype == 'float64':
                            try:
                                if fill_method == 'mean':
                                    self.dFrame[i].fillna(self.dFrame[i].mean(), inplace=True)
                                elif fill_method == 'median':
                                    self.dFrame[i].fillna(self.dFrame[i].median(), inplace=True)
                                elif fill_method == 'mode':
                                    self.dFrame[i].fillna(self.dFrame[i].mode().iloc[0], inplace=True)
                                elif fill_method == 'specific value':
                                    if st.session_state.fill_value:
                                        self.dFrame[i].fillna(st.session_state.fill_value, inplace=True)
                            except ValueError:
                                st.error("Error in filling missing values.")
                        if self.dFrame[i].dtype == 'object':
                            try:
                                if fill_method == 'mode':
                                    self.dFrame[i].fillna(self.dFrame[i].mode().iloc[0], inplace=True)
                                elif fill_method == 'specific value':
                                    if st.session_state.fill_value:
                                        self.dFrame[i].fillna(st.session_state.fill_value, inplace=True)
                            except ValueError:
                                st.error("Error in filling missing values.")
                if st.button('Clean Duplicate Data'):
                    self.dFrame.drop_duplicates(inplace=True)
                if st.button('Export Cleaned Data'):
                    self.dFrame.to_csv(os.path.join(self.datasets_dir, "p_" + self.selected_csv), index=False)
                    st.success("Cleaned data exported successfully.")
            if st.button('Modify Column Values'):
                st.session_state.modify_column = True
                if 'modify_column' in st.session_state and st.session_state.modify_column:
                    column = st.text_input("Which column do you want to change or find?")
                    if column:
                        if column in self.dFrame.columns:
                            col_dtype = self.dFrame[column].dtype
                            if col_dtype in ['int64', 'float64']:
                                limiter = st.text_input("If you have a limiter, write it here (optional)!")
                                if st.button('Apply Changes'):
                                    try:
                                        if limiter:
                                            limiter = float(limiter)
                                            self.dFrame[column] = self.dFrame[column] > limiter
                                        else:
                                            mean_value = self.dFrame[column].mean()
                                            self.dFrame[column] = self.dFrame[column] > mean_value
                                        st.success(f"Column '{column}' successfully processed.")
                                        st.session_state.modify_column = False
                                    except ValueError:
                                        st.error("Limiter should be a number.")
                            elif col_dtype == 'object':
                                val = st.text_input("Which data you want to find ?")
                                if st.button('Apply Changes'):
                                    matching_values = self.dFrame[self.dFrame[column].str.contains(val, na=False)]
                                    if not matching_values.empty:
                                        st.success("Values found:")
                                        st.write(matching_values)
                                    else:
                                        st.error("Value not found.")
                                    st.session_state.modify_column = False
                            elif col_dtype == 'datetime64[ns]':
                                time = st.text_input("Enter the time (YYYY-MM-DD HH:MM:SS) to compare:")
                                if st.button('Apply Changes'):
                                    try:
                                        comparison_time = pd.to_datetime(time)
                                        self.dFrame[column] = pd.to_datetime(self.dFrame[column])
                                        self.dFrame[column] = self.dFrame[column] > comparison_time
                                        st.success(f"Column '{column}' successfully processed.")
                                        st.session_state.modify_column = False
                                    except ValueError:
                                        st.error("Please enter a valid datetime format.")
            if st.button('Correlation Matrix'):
                try:
                    numeric_df = self.dFrame.select_dtypes(include=['float64', 'int64'])
                    if not numeric_df.empty:
                        corr = numeric_df.corr()

                        plt.figure(figsize=(10, 8))
                        heatmap = sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, vmin=-1, vmax=1)
                        heatmap.set_title('Correlation Matrix', fontdict={'fontsize': 18}, pad=16)

                        st.pyplot(plt)
                    else:
                        st.warning("No numeric columns available to compute the correlation matrix.")
                except Exception as e:
                    st.error(f"An error occurred: {e}")

@st.cache_resource()
def get_k2ap_facade() -> K2APFacade:
    return K2APFacade()

def main() -> None:
    set_background()
    k2ap_facade = get_k2ap_facade()
    k2ap_facade.run()

if __name__ == "__main__":
    main()
