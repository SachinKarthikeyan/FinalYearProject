from operator import index
import streamlit as st
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
import os 

if os.path.exists('./dataset.csv'): 
    df = pd.read_csv('dataset.csv', index_col=None)

with st.sidebar: 
    st.title("Data Preprocessing - EAML Toolkit v 0.1")
    st.divider()
    st.header("Report Generator")
    choice = st.radio("Navigation",["Upload","Report"], captions = ["Load Datasets", "Reports & Exports"], label_visibility="collapsed")
    st.info("Kindly upload your CSV file and then proceed to navigate to 'Report' tab to generate relevant analysis.")
    st.divider()
    st.caption("  Made by :violet[**Amirtha Krishnan**], :blue[**Sachin**] & :green[**Yekanthavasan**] - 2023")

if choice == "Upload":
    st.title("Upload Your Dataset")
    file = st.file_uploader("Upload Your Dataset")
    if file: 
        df = pd.read_csv(file, index_col=None)
        df.to_csv('dataset.csv', index=None)
        st.dataframe(df)

if choice == "Profiling": 
    st.title("Exploratory Data Analysis")
    profile_df = df.profile_report()
    st_profile_report(profile_df)
    export = profile_df.to_html()
    st.download_button(label="Export Report (HTML)", data=export, file_name= filenameholder + "rf.html")

if choice == "Modelling":
    chosen_target = st.selectbox('Choose the Target Column', df.columns)
    if st.button('Run Modelling'):
        setup(df, target=chosen_target, silent=True)
        setup_df = pull()
        st.dataframe(setup_df)
        best_model = compare_models()
        compare_df = pull()
        st.dataframe(compare_df)
        save_model(best_model, 'best_model')

if choice == "Download":
    with open('best_model.pkl', 'rb') as f:
        st.download_button('Download Model', f, file_name="best_model.pkl")