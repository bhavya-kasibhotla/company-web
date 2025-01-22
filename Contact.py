import streamlit as st
import pandas
from send_email import send_email

df=pandas.read_csv("topics.csv")

with st.form(key="email_form"):
    user_email=st.text_input("enter email address")
    option=st.selectbox("what topic do you want to discuss",
                        df["topic"])
    raw_message=st.text_area("text")
    message=f"""\
Subject:New e-mail from {user_email}\n

From:{user_email}
Topic {option}
{raw_message}"""

    button=st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("e-mail sent successfully")
