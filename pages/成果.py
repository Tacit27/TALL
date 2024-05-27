import streamlit as st
import pandas as pd
import re

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

# 页面副标题
st.subheader('论著')

# 读取Excel文件
sample_data = pd.read_excel('./成果.xlsx', engine='openpyxl', index_col=0)

# 从论文标题中提取年份
def extract_year(paper):
    match = re.search(r'\b(\d{4})\b', paper)
    if match:
        return int(match.group(1))
    return 9999  # 未定义年份的默认值

# 检查论文是否包含 [J/OL]
def contains_jol(paper):
    return '[J/OL]' in paper

# 检查论文是否为中文
def is_chinese(paper):
    return any('\u4e00' <= char <= '\u9fff' for char in paper)

# 应用函数以提取年份、检查 [J/OL] 和中文
sample_data['year'] = sample_data['paper'].apply(extract_year)
sample_data['contains_jol'] = sample_data['paper'].apply(contains_jol)
sample_data['is_chinese'] = sample_data['paper'].apply(is_chinese)

# 按照年份升序、[J/OL] 升序、中文降序排序数据
sorted_data = sample_data.sort_values(by=['year', 'contains_jol', 'is_chinese'],
                                      ascending=[True, True, False])

# 添加编号列
sorted_data.reset_index(drop=True, inplace=True)
sorted_data.index += 1

# 删除辅助列
sorted_data = sorted_data.drop(columns=['year', 'contains_jol', 'is_chinese'])

sorted_data.rename(columns={'paper': '论文/ paper', 'date': '年度'}, inplace=True)

# 在一个宽的列中放置搜索框和表格
wide_col = st.columns(1)[0]

with wide_col:
    # 搜索功能
    search_query = st.text_input("", placeholder="请输入搜索关键字:")
    if search_query:
        sorted_data = sorted_data[sorted_data['paper'].str.contains(search_query, case=False, na=False)]

    # 显示排序后的数据
    st.dataframe(sorted_data, use_container_width=True)