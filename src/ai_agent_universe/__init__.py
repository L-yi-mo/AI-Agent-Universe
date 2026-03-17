"""
AI Agent Universe - 统一 AI Agent 平台
由 Trae IDE 整合制作
"""

__version__ = "0.1.0"
__author__ = "niuzaisheng"
__description__ = "A comprehensive AI Agent platform integrating multiple frameworks"

from .core.agent import Agent
from .core.crew import Crew
from .core.task import Task
from .core.workflow import Workflow
from .utils.decorators import tool

__all__ = [
    "Agent",
    "Crew",
    "Task",
    "Workflow",
    "tool"
]
