import streamlit as st

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


st.subheader('实验室招生', divider='rainbow')

st.write('TALL实验室致力于前沿技术的研究与创新。研究方向覆盖了机器学习、计算机视觉、自然语言处理、机器人技术等多个领域。目前实验室与上海交通大学，南京大学，南京理工大学，西交利物浦大学等有紧密的科研合作。')
st.write('TALL面向本校常年招纳优秀学子，为本科生提供系统的科研训练。如果您希望加入我们从事科学研究工作或从事AI方向的本科毕业，请与实验室老师联系（jf@nustti.edu.cn，zhipengye@nustti.edu.cn）。')
st.write('以下是实验室的福利和要求。')

st.subheader('福利🎁')

st.markdown("""
1. 提供实验室的独立工位，实验室配有6*4090显卡的超算服务器资源。
2. 提供手把手的科研指导和科研训练。
3. 表现优秀者，可参加国际学术会议，并发表SCI/CCF类论文。
4. 表现优秀者，可推荐申请校级奖学金项目和优秀毕业生。
5. 表现优秀者，可推荐到国内外知名大学攻读硕博士和研究机构（微软、华为）工作。
""")

st.subheader('要求💻')

st.markdown("""
1. 熟悉Python编程能力，擅长解决问题。
2. 熟悉PyTorch深度学习框架。
3. 对科研具有较强的热情，自我驱动。
4. 服从实验室制度。
5. 如果你是大一/大二学生， 对科研具有较强的热情，自我驱动。也可以主动联系我们，我们会安排学习计划和对应人才培养。
""")

st.subheader('欢迎大家，加入我们TALL实验室!🥳')
