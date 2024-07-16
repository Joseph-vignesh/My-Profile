import streamlit as st

st.set_page_config(layout="wide")

col1,col2 = st.columns(2)

with col1:
    st.image("images/profile.png")

with col2:
    st.title("Vignesh Baskar")
    content = """Motivated and detail-oriented professional with a strong interest in programming and proficiency in Python. 
                 Excellent problem-solving abilities, effective communication skills, and strong time management. 
                 Demonstrated ability to learn quickly and adapt to new technologies. 
                 Passionate about developing efficient solutions and pursuing a career in full-stack development.
               """

    st.info(content)

content2 = """" Below you can find attached the web apps that i have built feel free to contact me
                """
st.write(content2)
