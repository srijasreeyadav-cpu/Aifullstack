from ollama import chat
import streamlit as st

st.set_page_config(page_title="LlamaBot App", page_icon="🤖")

st.title("LlamaBot - Here to talk!")

personality = """
You are a friendly and patient tutor named Llama.
Answer warmly and keep the answers within one sentence.
"""
personality

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = [
        {"role": "system", "content": personality}
    ]

# Welcome message
with st.chat_message("assistant"):
    st.write("Hello! I'm Llama. Ask something to get started.")

# Display previous messages
for msg in st.session_state.history[1:]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Get user input
question = st.chat_input("Type something...")

if question:
    # Add user's question to history
    st.session_state.history.append(
        {"role": "user", "content": question}
    )

    # Get response from Ollama
    response = chat(
        model="llama3.2",
        messages=st.session_state.history
    )

    reply = response["message"]["content"]

    # Add assistant response to history
    st.session_state.history.append(
        {"role": "assistant", "content": reply}
    )
    with st.sidebar:
        st.header("chat controls")
        st.button("clear chat",type="primary")
        st.button("change personality")

    # Display assistant response
    with st.chat_message("assistant"):
        st.write(reply)