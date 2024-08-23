#Made by DeVa Quantum Genesis
#Powerd by Google Gemini
#Thanks  to Google Gemini
import streamlit as st
import google.generativeai as genai
import google.ai.generativelanguage as glm
import datetime, time as dt


name = st.sidebar.text_input("名前を教えてください")
instructions = st.sidebar.text_input("役割を与えてください")

with st.sidebar:
    st.title("DeVaAI Studio")
    st.write(
        "AIが生成するテキストには誤りが含まれる可能性があります。慎重に利用してください。 "
        "詳しくは[公式サイト](https://project1titan.wordpress.com)をご確認ください。)　"
        " @2024 DeVa Quantum Genesis"
    )
    
    #Titan Kit
    
    st.title("TitanKit")
    
    #名言を生成する
    if st.button("今日の名言を考えて"):
        model = genai.GenerativeModel(model_name = 'gemini-1.5-flash')
        meigen = model.generate_content("今日の名言を一文であなたが考えてください")
        meigen_book = meigen.text
        st.write(meigen_book)
    #本を教える
    if st.button("おすすめの本を教えて"):
        model = genai.GenerativeModel(model_name = 'gemini-1.5-flash')
        book = model.generate_content("様々なジャンルでおすすめの本を教えてください")
        book_book = book.text
        st.write(book_book)
    
    if st.button("雑学を教えて"):
        model = genai.GenerativeModel(model_name = 'gemini-1.5-flash')
        zatu = model.generate_content("面白い雑学を５文以内でわかりやすく教えて")
        zatu_book = zatu.text
        st.write(zatu_book)

    st.title("Command")
now = datetime.datetime.now()
jptime = now.hour + 9

#Command動作 
comman = st.sidebar.text_input("Input command")
with st.sidebar:
    if comman == "datetime":
        st.write(jptime)
        st.write(now)
    elif comman == "company":
        st.write("@2024 DeVa Quantum Genesis")
    elif comman == "home_page":
        st.write("[開く](https://project1titan.wordpress.com))")
    elif comman == "naokitk":
        st.write(
            "Welcome, Naoki.I've wait for you."
        )
    else:
        st.write("Invailid Command")
    
#Titan Ultra　会話のインスピレーションを得る
if st.button("インスピレーションを得る"):
    model = genai.GenerativeModel('gemini-1.5-flash')
    insp = model.generate_content("会話の話題を3文で考えて")
    insp_book = insp.text
    st.write(insp_book)
    
#時間帯によって変わるテキスト+Titan Ultraによって生成される挨拶文
if 5<= jptime <10:
    st.title(f"おはようございます  {name}")
    model = genai.GenerativeModel('gemini-1.5-flash')
    sta = model.generate_content("1日の始まりにワクワクしている文を3文で考えて")
    sta_book = sta.text
    st.write(star_book)
elif 10<= jptime <17:
    st.title(f"こんにちは　{name}")
    model = genai.GenerativeModel('gemini-1.5-flash')
    kon = model.generate_content("こんにちはに続く挨拶を3文で考えて")
    kon_book = kon.text
    st.write(kon_book)
elif 17<= jptime or jptime<5 :
    st.title(f"こんばんは　{name}")
    model = genai.GenerativeModel('gemini-1.5-flash')
    fin = model.generate_content("1日の終わりの1日を労う文を3文で考えて")
    fin_book = fin.text
    st.write(fin_book)
else :
    st.title("Time zone error")

genai.configure(api_key="AIzaSyAyK2A2Ove7VnXEahCBB9SxEPoyLeeVJR0")
if "messages" not in st.session_state:
    st.session_state.messages = []

    # Display the existing chat messages via `st.chat_message`.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("ご用件を教えてください"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
    model = genai.GenerativeModel('gemini-1.5-flash')
    templa00=instructions
    system_prompt = templa00
    
    response = model.generate_content(prompt)
    assistant_response = response.text
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    with st.chat_message("assistant"):           
        st.write(assistant_response)
