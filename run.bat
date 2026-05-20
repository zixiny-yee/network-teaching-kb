@echo off
chcp 65001 >nul
title 中学计算机网络知识库

echo ========================================
echo     中学计算机网络知识库 启动中... 作者：zixiny-yee
echo ========================================
echo.
echo 正在加载检索模型和文档，请稍候...
echo 首次启动可能需要 10-15 秒，请耐心等待，长时间没有反应就按一下enter或者关掉再打开哦~
echo.
echo 启动完成后，用浏览器打开 http://localhost:8501
echo.
echo 注意：本窗口请勿关闭！
echo ========================================
echo.

set HTTP_PROXY=
set HTTPS_PROXY=
set NO_PROXY=localhost,127.0.0.1
set OLLAMA_HOST=127.0.0.1:11434

D:
cd D:\TECH\teaching-kb
python -m streamlit run app_minimal.py
pause