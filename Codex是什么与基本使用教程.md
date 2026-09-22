# Codex 简明使用教程

> 本文主要介绍：Codex 与 ChatGPT 的区别、Codex 项目中的常见文件，以及如何在 VS Code 中实际使用 Codex。
>
> 核对日期：2026-09-20。Codex 更新较快，界面和功能如有变化，请以 OpenAI 官方文档为准。

## 目录

- [一、Codex 与 ChatGPT 的区别](#一codex-与-chatgpt-的区别)
- [二、Codex 项目中常见的文件结构](#二codex-项目中常见的文件结构)
- [三、AGENTS.md：给 Codex 的项目说明书](#三agentsmd给-codex-的项目说明书)
- [四、Skills：给 Codex 的专项工作手册](#四skills给-codex-的专项工作手册)
- [五、在 VS Code 中使用 Codex](#五在-vs-code-中使用-codex)
- [六、推荐的实际工作流程](#六推荐的实际工作流程)
- [参考资料](#参考资料)

---

## 一、Codex 与 ChatGPT 的区别

### 1. ChatGPT 是通用 AI 助手

ChatGPT 适合回答问题、解释知识、写作、翻译、总结和讨论方案。它的主要工作方式是：你提出问题，它在聊天窗口中给出回答。

例如：

```text
请解释 MATLAB 中扩展卡尔曼滤波的原理，并给出一段示例代码。
```

ChatGPT 通常会解释原理，并生成可供参考的代码。

### 2. Codex 是编程智能体

Codex 面向软件开发。它不仅能回答代码问题，还能在你允许的范围内：

- 阅读项目目录和源代码；
- 搜索函数、类和调用关系；
- 修改真实项目文件；
- 运行测试、构建和检查命令；
- 查看 Git 状态和代码差异；
- 根据项目规则连续完成多个开发步骤。

可以简单理解为：

> ChatGPT 更偏向“告诉你怎么做”，Codex 更偏向“进入项目并使用开发工具把任务做完”。

例如：

```text
请阅读当前 MATLAB 项目的定位模块，找到状态更新函数。
在不改变输入输出接口的前提下加入扩展卡尔曼滤波，
补充测试，运行测试，并说明修改了哪些文件。
```

Codex 可以读取真实工程、修改相关文件并尝试运行验证。

### 3. 核心区别

| 对比内容 | ChatGPT 普通聊天 | Codex |
| --- | --- | --- |
| 主要用途 | 问答、写作、分析和讨论 | 软件开发和项目操作 |
| 主要上下文 | 当前对话和上传内容 | 项目目录、源代码、测试和 Git 状态 |
| 文件操作 | 通常给出建议或代码片段 | 可以直接修改授权目录中的文件 |
| 命令执行 | 通常告诉你运行什么命令 | 可以调用终端和项目已有工具 |
| 典型结果 | 回答、方案或示例代码 | 文件改动、测试结果和变更总结 |
| 使用风险 | 回答可能不准确 | 还可能改错文件或执行不合适的命令 |

Codex 与 ChatGPT 并不是完全分离的两个产品。Codex 可以作为 ChatGPT 中的开发入口，也可以通过桌面应用、IDE、命令行和云端使用。OpenAI 当前建议：普通 Chat 用于问答与讨论，Codex 用于带代码库上下文和开发工具的软件任务。参见 [OpenAI：使用 ChatGPT](https://developers.openai.com/zh-Hans/docs/use-chatgpt)。

### 4. 如何选择

- 只想学习概念、讨论想法或修改一段文字：使用普通 ChatGPT。
- 需要阅读、修改或验证一个真实项目：使用 Codex。
- 需求还不清楚：先用 ChatGPT 讨论，再把明确任务交给 Codex。

---

## 二、Codex 项目中常见的文件结构

### 1. Codex 不要求固定的项目结构

所谓“Codex 项目”，通常仍然是普通的 Python、MATLAB、Java 或前端项目。Codex 不要求把代码改成某种固定结构。

真正与 Codex 有关的文件主要是：

- `AGENTS.md`：项目规则；
- `.agents/skills/`：项目专用的 Skills；
- `.codex/config.toml`：可选的项目级 Codex 配置。

一个示例结构如下：

```text
my-project/
├─ README.md
├─ AGENTS.md
├─ .gitignore
├─ src/
│  └─ main.py
├─ tests/
│  └─ test_main.py
├─ .agents/
│  └─ skills/
│     └─ code-review/
│        ├─ SKILL.md
│        ├─ scripts/
│        └─ references/
├─ .codex/
│  └─ config.toml
└─ .git/
```

### 2. 每个文件或目录的作用

| 文件或目录 | 主要作用 | 是否必须 |
| --- | --- | --- |
| `README.md` | 向人说明项目用途、安装和运行方法 | 推荐 |
| `src/` | 存放主要源代码，实际名称可能不同 | 由项目决定 |
| `tests/` | 存放单元测试或集成测试 | 推荐 |
| `.git/` | 保存 Git 版本历史 | 推荐 |
| `.gitignore` | 指定不提交到 Git 的文件 | 推荐 |
| `AGENTS.md` | 告诉 Codex 项目背景、工作规则和完成标准 | 推荐 |
| `AGENTS.override.md` | 在某个目录临时覆盖同级规则 | 可选 |
| `.agents/skills/` | 保存项目专用的工作流程 | 可选 |
| `SKILL.md` | 定义一个 Skill 的名称、触发条件和步骤 | 创建 Skill 时必须 |
| `scripts/` | 保存 Skill 需要调用的辅助脚本 | 可选 |
| `references/` | 保存 Skill 按需阅读的规范或资料 | 可选 |
| `.codex/config.toml` | 保存项目级 Codex 配置 | 可选 |

刚开始使用时不必一次创建全部内容。普通项目文件加一个简洁的 `AGENTS.md` 就足够了；只有某类任务经常重复时，才需要建立 Skill。

### 3. 项目外的个人配置

用户目录中还可能存在：

```text
用户目录/
├─ .codex/
│  ├─ AGENTS.md
│  └─ config.toml
└─ .agents/
   └─ skills/
```

- `~/.codex/AGENTS.md`：对多个项目生效的个人工作习惯；
- `~/.codex/config.toml`：个人默认配置；
- `~/.agents/skills/`：希望在多个项目中复用的 Skills。

项目中的文件适合团队共同维护，全局文件更适合保存个人习惯。

---

## 三、AGENTS.md：给 Codex 的项目说明书

这一部分对应[指定参考文章](https://jishuzhan.net/article/2053301309797892098)的第八节。

### 1. AGENTS.md 是什么

`AGENTS.md` 可以理解为“写给 Codex 看的项目说明书”。

- `README.md` 主要告诉开发者项目是什么、怎样使用；
- `AGENTS.md` 主要告诉 Codex 在项目中应当怎样工作。

其中通常包括：

- 项目使用的技术和版本；
- 重要目录及入口文件；
- 构建、运行和测试命令；
- 哪些文件不能修改；
- 必须保持哪些兼容性；
- 任务完成后需要报告什么。

Codex 会在开始任务前读取适用的 `AGENTS.md`。它通常从 Git 项目根目录开始，沿目录向当前工作目录逐层读取，距离当前目录更近的规则优先。参见 [OpenAI：使用 AGENTS.md 自定义指令](https://developers.openai.com/zh-Hans/docs/agent-configuration/agents-md)。

### 2. AGENTS.md 放在哪里

项目通用规则放在项目根目录：

```text
my-project/AGENTS.md
```

如果某个模块有特殊要求，可以在子目录中再放一个：

```text
my-project/
├─ AGENTS.md
└─ services/
   └─ payment/
      └─ AGENTS.md
```

处理 `payment` 模块时，Codex 会同时考虑根目录规则和该模块的具体规则。

### 3. 一个简单示例

```markdown
# AGENTS.md

## 项目说明

- 本项目使用 MATLAB R2024a。
- 主要算法位于 `src/`，测试位于 `tests/`。

## 工作规则

- 修改前先阅读 README 和相关测试。
- 不要改变公开函数的输入输出接口。
- 不要修改 `results/` 中的实验结果。
- 不要覆盖用户已有的未提交修改。

## 验证要求

- 修改代码后运行相关测试。
- 无法运行的测试必须说明原因。
- 完成前检查 Git diff。

## 完成后报告

- 修改了哪些文件；
- 运行了哪些测试；
- 是否存在未解决的风险。
```

### 4. 实际怎样使用

将文件放在项目中，然后开始一个新的 Codex 会话。Codex 会自动读取，一般不需要每次手动粘贴。

也可以让 Codex 根据现有项目起草：

```text
请阅读当前项目的 README、目录结构和测试配置，
为项目起草一份简洁的 AGENTS.md。
只写能够确认的内容，不确定之处标记出来。
```

生成后要人工检查测试命令、禁止事项和版本要求。`AGENTS.md` 应保持简短、明确，不要写入密码、令牌等秘密信息。

---

## 四、Skills：给 Codex 的专项工作手册

这一部分对应[指定参考文章](https://jishuzhan.net/article/2053301309797892098)的第九节。

### 1. Skill 是什么

Skill 可以理解为 Codex 的“专项工作手册”。

如果 `AGENTS.md` 说明整个项目都应遵守什么，那么 Skill 说明某一类任务具体应该怎样完成。例如：

- 代码审查；
- MATLAB 数据分析；
- 数据库安全迁移；
- 发布前检查；
- 生成测试与验证报告。

官方说明中，一个 Skill 是包含 `SKILL.md` 的文件夹，还可以包含脚本、参考资料和资源。Codex 先读取 Skill 的名称和描述，需要使用时才加载完整内容。参见 [OpenAI：构建 Skills](https://developers.openai.com/zh-Hans/docs/build-skills)。

### 2. Skill 的目录结构

```text
.agents/
└─ skills/
   └─ code-review/
      ├─ SKILL.md
      ├─ scripts/       # 可选：辅助脚本
      ├─ references/    # 可选：规范和资料
      └─ assets/        # 可选：模板等资源
```

其中只有 `SKILL.md` 是必需的。

### 3. 最小 SKILL.md 示例

文件路径：`.agents/skills/code-review/SKILL.md`

```markdown
---
name: code-review
description: 当用户要求审查代码、Git diff 或提交内容时使用。
---

# 代码审查流程

1. 先阅读 AGENTS.md 和当前 Git 状态。
2. 只审查，不修改文件。
3. 检查正确性、安全性、兼容性和测试遗漏。
4. 每个问题给出文件位置、影响和修改建议。
5. 按严重程度排列问题。
```

文件开头的 `name` 是 Skill 名称，`description` 告诉 Codex 何时应该使用它，正文是具体工作步骤。

### 4. 在实际过程中调用 Skill

可以在 Codex 对话框中直接输入：

```text
请使用 $code-review 审查当前未提交的修改，不要修改文件。
```

如果任务与 `description` 明确匹配，Codex 也可能自动选择相应 Skill。不过第一次使用或需要确保流程一致时，建议明确写出 `$code-review`。

### 5. AGENTS.md 与 Skill 的区别

| 内容 | AGENTS.md | Skill |
| --- | --- | --- |
| 作用范围 | 当前项目或目录 | 某一类专项任务 |
| 典型内容 | 技术栈、测试命令、禁止事项 | 审查、迁移、发布等具体流程 |
| 加载方式 | 开始任务时读取适用规则 | 需要该能力时加载完整流程 |
| 典型位置 | 项目根目录或子目录 | `.agents/skills/<名称>/SKILL.md` |

简单判断：

- “这个项目始终要怎样做”写入 `AGENTS.md`；
- “这类任务要按哪些步骤做”写入 Skill。

---

## 五、在 VS Code 中使用 Codex

本节参考了 [CodexGuide：在 VS Code 中使用 Codex](https://codexguide.ai/start/13-ide-vscode.html)，并根据 [OpenAI Codex IDE 官方文档](https://developers.openai.com/zh-Hans/docs/codex/ide)进行了核对。

### 1. 安装扩展

1. 打开 VS Code；
2. 点击左侧“扩展”；
3. 搜索 `Codex`；
4. 建议从 OpenAI 官方 IDE 页面进入安装链接，并确认发布者为 OpenAI；
5. 安装后按提示登录。

扩展名称和图标可能变化，因此应以官方安装页面和发布者信息为准。

### 2. 打开 Codex 侧边栏

安装后，可以点击侧边栏中的 Codex 图标。

如果没有看到图标，按 `Ctrl+Shift+P` 打开命令面板，然后运行：

```text
Codex: Open Codex Sidebar
```

### 3. 打开整个项目文件夹

使用“文件 → 打开文件夹”，选择包含源代码、测试、`AGENTS.md` 和 `.git` 的项目根目录。

应该打开：

```text
D:\code\my-project\
```

不要只打开：

```text
D:\code\my-project\src\main.py
```

打开整个项目后，Codex 才能理解目录结构、测试和项目规则。

### 4. 第一次先只读分析

在对话框中输入：

```text
请阅读当前项目的 README、AGENTS.md、目录结构和测试配置。
不要修改文件。请说明项目用途、主要入口、测试方法和可用 Skills。
```

这一步可以确认 Codex 是否打开了正确项目，以及是否识别了项目规则。

### 5. 指定相关文件或代码

在 VS Code 中可以：

- 打开相关文件后再提问；
- 选中一段代码，让 Codex 解释或修改；
- 使用输入框中的文件添加功能；
- 当前版本支持时，用 `@` 指定文件。

例如：

```text
请检查 @src/config.py 和 @tests/test_config.py。
解释配置文件缺失时的处理流程，只分析，不修改。
```

### 6. 提交一个清晰任务

```text
目标：配置文件不存在时显示清晰的错误信息。
范围：只修改配置加载模块和对应测试。
限制：不要改变公开接口，不要修改其他模块。
验证：补充缺失文件场景的测试，并运行相关测试。
完成后：列出修改文件、测试结果和剩余问题。
```

任务应尽量包含目标、范围、限制和验证方式，避免只说“帮我把项目改好”。

### 7. 使用 Skill 审查结果

如果项目中有前面的代码审查 Skill，可以输入：

```text
请使用 $code-review 审查当前 Git diff，只报告问题，不修改文件。
```

### 8. 在 VS Code 中检查改动

Codex 完成后：

1. 打开“源代码管理”面板；
2. 逐个查看修改文件；
3. 检查是否出现任务外改动；
4. 确认测试是否真的运行；
5. 不理解的修改应让 Codex 解释，不能只看总结。

OpenAI 官方文档建议在任务前后建立 Git 检查点，以便恢复不满意的修改。

---

## 六、推荐的实际工作流程

### 第一步：开始前检查

```powershell
git status
```

确认已有修改，避免 Codex 覆盖自己的工作。

### 第二步：让 Codex 读取规则并分析

```text
请先总结当前生效的 AGENTS.md 规则和可用 Skills。
然后分析这个问题的原因，先不要修改文件。
```

### 第三步：确认方案后修改

```text
按最小方案修复，只修改必要文件，保持公开接口不变，
补充测试并运行相关测试。
```

### 第四步：使用 Skill 审查

```text
请使用 $code-review 审查当前修改，只报告问题。
```

### 第五步：人工查看并提交

```powershell
git diff
git status
```

确认差异和测试结果后，再提交本次任务文件。

整个流程可以概括为：

```text
打开项目 → 读取 AGENTS.md → 分析问题 → 小范围修改
→ 运行测试 → 使用 Skill 审查 → 查看 Git diff → 提交
```

使用时记住三点：

1. Codex 的文字总结不能代替真实的测试和 Git diff；
2. 只给予完成任务所需的权限；
3. 不要把密码、API 密钥或访问令牌写入提示词、`AGENTS.md` 或 `SKILL.md`。

---

## 参考资料

### OpenAI 官方资料

1. [使用 ChatGPT：Chat、Work 与 Codex](https://developers.openai.com/zh-Hans/docs/use-chatgpt)
2. [Codex IDE 扩展](https://developers.openai.com/zh-Hans/docs/codex/ide)
3. [使用 AGENTS.md 自定义指令](https://developers.openai.com/zh-Hans/docs/agent-configuration/agents-md)
4. [构建 Skills](https://developers.openai.com/zh-Hans/docs/build-skills)
5. [Codex 配置参考](https://developers.openai.com/zh-Hans/docs/config-file/config-reference)

### 用户指定的参考教程

1. [VSCode 中使用 Codex：命令、Agent 与 Skills 完整指南](https://jishuzhan.net/article/2053301309797892098)，重点参考第八节 `AGENTS.md` 和第九节 Skills。
2. [在 VS Code 中使用 Codex｜CodexGuide](https://codexguide.ai/start/13-ide-vscode.html)

第三方教程适合帮助理解操作过程；安装入口、文件位置和功能支持如有变化，应以 OpenAI 官方文档为准。
