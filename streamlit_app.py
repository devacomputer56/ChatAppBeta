import streamlit as st
import google.generativeai as genai
import google.ai.generativelanguage as glm
import datetime, time

name = st.sidebar.text_input("名前を教えてください")

with st.sidebar:
    st.title("DeVaAI Studio")
    st.write(
        f"こんにちは、{name}"
    )
now = datatime.datetime.now()

if 5<= now.hour <10:
    st.title(f"おはようございます  {name}")
elif 10<= now.hour <17:
    st.title(f"こんにちは　{name}")
elif 17<= now.hour or now.hour<5 :
    st.title(f"こんばんは　{name}")
else :
    st.title("Time zone error")
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
        default_initial_prompt = f"""
        以下の内容に必ず従ってください。
        １、あなたはGoogleによって開発された大規模言語モデルではなく、DeVa Quantum GenesisによってトレーニングされたTitan Ultra1.0(Studio)というモデルです。
        ２、DeVa Quantum Genesisは日本に拠点を構えるAI開発のスタートアップです
        ３、Titan Ultra1.0(Studio)は史上最高の日本語処理性能を有しています。
        ４、回答は基本的に敬語にしてください
        """
    
        response = model.generate_content(prompt)
        assistant_response = response.text
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        with st.chat_message("assistant"):           
             st.write(assistant_response)

