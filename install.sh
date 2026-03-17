#!/bin/bash
# AI Agent Universe Linux/Mac 快速安装脚本
# 由 Trae IDE 整合制作

echo "============================================================"
echo "AI Agent Universe 安装程序"
echo "由 Trae IDE 整合制作"
echo "============================================================"

# 检查 Python 版本
if ! command -v python3 &> /dev/null; then
    echo "[错误] 未检测到 Python3，请先安装 Python 3.10+"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
REQUIRED_VERSION="3.10"

echo "[✓] Python 已安装：$PYTHON_VERSION"

# 创建虚拟环境
if [ ! -d "venv" ]; then
    echo ""
    echo "正在创建虚拟环境..."
    python3 -m venv venv
    echo "[✓] 虚拟环境创建成功"
else
    echo "[✓] 虚拟环境已存在"
fi

# 激活虚拟环境
echo ""
echo "正在激活虚拟环境..."
source venv/bin/activate

# 升级 pip
echo ""
echo "正在升级 pip..."
python -m pip install --upgrade pip

# 安装依赖
echo ""
echo "正在安装依赖..."
pip install -r requirements.txt

# 复制配置文件
if [ ! -f "config.yaml" ]; then
    echo ""
    echo "正在创建配置文件..."
    cp config.example.yaml config.yaml
    echo "[✓] 配置文件创建成功"
else
    echo "[✓] 配置文件已存在"
fi

echo ""
echo "============================================================"
echo "✓ 安装完成!"
echo "============================================================"
echo ""
echo "下一步:"
echo "1. 编辑 config.yaml 文件，配置您的 API 密钥"
echo "2. 运行示例代码：python examples/example_1_basic_agent.py"
echo "3. 查看文档了解更多信息"
echo ""
echo "如有问题，请访问：https://github.com/niuzaisheng/AI-Agent-Universe/issues"
echo "============================================================"
