@echo off
REM AI Agent Universe Windows 快速安装脚本
REM 由 Trae IDE 整合制作

echo ============================================================
echo AI Agent Universe Windows 安装程序
echo 由 Trae IDE 整合制作
echo ============================================================

REM 检查 Python 版本
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未检测到 Python，请先安装 Python 3.10+
    pause
    exit /b 1
)

echo [✓] Python 已安装

REM 创建虚拟环境
if not exist "venv" (
    echo.
    echo 正在创建虚拟环境...
    python -m venv venv
    echo [✓] 虚拟环境创建成功
) else (
    echo [✓] 虚拟环境已存在
)

REM 激活虚拟环境
echo.
echo 正在激活虚拟环境...
call venv\Scripts\activate.bat

REM 升级 pip
echo.
echo 正在升级 pip...
python -m pip install --upgrade pip

REM 安装依赖
echo.
echo 正在安装依赖...
pip install -r requirements.txt

REM 复制配置文件
if not exist "config.yaml" (
    echo.
    echo 正在创建配置文件...
    copy config.example.yaml config.yaml
    echo [✓] 配置文件创建成功
) else (
    echo [✓] 配置文件已存在
)

echo.
echo ============================================================
echo ✓ 安装完成!
echo ============================================================
echo.
echo 下一步:
echo 1. 编辑 config.yaml 文件，配置您的 API 密钥
echo 2. 运行示例代码：python examples\example_1_basic_agent.py
echo 3. 查看文档了解更多信息
echo.
echo 如有问题，请访问：https://github.com/niuzaisheng/AI-Agent-Universe/issues
echo ============================================================
echo.
pause
