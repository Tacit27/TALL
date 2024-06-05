import streamlit as st

sidebar_logo = "images/logo.png"
st.sidebar.image(sidebar_logo, use_column_width=True)

# 创建四个并排的列，用于导航链接
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.page_link("主页.py", label="主页", icon="🏠")
with col2:
    st.page_link("pages/成员.py", label="成员", icon="🧑‍💻")
with col3:
    st.page_link("pages/成果.py", label="成果", icon="📑")
with col4:
    st.page_link("pages/实验室招生.py", label="实验室招生", icon="🔥")

# 页面标题
st.header('教师信息')

# 人员信息列表
persons = [
    {
        "姓名": "姜枫",
        "职称": "教授",
        "邮箱": "jf@nustti.edu.cn",
        "办公室": "敏行楼A403",
        "研究方向": "计算机视觉、多模态技术、机器学习等",
        "简历": "",
        "图片": "images/JiangFeng.jpg"
    },{
        "姓名": "叶志鹏",
        "职称": "助教",
        "邮箱": "zhipengye@nustti.edu.cn",
        "办公室": "敏行楼A401",
        "研究方向": "计算机视觉、多模态技术、机器学习等",
        "简历": "",
        "图片": "images/YeZhipeng.jpg"
    },
]

# 遍历人员信息并展示
for person in persons:
    col1, col2 = st.columns([1, 3])

    with col1:
        st.image(person["图片"])

    with col2:
        st.subheader(person['姓名'])
        st.write(f"职称：{person['职称']}")
        st.write(f"邮箱：{person['邮箱']}")
        st.write(f"办公室：{person['办公室']}")
        st.write(f"研究方向：{person['研究方向']}")

    # 在每一个人物名片下方添加灰色分割线
    st.markdown("<hr style='color:grey;'>", unsafe_allow_html=True)


st.header('实验室学生信息')
st.subheader('往届学生')
persons = [
    {
        "姓名": "乔一鸣",
        "入学年份": "2024届",
        "专业": "软件工程",
        "研究方向": "深度学习",
        "去向": "莫纳什大学",
        "简介": "1、第十八届挑战杯学术作品竞赛省三等奖。2、发表省级期刊一篇。3、校一等奖学金。4、2024届优秀毕业生。",
        "图片": "images/QiaoYiming.jpg"
    },{
        "姓名": "汤可",
        "入学年份": "2024届",
        "专业": "信息管理与信息系统",
        "研究方向": "深度学习",
        "去向": "湖北大学",
        "简介": "1、第十八届挑战杯学术作品竞赛省三等奖。2、发表省级期刊一篇。3、校一等奖学金。4、2024届优秀毕业生。",
        "图片": "images/TangKe.jpg"
    },{
        "姓名": "王政豪",
        "入学年份": "2024届",
        "专业": "计算机科学与技术",
        "研究方向": "深度学习",
        "去向": "待定",
        "简介": "1、发表CCF-C国际学术论文一篇。2、第十八届挑战杯学术作品竞赛省三等奖。3、校一等奖学金。4、2024届优秀毕业生。",
        "图片": "images/WangZhenhao.jpg"
    }
]

# 遍历人员信息并展示
for person in persons:
    col1, col2 = st.columns([1, 3])

    with col1:
        st.image(person["图片"])

    with col2:
        st.subheader(person['姓名'])
        st.write(person['入学年份'])
        st.write(f"专业：{person['专业']}")
        st.write(f"研究方向：{person['研究方向']}")
        st.write(f"去向：{person['去向']}")
        st.write(f"简介：{person['简介']}")

    # 在每一个人物名片下方添加灰色分割线
    st.markdown("<hr style='color:grey;'>", unsafe_allow_html=True)


st.subheader('在读学生')

persons = [
    {
        "姓名": "杨博成",
        "入学年份": "2021级",
        "专业": "信息管理与信息系统",
        "研究方向": "AIGC detection",
        "简介": "一个不会写简介的人",
        "图片": "images/YangBocheng.jpg"
    },{
        "姓名": "郭林艳",
        "入学年份": "2021级",
        "专业": "信息管理与信息系统",
        "研究方向": "AIGC detection",
        "简介": "",
        "图片": "images/GuoLinyan.jpg"
    },{
        "姓名": "王银平",
        "入学年份": "2021级",
        "专业": "信息管理与信息系统",
        "研究方向": "计算机视觉",
        "简介": "1、国家励志奖学金。2、校一等奖学金",
        "图片": "images/WangYinping.jpg"
    },{
        "姓名": "钱心悦",
        "入学年份": "2021级",
        "专业": "计算机科学与技术",
        "研究方向": "语义分割",
        "简介": "1、第二届“华数杯”国际大学生数学建模H奖。2、2024年美赛MCM/ICM S奖。3、校奖学金二等奖。",
        "图片": "images/QianXinyue.jpg"
    },{
        "姓名": "吕翰杰",
        "入学年份": "2023级",
        "专业": "计算机科学与技术",
        "研究方向": "AI深度学习",
        "简介": "1、2024团体程序设计天梯赛团队三等奖。",
        "图片": "images/LvHanjie.jpg"
    },{
        "姓名": "于智钧",
        "入学年份": "2023级",
        "专业": "计算机科学与技术",
        "研究方向": "计算机视觉",
        "简介": "",
        "图片": "images/YuZhijun.jpg"
    },{
        "姓名": "潘可欣",
        "入学年份": "2023级",
        "专业": "计算机科学与技术",
        "研究方向": "计算机视觉",
        "简介": "1、校一等奖学金",
        "图片": "images/PanKexin.jpg"
    }
]

# 遍历人员信息并展示
for person in persons:
    col1, col2 = st.columns([1, 3])

    with col1:
        st.image(person["图片"])

    with col2:
        st.subheader(person['姓名'])
        st.write(person['入学年份'])
        st.write(f"专业：{person['专业']}")
        st.write(f"研究方向：{person['研究方向']}")
        st.write(f"简介：{person['简介']}")

    # 在每一个人物名片下方添加灰色分割线
    st.markdown("<hr style='color:grey;'>", unsafe_allow_html=True)
