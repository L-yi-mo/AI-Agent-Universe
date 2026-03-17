"""
Task 任务模块
"""

from typing import Dict, Any, Optional, Callable


class Task:
    """
    任务类
    
    用于定义和执行单个任务
    """
    
    def __init__(
        self,
        description: str,
        agent=None,
        expected_output: str = "",
        async_execution: bool = False,
        context: Optional[Dict[str, Any]] = None,
        **kwargs
    ):
        self.description = description
        self.agent = agent
        self.expected_output = expected_output
        self.async_execution = async_execution
        self.context = context or {}
        
    def execute(self) -> Dict[str, Any]:
        """
        执行任务
        
        Returns:
            执行结果
        """
        if self.agent:
            result = self.agent.execute(self.description)
            return {
                "task": self.description,
                "result": result,
                "agent": self.agent.role
            }
        else:
            return {
                "task": self.description,
                "result": "No agent assigned",
                "agent": None
            }
    
    def set_agent(self, agent):
        """设置执行 Agent"""
        self.agent = agent
