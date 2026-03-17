"""
示例 2: 多 Agent 协作
"""

import sys
sys.path.insert(0, 'src')

from ai_agent_universe import Agent, Crew, Task

# 创建不同角色的 Agent
researcher = Agent(
    role="高级研究员",
    goal="收集和分析信息",
    backstory="你是一位经验丰富的研究员，擅长从各种来源收集信息并进行分析。",
    verbose=True
)

writer = Agent(
    role="技术作家",
    goal="撰写清晰的技术文档",
    backstory="你是一位专业的技术作家，擅长将复杂的技术概念转化为易于理解的内容。",
    verbose=True
)

reviewer = Agent(
    role="质量审核员",
    goal="确保内容质量",
    backstory="你是一位细致的质量审核员，负责检查文档的准确性和完整性。",
    verbose=True
)

# 创建任务
task1 = Task(
    description="研究 AI Agent 技术的最新发展",
    agent=researcher,
    expected_output="一份包含最新发展趋势的研究摘要"
)

task2 = Task(
    description="根据研究结果撰写技术博客文章",
    agent=writer,
    expected_output="一篇结构清晰的技术博客文章"
)

task3 = Task(
    description="审核博客文章的质量",
    agent=reviewer,
    expected_output="审核报告和改进建议"
)

# 创建团队并运行
print("=" * 50)
print("示例 2: 多 Agent 协作")
print("=" * 50)

crew = Crew(
    agents=[researcher, writer, reviewer],
    tasks=[task1, task2, task3],
    verbose=True
)

result = crew.run()

print("\n执行结果:")
for item in result['results']:
    print(f"\n任务：{item['task']}")
    print(f"执行者：{item.get('agent', 'N/A')}")
    print(f"结果：{item['result']}")
