import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="mail_form"):
    user_email = st.text_input("Your email address",placeholder="i.e: Vik*d***kj.@gmailcom")
    user_number = st.text_input("Type i n your mobile Number",placeholder="i.e:+91 9*******89")
    raw_message = st.text_area("Cover Your Message Here")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
Number: {user_number}
{raw_message}
 """
    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info("Your email was sent successfully")
