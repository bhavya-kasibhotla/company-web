import streamlit as st
import pandas
st.set_page_config(layout="wide")
st.header("The Best Company")
st.write(" It’s an opportunity to tell your brand’s story, share your vision or mission, introduce team members, and outline your history and achievements. ")
st.subheader("Our Team")
col1,col2,col3=st.columns(3)
df=pandas.read_csv("data (1).csv")
with col1:
    for index,row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        



with col2:
    for index,row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])

with col3:
    for index,row in df[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
