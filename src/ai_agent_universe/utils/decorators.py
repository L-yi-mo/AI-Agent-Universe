"""
工具装饰器模块
用于定义和注册工具
"""

from functools import wraps
from typing import Callable, Dict, Any, Optional


def tool(func: Callable) -> Callable:
    """
    工具装饰器
    
    用于标记一个函数为 Agent 工具
    
    Usage:
        @tool
        def my_tool(param: str) -> str:
            '''Tool description'''
            return result
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    
    # 添加工具元数据
    wrapper._is_tool = True
    wrapper._tool_name = func.__name__
    wrapper._tool_description = func.__doc__ or ""
    
    return wrapper


class ToolRegistry:
    """工具注册表"""
    
    _tools: Dict[str, Callable] = {}
    
    @classmethod
    def register(cls, func: Callable) -> Callable:
        """注册工具"""
        if hasattr(func, '_is_tool') and func._is_tool:
            cls._tools[func.__name__] = func
        else:
            # 自动标记为工具
            func = tool(func)
            cls._tools[func.__name__] = func
        return func
    
    @classmethod
    def get_tool(cls, name: str) -> Optional[Callable]:
        """获取工具"""
        return cls._tools.get(name)
    
    @classmethod
    def list_tools(cls) -> Dict[str, str]:
        """列出所有工具"""
        return {
            name: tool._tool_description 
            for name, tool in cls._tools.items()
        }
    
    @classmethod
    def clear(cls):
        """清空注册表"""
        cls._tools = {}
