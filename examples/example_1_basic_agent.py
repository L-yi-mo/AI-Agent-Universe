"""
示例 1: 基础 Agent 使用
"""

import sys
sys.path.insert(0, 'src')

from ai_agent_universe import Agent, tool

# 创建自定义工具
@tool
def calculate_sum(numbers: list) -> str:
    """计算数字列表的总和"""
    return str(sum(numbers))

# 创建 Agent
agent = Agent(
    role="Python 助手",
    goal="帮助用户执行 Python 相关任务",
    model="gpt-4",
    verbose=True
)

# 添加自定义工具
agent.add_tool(calculate_sum)

# 执行任务
print("=" * 50)
print("示例 1: 基础 Agent 使用")
print("=" * 50)

response = agent.execute("计算 [1, 2, 3, 4, 5] 的总和")
print(f"Response: {response}")

# 对话模式
print("\n对话模式:")
response = agent.chat("你好，请介绍一下自己")
print(f"Agent: {response}")
