"""
示例 5: 网页自动化
"""

import sys
sys.path.insert(0, 'src')

from ai_agent_universe import Agent

# 创建网页自动化 Agent
web_agent = Agent(
    role="网页自动化助手",
    goal="帮助用户完成网页自动化任务",
    model="gpt-4",
    tools=["browser", "code_interpreter"],
    verbose=True
)

print("=" * 50)
print("示例 5: 网页自动化")
print("=" * 50)

# 任务 1: 信息抓取
print("\n任务 1: 抓取新闻网站标题")
response = web_agent.execute("""
请访问新闻网站并：
1. 打开网站首页
2. 抓取前 10 条新闻标题
3. 提取每条新闻的链接
4. 保存为 CSV 文件
""")
print(response)

# 任务 2: 自动登录
print("\n任务 2: 网站自动登录")
response = web_agent.execute("""
请帮我登录到指定网站：
1. 打开登录页面
2. 填写用户名和密码
3. 点击登录按钮
4. 确认登录成功
5. 截图保存登录后的页面
""")
print(response)

# 任务 3: 数据监控
print("\n任务 3: 价格监控")
response = web_agent.execute("""
请监控商品价格：
1. 访问商品页面
2. 提取当前价格
3. 与目标价格比较
4. 如果低于目标价格，发送邮件通知
5. 记录价格历史
""")
print(response)
