# 快速开始指南

## 安装

### Windows

1. 运行安装脚本：
```bash
install.bat
```

2. 激活虚拟环境：
```bash
venv\Scripts\activate
```

### Linux/Mac

1. 运行安装脚本：
```bash
bash install.sh
```

2. 激活虚拟环境：
```bash
source venv/bin/activate
```

### 手动安装

```bash
# 克隆仓库
git clone https://github.com/niuzaisheng/AI-Agent-Universe.git
cd AI-Agent-Universe

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 复制配置文件
cp config.example.yaml config.yaml
```

## 配置

编辑 `config.yaml` 文件，填入您的 API 密钥：

```yaml
llm:
  providers:
    openai:
      api_key: sk-your-api-key-here
    anthropic:
      api_key: your-anthropic-api-key
```

## 第一个 Agent

创建 `my_first_agent.py`：

```python
from ai_agent_universe import Agent

# 创建 Agent
agent = Agent(
    role="助手",
    goal="帮助用户完成任务",
    model="gpt-4",
    verbose=True
)

# 执行任务
response = agent.execute("你好，请介绍一下自己")
print(response)
```

运行：
```bash
python my_first_agent.py
```

## 运行示例

```bash
# 基础 Agent 示例
python examples/example_1_basic_agent.py

# 多 Agent 协作示例
python examples/example_2_multi_agent.py

# 工作流自动化示例
python examples/example_3_workflow.py

# 文件自动化示例
python examples/example_4_file_automation.py

# 网页自动化示例
python examples/example_5_web_automation.py
```

## 下一步

- 查看 [README.md](README.md) 了解完整功能
- 阅读 [docs/](docs/) 目录下的详细文档
- 尝试修改示例代码
- 创建您自己的 Agent 和工具

## 获取帮助

- 查看文档：https://github.com/niuzaisheng/AI-Agent-Universe
- 提交问题：https://github.com/niuzaisheng/AI-Agent-Universe/issues
- 讨论区：https://github.com/niuzaisheng/AI-Agent-Universe/discussions
