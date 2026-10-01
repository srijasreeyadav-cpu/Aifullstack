import streamlit as st
st.set_page_config(page_title = "Text input Demo")
st.title("text input Demo")
name = st.text_input("Enter your name:", placeholder="e.g. Shana")
st.write(f"Hello,{name}!")
secret = st.text_input("Enter your password:", type="password")
st.write(f"Your password has {len(secret)} characters.")
comments = st.text_area("Any additional comments?,height = 150")
st.write(f"Your wrote {len(comments)} characters.")
show_message = st.checkbox("Do you want an extra message?")
if st.button("submit"):
    st.write("You clicked on submit!")