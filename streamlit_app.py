import streamlit as st
import google.generativeai as genai

name = st.sidebar.text_input("名前を教えてください")

with st.sidebar:
    st.title("DeVaAI Studio")
   
st.title(f"{name}")
st.write(
    "AIが生成するテキストには誤りが含まれる可能性があります。慎重に利用してください。 "
    "詳しくは[公式サイト](https://project1titan.wordpress.com)をご確認ください."
)
genai.configure(api_key="AIzaSyAyK2A2Ove7VnXEahCBB9SxEPoyLeeVJR0")
if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display the existing chat messages via `st.chat_message`.
for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Create a chat input field to allow the user to enter a message. This will display
    # automatically at the bottom of the page.
if prompt := st.chat_input("ご用件を教えてください"):

        # Store and display the current prompt.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a response using the OpenAI API.
        model = genai.GenerativeModel(model_name='gemini-1.5-flash') 
        response = model.generate_content(prompt)
        assistant_response = response.text
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        with st.chat_message("assistant"):           
             st.write(assistant_response)

