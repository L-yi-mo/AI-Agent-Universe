# GitHub Actions 配置指南

## 📦 已配置的工作流

### 1. Python CI/CD (python-ci.yml)

**功能**：
- ✅ 自动测试 Python 3.10, 3.11, 3.12
- ✅ 代码检查（flake8）
- ✅ 包结构验证
- ✅ 导入测试
- ✅ 构建包（发布时）

**触发条件**：
- 推送到 main 分支
- Pull Request
- Tag 推送（部署）

---

## 🚀 使用 GitHub Actions

### 启用 Actions

1. 访问您的仓库：https://github.com/L-yi-mo/AI-Agent-Universe
2. 点击 **"Actions"** 标签
3. 如果是首次使用，点击 **"I understand my workflows, go ahead and enable them"**
4. 工作流将自动运行

### 查看运行状态

- **Actions 标签**: 查看所有工作流运行记录
- **徽章**: 在 README 中添加状态徽章

```markdown
[![CI/CD](https://github.com/L-yi-mo/AI-Agent-Universe/actions/workflows/python-ci.yml/badge.svg)](https://github.com/L-yi-mo/AI-Agent-Universe/actions/workflows/python-ci.yml)
```

---

## 📝 其他可选配置

### SLSA 通用生成器

如果您需要生成 SLSA3 来源证明，可以配置：

```yaml
# .github/workflows/slsa-generator.yml
name: SLSA Generic Generator
on:
  push:
    tags:
      - '*'

permissions: read-all

jobs:
  build:
    outputs:
      digests: ${{ steps.hash.outputs.digests }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Hash artifacts
        id: hash
        run: |
          echo "digests=$(sha256sum *.tar.gz | base64 -w0)" >> $GITHUB_OUTPUT
  
  generate:
    needs: [build]
    permissions:
      actions: read
      id-token: write
    uses: slsa-framework/slsa-github-generator/.github/workflows/generator_generic_slsa3.yml@v2.0.0
    with:
      base64-subjects: "${{ needs.build.outputs.digests }}"
```

### 自动发布

```yaml
# .github/workflows/release.yml
name: Release

on:
  push:
    tags:
      - 'v*.*.*'

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Create Release
      uses: softprops/action-gh-release@v1
      with:
        generate_release_notes: true
```

---

## 🔧 自定义配置

### 添加测试

在 `python-ci.yml` 中添加测试步骤：

```yaml
- name: Run tests
  run: |
    pip install pytest
    pytest tests/ --cov=src/
```

### 添加代码覆盖率

```yaml
- name: Upload coverage
  uses: codecov/codecov-action@v3
  with:
    file: ./coverage.xml
```

### 添加依赖缓存

```yaml
- name: Cache pip packages
  uses: actions/cache@v3
  with:
    paths: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-pip-
```

---

## 📊 工作流状态徽章

将以下代码添加到 README.md：

```markdown
## 📊 CI/CD 状态

[![CI/CD](https://github.com/L-yi-mo/AI-Agent-Universe/actions/workflows/python-ci.yml/badge.svg?branch=main)](https://github.com/L-yi-mo/AI-Agent-Universe/actions/workflows/python-ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
```

---

## 🐛 故障排除

### 工作流未运行

**检查**：
1. Actions 是否已启用
2. 配置文件语法是否正确
3. 文件是否在正确位置：`.github/workflows/`

### 构建失败

**查看日志**：
1. 点击失败的运行记录
2. 查看详细错误信息
3. 修复后重新推送

### 权限问题

**确保**：
- 仓库有 Actions 权限
- 使用正确的权限设置

---

## 📚 相关资源

- [GitHub Actions 文档](https://docs.github.com/en/actions)
- [Python 工作流模板](https://github.com/actions/starter-workflows/tree/main/ci)
- [SLSA 框架](https://slsa.dev/)

---

**由 Trae IDE (Qwen3.5-Plus) 整合制作**

Made with ❤️ by L-yi-mo using Trae IDE (Qwen3.5-Plus)
