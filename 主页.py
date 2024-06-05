import streamlit as st
import streamlit.components.v1 as components
from streamlit_carousel import carousel
import time

sidebar_logo = "images/logo.png"
st.sidebar.image(sidebar_logo, use_column_width=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.page_link("主页.py", label="主页", icon="🏠")
with col2:
    st.page_link("pages/成员.py", label="成员", icon="🧑‍💻")
with col3:
    st.page_link("pages/成果.py", label="成果", icon="📑")
with col4:
    st.page_link("pages/实验室招生.py", label="实验室招生", icon="🔥")

st.title('TALL')
st.subheader("Taike Artificial inteLligence Lab", divider='rainbow')
st.write('TALL隶属于南京理工大学泰州科技学院计算机科学与工程学院，负责人为姜枫教授。"TALL" 的全称是"Taike Artificial InteLligence Laboratory（泰科人工智能实验室）"。TALL的主要研究兴趣包括机器学习、模式识别、计算机视觉、自然语言处理等领域。TALL面向本校常年招纳优秀学子，为本科生提供系统的科研训练，如果您希望加入我们或希望在TALL做本科毕业设计请与请与实验室老师联系。')

st.image('images/主页图.jpg')
