"""
配置管理模块
"""

import os
import yaml
from typing import Dict, Any, Optional
from pathlib import Path


class Config:
    """配置管理器"""
    
    _instance: Optional['Config'] = None
    _config: Dict[str, Any] = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._config:
            self.load_default_config()
    
    def load_default_config(self):
        """加载默认配置"""
        self._config = {
            'llm': {
                'default_provider': 'openai',
                'default_model': 'gpt-4',
            },
            'security': {
                'code_execution': {
                    'require_approval': True,
                    'sandbox_enabled': True,
                }
            },
            'agent': {
                'verbose': True,
            }
        }
    
    def load_from_file(self, path: str):
        """从文件加载配置"""
        config_path = Path(path)
        if config_path.exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                file_config = yaml.safe_load(f)
                self._config = self._merge_configs(file_config)
    
    def _merge_configs(self, new_config: Dict[str, Any]) -> Dict[str, Any]:
        """合并配置"""
        merged = self._config.copy()
        for key, value in new_config.items():
            if isinstance(value, dict) and key in merged:
                merged[key] = self._merge_configs(value)
            else:
                merged[key] = value
        return merged
    
    def get(self, key: str, default: Any = None) -> Any:
        """获取配置值"""
        keys = key.split('.')
        value = self._config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value
    
    def set(self, key: str, value: Any):
        """设置配置值"""
        keys = key.split('.')
        config = self._config
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        config[keys[-1]] = value
    
    @classmethod
    def reset(cls):
        """重置配置"""
        cls._instance = None
        cls._config = {}


# 全局配置实例
config = Config()
