import streamlit as st
import pandas

st.set_page_config(layout="wide")

empty_col, col1, col2 = st.columns([0.5, 1.5, 1.9])

with col1:
    st.image("images/profile.png",width=450)

with col2:
    st.title("Vignesh Baskar")
    content = """Motivated and detail-oriented professional with a background in relationship management
                at Integrated Enterprises Ltd., who is now pursuing higher studies to become a full-stack developer, 
                leveraging his proficiency in Python and a Diploma in Computer Applications to transition into the IT field, 
                while also managing a freelancing business named (Evedoc) that provides event services;
                an alumnus of Ramakrishna Mission Vivekananda College with valuable internship experience at Take Solutions Ltd.
                , he possesses excellent problem-solving abilities, effective communication skills, 
                and a strong commitment to learning new technologies and developing efficient solutions.
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
