#!/usr/bin/env python3
"""
AI Agent Universe 安装脚本
由 Trae IDE 整合制作
"""

import subprocess
import sys
from pathlib import Path


def check_python_version():
    """检查 Python 版本"""
    if sys.version_info < (3, 10):
        print("❌ 错误：需要 Python 3.10 或更高版本")
        print(f"当前版本：{sys.version_info.major}.{sys.version_info.minor}")
        sys.exit(1)
    print(f"✓ Python 版本检查通过：{sys.version_info.major}.{sys.version_info.minor}")


def create_venv():
    """创建虚拟环境"""
    venv_path = Path("venv")
    if not venv_path.exists():
        print("\n正在创建虚拟环境...")
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✓ 虚拟环境创建成功")
    else:
        print("✓ 虚拟环境已存在")


def install_dependencies():
    """安装依赖"""
    print("\n正在安装依赖...")
    
    # 检测虚拟环境
    if sys.platform == "win32":
        pip_path = Path("venv/Scripts/pip")
    else:
        pip_path = Path("venv/bin/pip")
    
    if pip_path.exists():
        subprocess.run(
            [str(pip_path), "install", "--upgrade", "pip"],
            check=True
        )
        subprocess.run(
            [str(pip_path), "install", "-r", "requirements.txt"],
            check=True
        )
        print("✓ 依赖安装成功")
    else:
        print("⚠ 未找到虚拟环境，使用系统 pip 安装")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
            check=True
        )
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            check=True
        )


def setup_config():
    """设置配置文件"""
    config_example = Path("config.example.yaml")
    config_file = Path("config.yaml")
    
    if config_example.exists() and not config_file.exists():
        print("\n正在创建配置文件...")
        import shutil
        shutil.copy(config_example, config_file)
        print("✓ 配置文件创建成功")
        print("⚠ 请编辑 config.yaml 文件，填入您的 API 密钥等配置")
    elif config_file.exists():
        print("✓ 配置文件已存在")
    else:
        print("⚠ 未找到配置文件示例")


def main():
    """主函数"""
    print("=" * 60)
    print("AI Agent Universe 安装程序")
    print("由 Trae IDE 整合制作")
    print("=" * 60)
    
    # 检查 Python 版本
    check_python_version()
    
    # 创建虚拟环境
    create_venv()
    
    # 安装依赖
    install_dependencies()
    
    # 设置配置文件
    setup_config()
    
    print("\n" + "=" * 60)
    print("✓ 安装完成！")
    print("=" * 60)
    print("\n下一步:")
    print("1. 编辑 config.yaml 文件，配置您的 API 密钥")
    print("2. 运行示例代码：python examples/example_1_basic_agent.py")
    print("3. 查看文档了解更多信息")
    print("\n如有问题，请访问：https://github.com/niuzaisheng/AI-Agent-Universe/issues")
    print("=" * 60)


if __name__ == "__main__":
    main()
