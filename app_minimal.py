# -*- coding: utf-8 -*-
# 作者：zixiny-yee
# 创建时间：2026年5月
# 联系方式: yeziwquq@m.scnu.edu.cn
# 描述：中学计算机网络知识库 - Web界面

import os
import streamlit as st
from qa_minimal import MiniTeachingKB

# 页面设置
st.set_page_config(
    page_title="中学计算机网络知识库",
    page_icon="🎓",
    layout="wide"
)

@st.cache_resource
def load_kb():
    return MiniTeachingKB()

# ========== 功能1：侧边栏 ==========
with st.sidebar:
    st.markdown("# 🌐")
    st.title("📚 关于本库")
    st.markdown("""
    **中学计算机网络知识库**
    
    一个完全本地运行的智能问答系统，
    适用于中职与高职院校的计算机网络教师，
    辅助备课与课堂教学。
    
    ---
    ### 👩‍🏫 作者信息
    - 作者：zixiny-yee
    - 联系：yeziwquq@m.scnu.edu.cn
    
    ---
    ### 📖 涵盖内容
    - 计算机网络基础
    - TCP/IP协议栈
    - 局域网与广域网
    - 网络安全与信息素养
    - 网络拓扑结构
    - IP地址与子网划分
    
    ---
    ### 📜 版权声明
    © 2026 zixiny-yee 保留所有权利。
    采用 MIT License 协议。
    仅供教学使用，禁止商用。
    
    ---
    ### 🔗 链接
    [GitHub仓库](https://github.com/zixiny-yee/network-teaching-kb)
    """)
    
    st.divider()
    st.caption("💡 提示：在下方对话框输入问题即可查询")

# ========== 主界面 ==========
st.title("🎓 中学计算机网络知识库")
st.caption("完全本地运行 | 智能检索 | 即时回答")

# 初始化知识库
kb = load_kb()

# ========== 功能2：对话历史模式 ==========
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ========== 聊天输入 ==========
if prompt := st.chat_input("请输入你的教学问题..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("正在检索本地知识库..."):
            response = kb.ask(prompt)
        st.write(response)
        
        with st.expander("📄 查看参考来源"):
            docs_list = "\n".join([f"- `{f}`" for f in os.listdir("docs") if f.endswith(('.txt', '.docx', '.pdf'))])
            st.info(f"""
            回答基于以下文档：
            {docs_list}
            
            💡 你可以在 `docs/` 文件夹中添加更多教学文档来扩充知识库。
            """)
    
    st.session_state.messages.append({"role": "assistant", "content": response})