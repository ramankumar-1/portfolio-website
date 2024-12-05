import streamlit as st

st.set_page_config(page_title="Raman Kumar",page_icon=":computer:")

st.title("Where I had worked till now?")
st.divider()

st.image("resources/tcs-logo.png", width=250)
st.code('''{"Organization": "Tata Consultancy Services Limited",
 "Role" : "System Engineer",
 "Location" : "Mumbai, India",
 "When"   : "July 2024 - Now"}''',language="json5")

with st.sidebar:
    st.page_link(page="app.py", label=":male-technologist: About")
    st.page_link(page="pages/projects.py", label=":wrench: Projects")
    st.page_link(page="pages/education.py", label=":student: Education")
    st.page_link(page="pages/workexp.py", label=":briefcase: Work Experience")
    st.page_link(page="pages/skills.py", label=":dart: Skills")
    st.page_link(page="pages/contactme.py", label=":telephone_receiver: Contact Me")