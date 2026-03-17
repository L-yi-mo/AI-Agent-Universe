"""
示例 3: 工作流自动化
"""

import sys
sys.path.insert(0, 'src')

from ai_agent_universe import Workflow

# 创建工作流
print("=" * 50)
print("示例 3: 工作流自动化")
print("=" * 50)

workflow = Workflow(verbose=True)

# 添加步骤：获取数据
workflow.add_step(
    name="fetch_data",
    action="api_call",
    params={
        "url": "https://api.example.com/data",
        "method": "GET"
    }
)

# 添加步骤：处理数据
workflow.add_step(
    name="process_data",
    action="python_code",
    code="""
import pandas as pd
# 数据处理逻辑
data = fetch_data_result
processed = data.groupby('category').sum()
"""
)

# 添加步骤：生成报告
workflow.add_step(
    name="generate_report",
    action="python_code",
    code="""
# 生成报告
report = f"Report generated with {len(processed)} categories"
"""
)

# 添加步骤：保存结果
workflow.add_step(
    name="save_results",
    action="file_write",
    params={
        "path": "output/report.json",
        "format": "json"
    }
)

# 可视化工作流
print("\n工作流步骤:")
workflow.visualize()

# 执行工作流
print("\n执行工作流...")
result = workflow.run()

print("\n执行结果:")
for step_name, step_result in result['results'].items():
    print(f"  {step_name}: {step_result}")
