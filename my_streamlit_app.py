import streamlit as st

st.title('Hello Wilders, welcome to my application!')

name = st.text_input("Please give me your name :")
name_length = len(name)
st.write("Your name has ",name_length,"characters")

/Users/Magda/Desktop/migration_test/wild_code_school/my_streamlit_app.py