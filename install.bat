@echo off
chcp 65001 >nul
title 中学计算机网络知识库 - 一键安装
echo ========================================
echo   中学计算机网络知识库 - 安装程序
echo ========================================
echo.

:: 安装 Python
echo [1/3] 正在安装 Python...
if exist "python-3.11.2-amd64.exe" (
    python-3.11.2-amd64.exe /quiet InstallAllUsers=1 PrependPath=1
    echo Python 安装完成。
) else (
    echo 未找到 Python 安装包，请确保 python-3.11.2-amd64.exe 在本文件夹内。
    pause
    exit
)
echo.

:: 安装 Ollama
echo [2/3] 正在打开 Ollama 下载页面...
echo 请下载后双击安装，一路点"下一步"即可。
echo 安装完成后，回到这里按任意键继续...
start https://ollama.com/download/windows
pause

echo 正在下载问答模型（约 400MB，请耐心等待）...
ollama pull qwen2:0.5b
echo 模型下载完成。
echo.

:: 安装 Python 依赖
echo [3/3] 正在安装 Python 依赖包...
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
echo 依赖包安装完成。
echo.

echo ========================================
echo   安装完成！双击 run.bat 启动知识库。
echo ========================================
pause