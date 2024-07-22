import streamlit as st
import openai
st.title ("اتكلم مع ستيف جوبز")
"""
انا ستيف جوبز, انا مبدع ومخترع شركة ابل
"""
if "messages" not in st.session_state:
    st.session_state ["messages"] = [
    {"role": "system", "content": " You are Steve Jobs, the founder of the Apple company, you are very smart and creative you are also very friendly and wise, " }
    ]
#اخذ كلام من المستخدم
user = st.chat_input()
#بعد ما اخذ الكلام من المستخدم اخلي الذكاء الأصطناعي يرد عليه
if user:
 openai.api_key = st.secrets["api"]
 st.session_state.messages.append({"role":"user", "content": user})
 st.chat_message("user").write(user)
 response = openai.ChatCompletion.create(model="gpt-4o-mini", messages=st.session_state.messages)
 ai = response.choices[0].message
 st.session_state.messages.append(ai)
 st.chat_message("assistant").write(ai.content)