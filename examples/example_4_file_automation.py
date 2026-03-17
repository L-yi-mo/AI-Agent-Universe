"""
示例 4: 文件自动化任务
"""

import sys
sys.path.insert(0, 'src')

from ai_agent_universe import Agent

# 创建文件管理 Agent
file_agent = Agent(
    role="文件管理助手",
    goal="帮助用户管理和组织文件",
    model="gpt-4",
    tools=["file_system", "code_interpreter"],
    verbose=True
)

print("=" * 50)
print("示例 4: 文件自动化任务")
print("=" * 50)

# 任务 1: 文件整理
print("\n任务 1: 整理下载文件夹")
response = file_agent.execute("""
请帮我整理下载文件夹：
1. 扫描下载文件夹中的所有文件
2. 按文件类型分类（图片、文档、压缩包等）
3. 创建对应的文件夹并将文件移动进去
4. 生成整理报告
""")
print(response)

# 任务 2: 批量重命名
print("\n任务 2: 批量重命名文件")
response = file_agent.execute("""
请批量重命名当前目录下的所有图片文件：
1. 找出所有 .jpg 和 .png 文件
2. 按照 'image_001.jpg', 'image_002.png' 的格式重命名
3. 保持序号连续
""")
print(response)

# 任务 3: 文件分析
print("\n任务 3: 分析项目文件结构")
response = file_agent.execute("""
请分析当前项目的文件结构：
1. 列出所有目录和文件
2. 统计各类文件的数量
3. 找出最大的 10 个文件
4. 生成项目结构报告
""")
print(response)
