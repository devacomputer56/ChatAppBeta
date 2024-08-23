import streamlit as st
import google.generativeai as genai
import google.ai.generativelanguage as glm
import datetime, time as dt

name = st.sidebar.text_input("名前を教えてください")
instructions = st.sidebar.text_input("チャットの指示を与えてください")

with st.sidebar:
    st.title("DeVaAI Studio")
    st.write(
        "AIが生成するテキストには誤りが含まれる可能性があります。慎重に利用してください。 "
        "詳しくは[公式サイト](https://project1titan.wordpress.com)をご確認ください。　"
        " @2024 DeVa Quantum Genesis"
    )
    
    st.title("TitanKit")
    if st.button("今日の名言を考えます"):
        model = genai.GenerativeModel(model_name = 'gemini-1.5-flash')
        meigen = model.generate_content("今日の名言を一文であなたが考えてください")
        meigen_book = meigen.text
        st.write(meigen_book)
    if st.button("公式ページのリンク"):
        st.write("[開く](https://project1titan.wordpress.com)")
    if st.button("おすすめの本を教えます"):
        model = genai.GenerativeModel(model_name = 'gemini-1.5-flash')
        book = model.generate_content("様々なジャンルでおすすめの本を教えてください")
        book_book = book.text
        st.write(book_book)


if st.button("インスピレーションを得る"):
    model = genai.GenerativeModel('gemini-1.5-flash')
    insp = model.generate_content("会話の話題を3文で考えて")
    insp_book = insp.text
    st.write(insp_book)

    now = datetime.datetime.now()
    jptime = now.hour + 9
    
    if 5<= jptime <10:
        st.title(f"おはようございます  {name}")
        st.write(
        "今日はどんな一日となりそうですか？"
        )
    elif 10<= jptime <17:
        st.title(f"こんにちは　{name}")
        st.write(
        "お会いできて嬉しいです"
        )
    elif 17<= jptime or jptime<5 :
        st.title(f"こんばんは　{name}")
        st.write(
        "今日はどんな1日でしたか？"
        )
    else :
        st.title("Time zone error")

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
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a response using the OpenAI API.
        model = genai.GenerativeModel(
            "gemini-1.5-flash",
            system_instruction=[
                instructions
            ],
        )

    
        response = model.generate_content(prompt)
        assistant_response = response.text
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        with st.chat_message("assistant"):           
             st.write(assistant_response)
