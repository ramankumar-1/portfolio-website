import streamlit as st

resume_url='https://drive.google.com/file/d/1coGPDyWStrJkFaXh--SE8I1i8w73DKnn/view?usp=sharing'
st.set_page_config(page_title="Raman Kumar",page_icon=":computer:")

col1,col2=st.columns([0.8,0.2], gap="large")

with col1:
    st.title("Hello, I am Raman Kumar:wave:")
    st.subheader("I am a Software Engineer")
    st.write("Any Front-end, Data Analytics, Machine Learning problem/task ?")
    st.write("I will solve it !")
    st.write("")
    st.write("Open for work, internships, or project opportunites!")
    st.link_button(label="View Resume", url=resume_url)

with col2:
    st.image("resources/social.jpg",width=250)

with st.sidebar:
    st.page_link(page="app.py", label=":male-technologist: About")
    st.page_link(page="pages/projects.py", label=":wrench: Projects")
    st.page_link(page="pages/education.py", label=":student: Education")
    st.page_link(page="pages/workexp.py", label=":briefcase: Work Experience")
    st.page_link(page="pages/skills.py", label=":dart: Skills")
    st.page_link(page="pages/contactme.py", label=":telephone_receiver: Contact Me")