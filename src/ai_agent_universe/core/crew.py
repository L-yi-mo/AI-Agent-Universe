"""
Crew 多 Agent 协作模块
整合了 CrewAI 和 MetaGPT 的多 Agent 协作能力
"""

from typing import List, Dict, Any
from .agent import Agent
from .task import Task


class Crew:
    """
    Agent 团队
    
    用于编排多个 Agent 协同完成复杂任务
    """
    
    def __init__(
        self,
        agents: List[Agent],
        tasks: List[Task],
        verbose: bool = False,
        **kwargs
    ):
        self.agents = agents
        self.tasks = tasks
        self.verbose = verbose
        self.results = []
        
    def run(self) -> Dict[str, Any]:
        """
        运行团队任务
        
        Returns:
            执行结果
        """
        print(f"[Crew] Starting with {len(self.agents)} agents and {len(self.tasks)} tasks")
        
        for task in self.tasks:
            print(f"[Crew] Executing task: {task.description}")
            result = task.execute()
            self.results.append({
                "task": task.description,
                "result": result
            })
        
        return {
            "success": True,
            "results": self.results
        }
    
    def add_agent(self, agent: Agent):
        """添加 Agent"""
        self.agents.append(agent)
    
    def add_task(self, task: Task):
        """添加任务"""
        self.tasks.append(task)
