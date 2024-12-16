from langchain_openai import ChatOpenAI
import streamlit as st

#chat_model = ChatOpenAI(api_key=OPENAI_API_KEY, model_name="gpt-3.5-turbo")
chat_model = ChatOpenAI(model_name="gpt-3.5-turbo")

st.title('AI 작사가')

content = st.text_input('작사할 주제를 제시해주세요.')
# 윗 부분은 동일함. 아래 부부만 코드 변경
if st.button('작사 요청하기'):
    with st.spinner('노래 가사 작성 중입니다...'):
        result = chat_model.invoke(content + "에 대한 노래의 작사를 해 줘")
        st.write(result.content)
