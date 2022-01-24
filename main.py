import streamlit as st
import pickle
#import numpy as np
import pandas as pd
df = pickle.load(open('df.pkl','rb'))
st.header("Import Products")
st.subheader("Step 1: ")
data_file = st.file_uploader("Select file")
if st.button("Process"):
    if data_file is not None:
        file_details = {"Filename": data_file.name, "FileType": data_file.type, "FileSize": data_file.size}
        st.write(file_details)
        df = pd.read_csv(data_file)

    st.subheader("Step 2: ")

    st.markdown("Specify format")
    file_type = st.selectbox(
    'File Type : ',
    ('csv', 'xlsx', 'doc'))
    character_encoding = st.selectbox(
    'Character Encoding : ',
    ('UTF-8', 'UTF-16', 'UTF-32'))
    delimiter = st.selectbox(
    'Delimiter : ',
    ('comma', 'space', 'semicolon'))
    header1 = st.checkbox('Has Header',value=True)

    if header1:
        st.subheader("Step 3: ")
        st.write('Display Handling')
        st.write('Select the fields to be displayed')
        col1,col2,col3=st.columns(3)
        with col1:
            st.markdown("***Available Fields***")
            container = st.container()
            container.text("Product Id")
            container.text("title")
            container.text("Price")
            container.text("Popularity")
            container.text("Description")
            container.text("Rating")
            container.text("UTM Source")
            container.text("UTM Medium")

        with col2:
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.button(">>")

            st.button("<<")

        with col3:
            st.markdown("***Fields to be displayed***")
            container2 = st.container()
            container2.write("Product Id")
    st.dataframe(df)