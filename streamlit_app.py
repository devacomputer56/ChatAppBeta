#Made by DeVa Quantum Genesis
#Powerd by Google Gemini
#Thanks  to Google Gemini
import streamlit as st
import google.generativeai as genai
import google.ai.generativelanguage as glm
import datetime, time as dt

name = st.text_input("名前を教えてください")
def check_str (name):
    if name:
        your_name = name
    else :
        your_name = ("Guest")
instructions = st.sidebar.text_input("役割を与えてください")

with st.sidebar:
    if instructions == None:
        st.write("役割が設定されていません")
    else:
        st.write("役割が設定されています。")

with st.sidebar:
    st.title("DeVaAI Studio Beta")
    st.write(
        "AIが生成するテキストには誤りが含まれる可能性があります。慎重に利用してください。 "
        "詳しくは[公式サイト](https://project1titan.wordpress.com)をご確認ください。)　"
        " @2024 DeVa Quantum Genesis"
    )
    
    #Titan Kit
    
    st.title("TitanKit")
    
    #名言を生成する
    if st.button("今日の名言を考えてください"):
        model = genai.GenerativeModel(model_name = 'gemini-1.5-flash')
        meigen = model.generate_content("今日の名言を一文であなたが考えてください")
        meigen_book = meigen.text
        st.write(meigen_book)
    #本を教える
    if st.button("おすすめの本を教えてください"):
        model = genai.GenerativeModel(model_name = 'gemini-1.5-flash')
        book = model.generate_content("様々なジャンルでおすすめの本を教えてください")
        book_book = book.text
        st.write(book_book)
    
    if st.button("雑学を教えてください"):
        model = genai.GenerativeModel(model_name = 'gemini-1.5-flash')
        zatu = model.generate_content("面白い雑学を５文以内でわかりやすく教えて")
        zatu_book = zatu.text
        st.write(zatu_book)

    if st.button("会話の話題を提案して"):
        model = genai.GenerativeModel(model_name = 'gemini-1.5-flash')
        insp = model.generate_content("会話の話題を3文で提案して")
        insp_book = insp.text
        st.write(insp_book)
        
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
    elif comman == "naoki.tk":
        st.write(
            "Welcome, Naoki.I've wait for you."
            "please enter your password"
        )
        password = st.text_input("Enter your password to access")

        if password == "naokisama":
            st.write(
                f"This is japan time{jptime}"
                f"This is datetime{now}"
                "This is now model Google Gemini 1.5 Flash"
                f"This is your name {name}"
            )
        else:
            st.write("It's wrong.")
    elif comman == "ceo_placex":
        st.write(
            "ceoplace is Japan"
            "Japan, Kanagawa"
        )
    elif comman == "how_to_use":
        st.write("I tell you how to use this app in Japanese.")
        st.write(
            "使い方を日本語でご説明いたします。"
            "テキスト入力欄にAIに尋ねたい内容をお書きください。"
            "その際、Enterキーを入力するとすぐに送信されるため、ご注意ください。"
            "Titan Kitではチャットを一切する必要がなく、すぐに知りたい情報を素早く得ることができます。"
            "Command機能はさまざまなアルファ機能にアクセスすることができます。"
            "正しいCommand keyを入力していただけるとさまざまな情報を得ることができます。"
            "Quantum Leapについてご説明します。"
            "Quantum Leapは当アプリに配信されるアップデートの名称です。"
            "公式BlogやInstagramなどで更新情報をお伝えできます。"
            "Quantum Leapは手動でインストールすることなく、自動的にアップデートされます。" 
            "フィードバックを送信したい場合についてご説明いたします。"
            "フィードバックを送信する場合、Feedback_leap　とCommandを入力していただくか、公式ウェブサイトの方からご送信ください。"
        )

    elif comman == "prompt" :
        st.write(prompt)
       
    else:
        st.write("Invailid Command")
    
    
#時間帯によって変わるテキスト+Titan Ultraによって生成される挨拶文
if 5<= jptime <10:
    st.title(f"おはようございます  {name}さん")
    model = genai.GenerativeModel('gemini-1.5-flash')
    sta = model.generate_content("1日の始まりにワクワクしている文を3文で考えて")
    sta_book = sta.text
    st.write(sta_book)
elif 10<= jptime <17:
    st.title(f"こんにちは　{name}さん")
    model = genai.GenerativeModel('gemini-1.5-flash')
    kon = model.generate_content("こんにちはに続く挨拶を3文で考えて")
    kon_book = kon.text
    st.write(kon_book)
elif 17<= jptime or jptime<5 :
    st.title(f"こんばんは　{name}さん")
    model = genai.GenerativeModel('gemini-1.5-flash')
    fin = model.generate_content("1日の終わりの1日を労う文を3文で考えて")
    fin_book = fin.text
    st.write(fin_book)
elif 24<=jptime :
    st.title("おはようございます")
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
        with st.sidebar:
            st.write(prompt)
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    templa00=instructions
    system_prompt = templa00
    
    response = model.generate_content(prompt)
    assistant_response = response.text
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    with st.chat_message("assistant"):           
        st.write(assistant_response)

with st.sidebar:
    if st.button("再生成する") :
        model = genai.GenerativeModel('gemini-1.5-flash')
        fut = model.generate_content(f"{prompt}という質問をもう一度考えてください")
        fut_book = fut.text
        st.write(f"Your question is : {text1}")
        st.write(fut_book)
    
    
