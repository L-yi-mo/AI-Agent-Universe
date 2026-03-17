# 开发指南

## 版权信息

**Copyright (c) 2026 L-yi-mo. All Rights Reserved.**

**整合制作**: Trae IDE (Qwen3.5-Plus)

本项目采用专有许可证，详见 [LICENSE](../LICENSE) 文件。

## 开发环境设置

```bash
# 克隆仓库
git clone https://github.com/L-yi-mo/AI-Agent-Universe.git
cd AI-Agent-Universe
```

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装开发依赖
pip install -r requirements.txt
pip install -r requirements-dev.txt  # 如果有的话
```

## 代码规范

### 代码风格

- 遵循 PEP 8 规范
- 使用 Black 进行代码格式化
- 使用 Flake8 进行代码检查
- 使用 MyPy 进行类型检查

```bash
# 格式化代码
black src/ examples/

# 代码检查
flake8 src/ examples/

# 类型检查
mypy src/
```

### 命名规范

- 类名：大驼峰命名 (CamelCase)
- 函数和变量：小写 + 下划线 (snake_case)
- 常量：全大写 + 下划线
- 私有成员：单下划线前缀

### 类型注解

所有公共 API 都应该有类型注解：

```python
from typing import List, Dict, Optional

def process_data(
    items: List[str],
    config: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """处理数据"""
    pass
```

## 测试

### 运行测试

```bash
# 运行所有测试
pytest tests/

# 运行特定测试
pytest tests/test_agent.py

# 带覆盖率
pytest --cov=src tests/
```

### 编写测试

```python
import pytest
from ai_agent_universe import Agent

def test_agent_creation():
    """测试 Agent 创建"""
    agent = Agent(role="test", goal="test goal")
    assert agent.role == "test"
    assert agent.goal == "test goal"

@pytest.mark.asyncio
async def test_async_execution():
    """测试异步执行"""
    pass
```

## 添加新功能

### 1. 创建新 Agent

```python
# src/ai_agent_universe/agents/custom_agent.py
from ..core.agent import Agent

class CustomAgent(Agent):
    """自定义 Agent"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 初始化代码
    
    def execute(self, task: str) -> str:
        """执行任务"""
        # 实现逻辑
        return result
```

### 2. 添加工具

```python
# src/ai_agent_universe/tools/my_tool.py
from ..utils.decorators import tool, ToolRegistry

@ToolRegistry.register
@tool
def my_tool(param: str) -> str:
    """
    我的工具
    
    Args:
        param: 参数
    
    Returns:
        结果
    """
    return f"Result: {param}"
```

### 3. 集成第三方框架

```python
# src/ai_agent_universe/integrations/third_party.py
from .base import Integration

class ThirdPartyIntegration(Integration):
    """第三方集成"""
    
    def __init__(self):
        super().__init__()
        self.client = None
    
    def connect(self, config):
        """连接到服务"""
        # 实现连接逻辑
        pass
    
    def execute(self, action, **kwargs):
        """执行操作"""
        # 实现执行逻辑
        pass
```

## 提交代码

### Git 工作流

```bash
# 创建特性分支
git checkout -b feature/your-feature

# 提交更改
git add .
git commit -m "feat: add new feature

- Description of change 1
- Description of change 2"

# 推送到远程
git push origin feature/your-feature

# 创建 Pull Request
```

### 提交信息规范

遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

- `feat`: 新功能
- `fix`: 修复 bug
- `docs`: 文档更新
- `style`: 代码格式
- `refactor`: 重构
- `test`: 测试相关
- `chore`: 构建/工具

## 文档

### 代码注释

所有公共 API 都应该有文档字符串：

```python
def my_function(param: str) -> str:
    """
    函数说明
    
    Args:
        param: 参数说明
    
    Returns:
        返回值说明
    
    Raises:
        ValueError: 异常说明
    """
    pass
```

### 更新文档

- README.md: 项目概述
- QUICKSTART.md: 快速开始
- docs/: 详细文档

## 发布

### 版本管理

使用语义化版本 (Semantic Versioning):

- MAJOR.MINOR.PATCH (例如：1.2.3)
- MAJOR: 不兼容的 API 更改
- MINOR: 向后兼容的功能
- PATCH: 向后兼容的问题修复

### 发布步骤

1. 更新版本号 (src/ai_agent_universe/__init__.py)
2. 更新 CHANGELOG.md
3. 提交并打标签
4. 发布到 PyPI (如果适用)

## 调试

### 启用调试模式

```yaml
# config.yaml
agent:
  verbose: true
  debug: true

logging:
  level: DEBUG
```

### 使用调试器

```python
import pdb; pdb.set_trace()  # 传统调试
# 或
breakpoint()  # Python 3.7+
```

## 性能优化

### 性能分析

```python
import cProfile
import pstats

def profile_function():
    profiler = cProfile.Profile()
    profiler.enable()
    
    # 运行代码
    my_function()
    
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats()
```

### 优化建议

- 使用缓存减少重复计算
- 异步处理 I/O 操作
- 批量处理减少 API 调用
- 使用生成器处理大数据

## 常见问题

### Q: 如何添加新的 LLM 提供商？

A: 在 `src/ai_agent_universe/integrations/llm_providers.py` 中添加新的提供商类

### Q: 如何创建自定义工具？

A: 使用 `@tool` 装饰器，参考 `docs/PROJECT_STRUCTURE.md`

### Q: 如何调试 Agent 执行？

A: 设置 `verbose=True` 并检查日志文件

## 贡献

欢迎贡献代码、文档、测试等！请查看：

- 问题追踪器：https://github.com/L-yi-mo/AI-Agent-Universe/issues
- 讨论区：https://github.com/L-yi-mo/AI-Agent-Universe/discussions

---

**由 Trae IDE (Qwen3.5-Plus) 整合制作**

**Copyright (c) 2026 L-yi-mo. All Rights Reserved.**
