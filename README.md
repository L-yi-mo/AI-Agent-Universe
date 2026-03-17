# 🌟 AI Agent Universe - 统一 AI Agent 平台

<div align="center">

**由 Trae IDE 整合制作**

一个功能强大的本地 AI Agent 自动化平台，整合了业界领先的 AI 框架和工具

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![GitHub stars](https://img.shields.io/github/stars/L-yi-mo/AI-Agent-Universe)](https://github.com/L-yi-mo/AI-Agent-Universe/stargazers)

</div>

## 📖 项目简介

**AI Agent Universe** 是一个全新的综合性 AI Agent 平台，旨在让 AI 能够在本地主机上运行和使用所有程序。本项目整合了以下顶级开源项目：

### 核心整合框架

#### 🎯 代码执行与解释器
- **[Open Interpreter](https://github.com/openinterpreter/open-interpreter)** - 自然语言界面的计算机控制
- **代码执行能力** - Python、JavaScript、Shell 等语言的本地执行

#### 🤖 多 Agent 协作框架
- **[MetaGPT](https://github.com/FoundationAgents/MetaGPT)** - 多 Agent 软件公司模拟
- **[AutoGen](https://github.com/microsoft/autogen)** - 微软多 Agent 对话框架
- **[CrewAI](https://github.com/crewAIInc/crewAI)** - 角色扮演的自主 AI Agent 编排
- **[AgentScope](https://github.com/ai-secure/AgentScope)** - 多 Agent 应用场景

#### 🔗 Agent 编排与工作流
- **[LangGraph](https://github.com/langchain-ai/langgraph)** - 基于图的 Agent 编排
- **[LangChain](https://github.com/langchain-ai/langchain)** - LLM 应用开发平台
- **[n8n](https://github.com/n8n-io/n8n)** - 工作流自动化平台
- **[TaskWeaver](https://github.com/microsoft/TaskWeaver)** - 微软任务编排器

#### 🧠 自主 Agent 系统
- **[AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)** - 自主 GPT-4 实验
- **[SuperAGI](https://github.com/TransformerOptimus/SuperAGI)** - 自主 Agent 框架
- **[AgentVerse](https://github.com/OpenBMB/AgentVerse)** - 协作 Agent 环境

#### 🖥️ 计算机控制与 UI 交互
- **[OmniParser](https://github.com/microsoft/OmniParser)** - 微软 UI 解析工具
- **[UFO](https://github.com/microsoft/UFO)** - 微软 Windows 自动化
- **[self-operating-computer](https://github.com/OthersideAI/self-operating-computer)** - 自操作计算机
- **[Agent-S](https://github.com/simular-ai/Agent-S)** - Agent 安全框架
- **[OS-Copilot](https://github.com/OS-Copilot/OS-Copilot)** - 操作系统副驾驶
- **[ShowUI](https://github.com/showlab/ShowUI)** - UI 视觉交互

#### 📚 知识库与 RAG
- **[LlamaIndex](https://github.com/run-llama/LlamaIndex)** - 文档数据框架
- **[llm-universe](https://github.com/datawhalechina/llm-universe)** - LLM 知识库

#### 🔌 集成与工具
- **[LiteLLM](https://github.com/BerriAI/litellm)** - 统一 LLM API
- **[phidata](https://github.com/phidatahq/phidata)** - Agent 工具库
- **[composio](https://github.com/composiohq/composio)** - Agent 工具集成
- **[MetaGPT](https://github.com/MetaGPT/MetaGPT)** - 元编程框架

## ✨ 核心特性

### 🚀 强大的本地执行能力
- ✅ 本地代码执行（Python、JavaScript、Shell）
- ✅ 文件系统操作与管理
- ✅ 系统命令自动化
- ✅ 浏览器控制与网页自动化
- ✅ GUI 应用交互

### 🧩 多 Agent 协作
- ✅ 角色定义与任务分配
- ✅ Agent 间通信与协作
- ✅ 复杂任务分解与执行
- ✅ 结果验证与质量保障

### 🔗 灵活的工作流编排
- ✅ 可视化工作流设计
- ✅ 条件分支与循环
- ✅ 并行任务执行
- ✅ 错误处理与恢复

### 🖥️ 智能 UI 交互
- ✅ 屏幕内容理解
- ✅ UI 元素识别与定位
- ✅ 鼠标键盘自动化
- ✅ 跨应用工作流

### 📊 企业级功能
- ✅ 多模型支持（OpenAI、Claude、本地模型）
- ✅ 安全沙箱执行
- ✅ 审计日志与监控
- ✅ 权限管理与控制

## 🏗️ 系统架构

```
AI Agent Universe
├── Core Engine (核心引擎)
│   ├── Agent Orchestrator (Agent 编排器)
│   ├── Code Executor (代码执行器)
│   ├── UI Controller (UI 控制器)
│   └── Security Manager (安全管理器)
├── Integration Layer (集成层)
│   ├── LLM Providers (LLM 提供商)
│   ├── Tool Adapters (工具适配器)
│   └── API Gateway (API 网关)
├── Agent Frameworks (Agent 框架)
│   ├── Multi-Agent System (多 Agent 系统)
│   ├── Workflow Engine (工作流引擎)
│   └── Task Planner (任务规划器)
└── User Interface (用户界面)
    ├── CLI Interface (命令行界面)
    ├── Web Dashboard (Web 仪表板)
    └── API Interface (API 接口)
```

## 📦 安装指南

### 前置要求

- Python 3.10+
- Node.js 18+ (用于 Web 界面)
- Git

### 快速安装

```bash
# 克隆仓库
git clone https://github.com/L-yi-mo/AI-Agent-Universe.git
cd AI-Agent-Universe

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 安装可选组件
pip install -r requirements-optional.txt
```

### 配置

```bash
# 复制配置文件
cp config.example.yaml config.yaml

# 编辑配置文件，设置您的 API 密钥等
# config.yaml 包含：
# - LLM API 密钥 (OpenAI, Anthropic, 等)
# - 本地模型配置
# - 安全设置
# - 功能开关
```

## 🚀 快速开始

### 基础使用

```python
from ai_agent_universe import Agent

# 创建 Agent
agent = Agent(
    model="gpt-4",
    tools=["code_interpreter", "file_system", "browser"],
    verbose=True
)

# 执行任务
response = agent.execute("分析当前目录下的所有 Python 文件")
print(response)
```

### 多 Agent 协作

```python
from ai_agent_universe import Crew, Agent, Task

# 定义 Agent
researcher = Agent(role="研究员", goal="信息收集")
analyst = Agent(role="分析师", goal="数据分析")
writer = Agent(role="作家", goal="报告撰写")

# 创建任务
tasks = [
    Task(description="收集最新 AI 资讯", agent=researcher),
    Task(description="分析收集的信息", agent=analyst),
    Task(description="撰写分析报告", agent=writer)
]

# 执行
crew = Crew(agents=[researcher, analyst, writer], tasks=tasks)
result = crew.run()
```

### 工作流自动化

```python
from ai_agent_universe import Workflow

# 创建工作流
workflow = Workflow()

# 添加步骤
workflow.add_step(
    name="fetch_data",
    action="api_call",
    params={"url": "https://api.example.com/data"}
)

workflow.add_step(
    name="process_data",
    action="python_code",
    code="process(data)"
)

workflow.add_step(
    name="save_result",
    action="file_write",
    params={"path": "output.json"}
)

# 执行工作流
workflow.run()
```

## 🔧 配置选项

### LLM 配置

```yaml
llm:
  providers:
    openai:
      api_key: ${OPENAI_API_KEY}
      models: ["gpt-4", "gpt-3.5-turbo"]
    anthropic:
      api_key: ${ANTHROPIC_API_KEY}
      models: ["claude-3-opus", "claude-3-sonnet"]
    local:
      api_base: "http://localhost:1234/v1"
      models: ["local-model"]
  
  default_provider: openai
  default_model: gpt-4
```

### 安全配置

```yaml
security:
  # 代码执行前需要确认
  require_code_approval: true
  
  # 允许的命令
  allowed_commands:
    - "ls"
    - "cat"
    - "python"
  
  # 禁止的路径
  blocked_paths:
    - "/etc"
    - "/system32"
  
  # 沙箱模式
  sandbox_enabled: true
```

## 🛠️ 开发指南

### 创建自定义 Agent

```python
from ai_agent_universe import BaseAgent, tool

class CustomAgent(BaseAgent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.specialty = "custom_task"
    
    @tool
    def custom_action(self, param: str) -> str:
        """执行自定义操作"""
        return f"Processed: {param}"
```

### 添加工具

```python
from ai_agent_universe import Tool

@Tool
def my_custom_tool(input: str) -> str:
    """
    我的自定义工具
    
    Args:
        input: 输入参数
    
    Returns:
        处理结果
    """
    return f"Result: {input}"
```

## 📚 使用案例

### 1. 自动化数据分析

```python
agent.execute("""
1. 读取 data.csv 文件
2. 进行数据清洗和预处理
3. 生成统计报告和可视化图表
4. 保存结果为 PDF 报告
""")
```

### 2. 智能文件管理

```python
agent.execute("""
1. 扫描下载文件夹
2. 按文件类型分类（图片、文档、视频等）
3. 移动到对应的文件夹
4. 生成整理报告
""")
```

### 3. 网页自动化

```python
agent.execute("""
1. 打开浏览器访问指定网站
2. 搜索关键词
3. 抓取前 10 个结果
4. 保存为结构化数据
""")
```

### 4. 多 Agent 代码审查

```python
crew = Crew(
    agents=[
        Agent(role="代码审查员", goal="发现代码问题"),
        Agent(role="安全专家", goal="检查安全漏洞"),
        Agent(role="性能优化师", goal="优化代码性能")
    ],
    tasks=[
        Task(description="审查 main.py 文件")
    ]
)
```

## 🔒 安全说明

⚠️ **重要安全提示**：

1. **代码执行风险**：Agent 执行的代码可能修改文件系统或系统设置
2. **建议操作**：
   - 在生产环境使用前，先在隔离环境测试
   - 启用沙箱模式
   - 配置适当的权限限制
   - 定期备份重要数据
3. **监控与审计**：启用完整的日志记录，定期审查 Agent 行为

## 🤝 贡献指南

我们欢迎社区贡献！请参考以下步骤：

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🙏 致谢

本项目整合了以下优秀的开源项目，向所有贡献者致敬：

- Open Interpreter
- Microsoft AutoGen
- MetaGPT
- LangChain/LangGraph
- CrewAI
- AutoGPT
- 以及所有列出的开源项目

## 📬 联系方式

- **项目地址**: https://github.com/L-yi-mo/AI-Agent-Universe
- **问题反馈**: https://github.com/L-yi-mo/AI-Agent-Universe/issues
- **作者**: L-yi-mo
- **整合制作**: Trae IDE (Qwen3.5-Plus)

## 🌟 Star History

感谢所有为本项目点亮 Star 的朋友！

---

<div align="center">

**由 Trae IDE 整合制作**

Made with ❤️ by L-yi-mo using Trae IDE (Qwen3.5-Plus)

</div>
