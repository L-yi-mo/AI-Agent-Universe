# 项目结构

```
AI-Agent-Universe/
├── src/                          # 源代码目录
│   └── ai_agent_universe/        # Python 包
│       ├── __init__.py           # 包初始化
│       ├── core/                 # 核心模块
│       │   ├── __init__.py
│       │   ├── agent.py          # Agent 基类
│       │   ├── crew.py           # 多 Agent 协作
│       │   ├── task.py           # 任务定义
│       │   └── workflow.py       # 工作流引擎
│       ├── agents/               # Agent 实现
│       ├── tools/                # 工具集成
│       │   ├── __init__.py
│       │   └── tool_integrations.py
│       ├── integrations/         # 第三方集成
│       ├── workflows/            # 工作流定义
│       ├── ui/                   # 用户界面
│       ├── config/               # 配置管理
│       │   ├── __init__.py
│       │   └── config_manager.py
│       └── utils/                # 工具函数
│           ├── __init__.py
│           └── decorators.py     # 装饰器
├── examples/                     # 示例代码
│   ├── example_1_basic_agent.py
│   ├── example_2_multi_agent.py
│   ├── example_3_workflow.py
│   ├── example_4_file_automation.py
│   └── example_5_web_automation.py
├── docs/                         # 文档
├── tests/                        # 测试
├── scripts/                      # 工具脚本
├── config.example.yaml           # 配置示例
├── requirements.txt              # 依赖
├── requirements-optional.txt     # 可选依赖
├── setup.py                      # 安装脚本
├── install.bat                   # Windows 安装脚本
├── install.sh                    # Linux/Mac安装脚本
├── LICENSE                       # 许可证
├── README.md                     # 项目说明
└── QUICKSTART.md                 # 快速开始
```

## 模块说明

### 核心模块 (core/)

- **agent.py**: Agent 基类，整合多个 Agent 框架
- **crew.py**: 多 Agent 协作编排
- **task.py**: 任务定义和执行
- **workflow.py**: 工作流引擎

### 工具模块 (tools/)

- **tool_integrations.py**: 整合各框架的工具能力
  - CodeInterpreterTools: 代码执行
  - FileSystemTools: 文件操作
  - BrowserTools: 浏览器自动化

### 配置模块 (config/)

- **config_manager.py**: 配置管理，支持 YAML 配置

### 工具模块 (utils/)

- **decorators.py**: 工具装饰器和注册表

## 架构设计

AI Agent Universe 采用分层架构：

1. **接口层**: CLI, Web UI, API
2. **编排层**: Crew, Workflow, Task
3. **核心层**: Agent, Tools, Integrations
4. **基础设施层**: LLM Providers, Config, Security

这种设计使得：
- 易于扩展新的 Agent 和工具
- 支持灵活的任务编排
- 便于集成第三方框架
- 保证安全性和可维护性
