import streamlit as st
import pandas

st.set_page_config(layout="wide")

empty_col, col1, col2 = st.columns([0.5, 1.5, 1.9])

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
st.subheader(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
