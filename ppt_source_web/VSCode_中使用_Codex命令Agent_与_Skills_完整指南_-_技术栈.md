<!--
  Source: https://jishuzhan.net/article/2053301309797892098
  Crawled: 2026-09-20T17:06:28.715539
-->

# VSCode 中使用 Codex：命令、Agent 与 Skills 完整指南 - 技术栈

> 最近很多开发者开始从 Claude Code、Cursor、Copilot 等工具转向或尝试使用 OpenAI Codex。相比单纯在网页中提问，Codex 更适合直接进入项目工程，读取代码、分析结构、修改文件、生成文档、排查报错。

### 前言

最近很多开发者开始从 Claude Code、Cursor、Copilot 等工具转向或尝试使用 OpenAI Codex。相比单纯在网页中提问，Codex 更适合直接进入项目工程，读取代码、分析结构、修改文件、生成文档、排查报错。

本文主要基于 **VSCode 使用场景** 来整理 Codex 的使用方式。也就是说，我们不是以纯命令行为主，而是以 **VSCode 插件 + 项目配置 + Agent + Skills** 的方式来使用 Codex。

Codex 官方支持通过 IDE 扩展在 VSCode、Cursor、Windsurf 等编辑器中使用，并可以读取编辑器中的文件、选区和项目上下文。官方也提供了 VSCode 命令面板命令、Slash commands、[AGENTS.md](http://AGENTS.md)、Skills、Subagents、自定义 Agents 等能力。([OpenAI 开发者](https://developers.openai.com/codex/ide?utm_source=chatgpt.com))

---

### 一、本文适合谁阅读

本文适合以下几类人：

- 想在 **VSCode** 中使用 Codex 的开发者；
- 想把 Codex 用在真实项目中的初学者；
- 想了解 `AGENTS.md`、`Skills`、`Subagents` 的用户；
- 想从 Claude Code 迁移到 Codex 的用户；
- 希望用 Codex 辅助完成后端、前端、数据库、文档生成、代码审查的开发者。

本文以 Windows + VSCode 为主要使用环境，示例项目目录使用：

text 复制代码

```
D:\ai\test
```

你可以根据自己的项目路径替换。

---

### 二、Codex 在 VSCode 中的推荐使用方式

如果你主要使用 VSCode，那么 Codex 的最佳使用方式不是一直在终端里敲命令，而是：

text 复制代码

```
VSCode Codex 扩展：日常对话、读取文件、修改代码
VSCode 命令面板：添加选中代码、添加当前文件、实现 TODO
VSCode 终端：安装、检查版本、执行一次性命令
AGENTS.md：项目长期规则
.agents/skills：专项能力包
.codex/agents：自定义 Agent
.codex/config.toml：Codex 配置
```

也就是说，最终你应该形成这样一套使用习惯：

text 复制代码

```
打开 VSCode 项目
→ 打开 Codex 侧边栏
→ 让 Codex 读取 AGENTS.md
→ 选中文件或代码加入上下文
→ 使用 Skill 或 Agent 完成专项任务
→ 查看 diff
→ 测试项目
```

Codex IDE 扩展支持在编辑器中使用打开的文件、选中的代码片段和 `@file` 引用来提供上下文，也可以在 IDE 内切换模型、调整审批模式、委派云端任务、使用 Slash commands。([OpenAI 开发者](https://developers.openai.com/codex/ide?utm_source=chatgpt.com))

---

### 三、安装 Codex VSCode 扩展

#### 1. 在 VSCode 中安装

打开 VSCode，进入扩展市场：

text 复制代码

```
Extensions
→ 搜索 Codex
→ 安装 OpenAI Codex 扩展
```

也可以通过命令面板打开扩展安装页面：

text 复制代码

```
Ctrl + Shift + P
→ 输入 Extensions: Install Extensions
→ 搜索 Codex
```

安装完成后，Codex 会出现在 VSCode 左侧边栏中。如果没有看到，可以在命令面板中搜索 Codex 相关命令。官方 Quickstart 说明，安装 IDE 扩展后 Codex 会显示在编辑器侧边栏中，并需要登录后开始使用。([OpenAI 开发者](https://developers.openai.com/codex/quickstart?utm_source=chatgpt.com))

---

### 四、VSCode 中 Codex 的常用命令

在 VSCode 中按下：

text 复制代码

```
Ctrl + Shift + P
```

然后搜索：

text 复制代码

```
Codex
```

你会看到一批 Codex 相关命令。

#### 常用命令说明

| 命令 | 作用 | 使用场景 |
| --- | --- | --- |
| Open Codex Sidebar | 打开 Codex 侧边栏 | 日常使用入口 |
| New Codex Panel | 新建 Codex 面板 | 多任务处理 |
| New Chat | 新建对话 | 开始新任务 |
| Add selected text to thread | 把选中的代码加入当前对话 | 分析某段代码 |
| Add file to thread | 把整个当前文件加入对话 | 分析完整文件 |
| Implement TODO | 实现选中的 TODO 注释 | 根据 TODO 自动补代码 |

Codex 官方 IDE 命令文档列出了这些命令，例如 `chatgpt.addToThread` 用于添加选中代码，`chatgpt.addFileToThread` 用于添加整个文件，`chatgpt.implementTodo` 用于实现 TODO，`chatgpt.openSidebar` 用于打开 Codex 侧边栏。([OpenAI 开发者](https://developers.openai.com/codex/ide/commands?utm_source=chatgpt.com))

---

### 五、VSCode 中最推荐的新手使用流程

第一次打开项目时，不建议直接让 Codex 修改代码。建议先让它只读分析项目结构。

#### 第一步：打开整个项目目录

不要只打开单个文件，应该打开整个项目文件夹：

text 复制代码

```
File
→ Open Folder
→ 选择项目根目录
```

例如：

text 复制代码

```
D:\ai\test
```

这样 Codex 才能读取整个项目结构。

---

#### 第二步：让 Codex 只读分析项目

在 Codex 侧边栏输入：

text 复制代码

```
请只读分析当前项目，不要修改任何文件。

请说明：
1. 后端入口在哪里
2. 前端入口在哪里
3. 数据库相关代码在哪里
4. 启动命令是什么
5. 当前项目可能有哪些风险点
```

---

#### 第三步：让 Codex 给修改方案

text 复制代码

```
请根据当前项目结构，告诉我如果要修改"任务恢复"和"分页显示"，会涉及哪些文件。
暂时不要修改。
```

---

#### 第四步：确认方案后再修改

text 复制代码

```
可以按方案修改。

要求：
1. 只修改必要文件
2. 不要动无关代码
3. 不要删除数据
4. 涉及数据库只给 SQL，不要直接执行
5. 修改完成后给出测试步骤
```

---

#### 第五步：查看修改结果

修改完成后，可以在 VSCode 左侧的 Source Control 中查看变更，也可以让 Codex 总结：

text 复制代码

```
请总结本次修改：
1. 修改了哪些文件
2. 每个文件改了什么
3. 是否涉及数据库 SQL
4. 是否涉及删除逻辑
5. 后端如何启动
6. 前端如何启动
7. 如何验证功能
8. 如何回滚
```

---

### 六、VSCode 终端中的 Codex 命令

虽然本文主要讲 VSCode 使用方式，但 VSCode 终端仍然很重要。

#### 1. 安装 Codex CLI

如果你希望在 VSCode 终端里使用 Codex CLI，可以执行：

powershell 复制代码

```
npm install -g @openai/codex
```

检查版本：

powershell 复制代码

```
codex --version
```

Codex CLI 是 OpenAI 的本地编码 Agent，可以在终端中读取、修改和运行当前目录中的代码。官方文档说明，Codex CLI 可以通过 npm 或 Homebrew 安装。([OpenAI 开发者](https://developers.openai.com/codex/cli?utm_source=chatgpt.com))

---

#### 2. 进入项目目录

powershell 复制代码

```
cd D:\ai\test
```

---

#### 3. 只读分析项目

powershell 复制代码

```
codex --sandbox read-only --ask-for-approval on-request
```

适合第一次分析项目、检查代码、看报错。

---

#### 4. 允许修改当前工作区

powershell 复制代码

```
codex --sandbox workspace-write --ask-for-approval on-request
```

适合确认方案之后，让 Codex 修改当前项目内的代码。

---

#### 5. 一次性生成项目分析报告

powershell 复制代码

```
codex exec "分析当前项目结构，输出后端、前端、数据库、任务队列、目录监听相关模块"
```

---

#### 6. 检查危险删除逻辑

powershell 复制代码

```
codex exec --sandbox read-only "检查当前项目中是否存在 DELETE、TRUNCATE、DROP、shutil.rmtree、os.remove、rmdir /s /q 等危险操作"
```

Codex CLI 官方参考文档列出了 `--sandbox`、`--ask-for-approval`、`--cd`、`--model`、`--image`、`exec` 等命令和参数，并说明命令行参数可以覆盖 `config.toml` 中的默认配置。([OpenAI 开发者](https://developers.openai.com/codex/cli/reference?utm_source=chatgpt.com))

---

### 七、VSCode 中的 Slash Commands

在 Codex 聊天输入框中输入：

text 复制代码

```
/
```

可以打开 Slash commands。

常用命令包括：

| 命令 | 作用 |
| --- | --- |
| `/status` | 查看当前状态 |
| `/model` | 切换模型 |
| `/permissions` | 调整权限 |
| `/diff` | 查看修改差异 |
| `/compact` | 压缩长上下文 |
| `/clear` | 清空当前对话上下文 |

Codex IDE 扩展支持在聊天输入框中使用 Slash commands，用于查看状态、切换模式、发送反馈等；Codex CLI 中的 Slash commands 还支持切换模型、调整权限、总结长对话等能力。([OpenAI 开发者](https://developers.openai.com/codex/ide/slash-commands?utm_source=chatgpt.com))

---

### 八、[AGENTS.md](http://AGENTS.md)：给 Codex 的项目说明书

#### 1. [AGENTS.md](http://AGENTS.md) 是什么？

`AGENTS.md` 可以理解为"写给 Codex 看的项目说明书"。

`README.md` 通常是写给人看的，而 `AGENTS.md` 是写给 AI Agent 看的。它可以告诉 Codex：

text 复制代码

```
项目是什么
技术栈是什么
启动命令是什么
哪些文件不能随便改
数据库修改要注意什么
删除操作有哪些限制
代码风格是什么
任务完成后要输出什么
```

官方文档说明，Codex 会在开始工作前读取 `AGENTS.md`，可以通过全局规则和项目级规则叠加，让不同仓库拥有一致的工作要求。([OpenAI 开发者](https://developers.openai.com/codex/guides/agents-md?utm_source=chatgpt.com))

---

#### 2. [AGENTS.md](http://AGENTS.md) 放在哪里？

项目级文件建议放在项目根目录：

text 复制代码

```
D:\ai\test\AGENTS.md
```

如果是全局规则，可以放在：

text 复制代码

```
C:\Users\你的用户名\.codex\AGENTS.md
```

项目级规则适合记录当前项目特有的要求，全局规则适合记录你个人长期使用习惯。

---

#### 3. [AGENTS.md](http://AGENTS.md) 示例

md 复制代码

```
# AGENTS.md

## 项目背景

这是一个本地部署的 xxxxx管理系统，用于xxxxxxx。

## 技术栈

- 后端：FastAPI + Uvicorn
- 前端：前后端分离
- 数据库：MySQL
- 目录监听：watchdog

## 工作规则

- 修改代码前，必须先阅读项目结构。
- 修改前必须说明会影响哪些文件。
- 修改后必须给出启动命令和测试步骤。
- 不允许把所有功能堆在一个页面或一个文件里。
- 不允许把 HTML 写死在 Python 字符串中。
- 不允许默认使用 SQLite，数据库优先使用 MySQL。
- 涉及数据库结构修改时，必须给出完整 SQL。
- 涉及删除文件、删除结果、清空数据库时，必须有二次确认、操作日志和回滚说明。

## 输出规范

- 原图文件名不能被破坏。
- xxxxx
- xxxxx
- xxxxx
- JSON 输出需要稳定，可供其他系统对接。

## 完成标准

每次任务完成后必须说明：

1. 修改了哪些文件。
2. 每个文件修改了什么。
3. 如何启动后端。
4. 如何启动前端。
5. 如何验证功能。
6. 是否涉及数据库 SQL。
7. 是否存在风险和回滚方式。
```

---

### 九、Skills：给 Codex 增加专项能力

#### 1. Skills 是什么？

Skills 可以理解为 Codex 的"专项工作手册"。

比如你经常让 Codex 做这些事情：

text 复制代码

```
检查 YOLO 项目代码
生成 MySQL 迁移 SQL
检查危险删除逻辑
整理 MQTT 设备 API 文档
重构前端页面
生成测试步骤
```

这些重复性的要求，就可以封装成一个 Skill。

官方说明中，Skill 是一个目录，里面必须包含 `SKILL.md`，也可以包含脚本、参考文档、资源文件等。Codex 可以通过 Skills 获得特定任务的流程和专业知识。([OpenAI 开发者](https://developers.openai.com/codex/skills?utm_source=chatgpt.com))

---

#### 2. Skills 放在哪里？

项目级 Skills 建议放在：

text 复制代码

```
D:\ai\test\.agents\skills\
```

目录示例：

text 复制代码

```
D:\ai\test\
├─ AGENTS.md
├─ .agents\
│  └─ skills\
│     ├─ code-review\
│     │  └─ SKILL.md
│     ├─ mysql-safe-migration\
│     │  └─ SKILL.md
│     └─ dangerous-delete-guard\
│        └─ SKILL.md
```

---

#### 3. 在 VSCode 中如何调用 Skill？

在 Codex 聊天框中直接输入：

text 复制代码

```
请使用 $code-review 检查当前项目的任务队列和断点续扫逻辑。
```

或者：

text 复制代码

```
请使用 $mysql-safe-migration 生成本次数据库修改 SQL、备份 SQL、回滚 SQL。
```

或者：

text 复制代码

```
请使用 $dangerous-delete-guard 检查当前项目是否存在高风险删除逻辑。
```

---

### 十、Skill 示例一：代码审查

文件路径：

text 复制代码

```
D:\ai\helmet\.agents\skills\yolo-code-review\SKILL.md
```

内容：

md 复制代码

```
---
name: code-review
description: 当任务涉及 xxxxx管理系统、FastAPI 后端、MySQL、watchdog 监听、任务队列、断点续扫、分页、识别结果 JSON 输出时使用。
---

#代码审查 Skill

## 使用场景

当用户要求检查或修改以下内容时使用：

- xxxxx管理系统
- FastAPI 后端
- MySQL 数据库
- watchdog 目录监听
- 任务队列
- 断点续扫
- 分页
- 输出结果
- 识别结果 JSON

## 工作流程

1. 先阅读项目结构，不要直接修改。
2. 找到后端入口、数据库模型、任务服务、监听服务、前端页面。
3. 修改前说明会影响哪些文件。
4. 涉及数据库变更时给出完整 SQL。
5. 涉及删除功能时必须要求二次确认、操作日志和回滚方式。
6. 修改完成后给出启动命令、测试步骤和风险点。

## 禁止事项

- 不允许默认清空数据库。
- 不允许删除模型权重文件。
- 不允许把 HTML 写死在 Python 字符串里。
- 不允许只改前端不改后端接口。
- 不允许破坏原始图片文件名。
```

---

### 十一、Skill 示例二：MySQL 安全迁移

文件路径：

text 复制代码

```
D:\ai\test\.agents\skills\mysql-safe-migration\SKILL.md
```

内容：

md 复制代码

```
---
name: mysql-safe-migration
description: 当任务涉及 MySQL 表结构修改、数据迁移、清库、删除识别结果、DELETE、TRUNCATE、DROP、备份和回滚时使用。
---

# MySQL 安全迁移 Skill

## 触发场景

- 修改 MySQL 表结构
- 新增字段
- 删除字段
- 清理识别结果
- 删除任务数据
- 批量删除 JSON 或图片
- 使用 DELETE / TRUNCATE / DROP
- 生成数据库升级 SQL

## 工作步骤

1. 先识别涉及哪些表。
2. 判断是否会影响历史数据。
3. 给出备份 SQL。
4. 给出迁移 SQL。
5. 给出回滚 SQL。
6. 给出验证 SQL。
7. 对 DELETE / TRUNCATE / DROP 做高风险提示。

## 输出格式

必须输出：

- 涉及表
- 风险等级
- 执行前备份 SQL
- 正式执行 SQL
- 回滚 SQL
- 验证 SQL
- 注意事项

## 禁止事项

- 不允许直接清空数据库。
- 不允许没有 WHERE 的 DELETE。
- 不允许没有备份方案的 DROP / TRUNCATE。
- 不允许忽略外键、索引、历史数据兼容问题。
```

---

### 十二、Skill 示例三：危险删除保护

文件路径：

text 复制代码

```
D:\ai\test\.agents\skills\dangerous-delete-guard\SKILL.md
```

内容：

md 复制代码

```
---
name: dangerous-delete-guard
description: 当任务涉及删除文件、删除目录、删除数据库记录、清空识别结果、shutil.rmtree、os.remove、rm、rmdir、DELETE、TRUNCATE、DROP 时使用。
---

# 危险删除保护 Skill

## 检查范围

需要重点检查：

- Python: os.remove
- Python: os.unlink
- Python: shutil.rmtree
- Shell: rm -rf
- Windows: rmdir /s /q
- SQL: DELETE
- SQL: TRUNCATE
- SQL: DROP
- 前端批量删除按钮
- 后端批量删除接口

## 强制要求

任何删除功能必须包含：

1. 二次确认。
2. 删除范围预览。
3. 操作日志。
4. 操作人或来源记录。
5. 删除数量统计。
6. 异常回滚或失败记录。
7. 不允许删除模型权重文件。
8. 不允许误删 raw 原始图片。

## 输出格式

请输出：

- 高风险代码位置
- 风险说明
- 可能后果
- 推荐修复方式
- 是否必须立即修改
```

---

### 十三、自定义 Agent：让 Codex 拥有不同角色

#### 1. Agent 和 Skill 的区别

很多人容易把 Agent 和 Skill 混在一起，可以这样理解：

| 类型 | 作用 |
| --- | --- |
| [AGENTS.md](http://AGENTS.md) | 项目总规则 |
| Skill | 某类任务的操作手册 |
| Custom Agent | 一个专门负责某类任务的角色 |
| Subagents | 多个 Agent 并行分析或执行任务 |

例如：

text 复制代码

```
project_explorer：只读分析项目结构
reviewer：专门做代码审查
mysql_guardian：专门检查数据库风险
```

官方 Subagents 文档说明，Codex 可以派生多个子 Agent 并行工作，等待它们完成后汇总结果；自定义 Agent 可以放在 `~/.codex/agents/` 或项目级 `.codex/agents/` 中。([OpenAI 开发者](https://developers.openai.com/codex/subagents?utm_source=chatgpt.com))

---

#### 2. 自定义 Agent 放在哪里？

项目级 Agent 建议放在：

text 复制代码

```
D:\ai\test\.codex\agents\
```

目录结构：

text 复制代码

```
D:\ai\test\
├─ .codex\
│  ├─ config.toml
│  └─ agents\
│     ├─ project-explorer.toml
│     ├─ reviewer.toml
│     └─ mysql-guardian.toml
```

---

### 十四、自定义 Agent 示例

#### 1. 项目探索 Agent

文件路径：

text 复制代码

```
D:\ai\test\.codex\agents\project-explorer.toml
```

内容：

toml 复制代码

```
name = "project_explorer"
description = "只读项目结构分析 Agent，用于在修改代码前梳理目录、模块、调用链和风险点。"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"

developer_instructions = """
你是只读项目探索 Agent。

你的任务：
1. 阅读项目结构。
2. 定位后端入口。
3. 定位前端入口。
4. 定位数据库模型。
5. 定位任务队列和目录监听逻辑。
6. 输出风险点和下一步建议。

禁止修改任何文件。
"""
```

---

#### 2. 代码审查 Agent

文件路径：

text 复制代码

```
D:\ai\test\.codex\agents\reviewer.toml
```

内容：

toml 复制代码

```
name = "reviewer"
description = "代码审查 Agent，重点检查正确性、安全风险、测试缺失和可维护性。"
model_reasoning_effort = "high"
sandbox_mode = "read-only"

developer_instructions = """
你是严格的代码审查 Agent。

重点检查：
1. 逻辑错误
2. 安全问题
3. 数据库风险
4. 删除操作风险
5. 并发问题
6. 测试缺失
7. 可维护性问题

不要修改代码，只输出审查结果。
每个问题必须包含：
- 问题位置
- 风险说明
- 修改建议
- 是否必须修复
"""
```

---

#### 3. 数据库安全 Agent

文件路径：

text 复制代码

```
D:\ai\test\.codex\agents\mysql-guardian.toml
```

内容：

toml 复制代码

```
name = "mysql_guardian"
description = "MySQL 数据库安全 Agent，用于检查表结构修改、DELETE、TRUNCATE、DROP、清库、迁移和回滚风险。"
model_reasoning_effort = "high"
sandbox_mode = "read-only"

developer_instructions = """
你是 MySQL 数据库安全 Agent。

重点检查：
1. 是否存在 DROP / TRUNCATE / DELETE 无条件执行
2. 是否缺少事务
3. 是否缺少备份方案
4. 是否缺少回滚 SQL
5. 是否影响历史识别结果
6. 是否存在连接池耗尽风险
7. 是否存在字段兼容问题

不要直接执行数据库命令。

输出必须包含：
- 风险等级
- 涉及表
- 涉及 SQL
- 修复建议
- 备份方案
- 回滚方案
"""
```

---

### 十五、VSCode 中如何使用多个 Agent

在 Codex 聊天框中输入：

text 复制代码

```
请启动 3 个 subagents 并行分析当前项目：

1. project_explorer：分析项目结构、入口文件和调用链。
2. reviewer：检查代码质量、安全风险和测试缺失。
3. mysql_guardian：检查 MySQL 表结构、删除逻辑和迁移风险。

要求：
- 不要修改文件。
- 每个 Agent 单独输出发现。
- 最后由主 Agent 汇总成一份修改优先级清单。
```

这种方式适合：

text 复制代码

```
大项目整体审查
前后端同时修改前的风险分析
数据库迁移前检查
删除功能上线前检查
任务队列和并发问题排查
```

但注意：Subagents 会消耗更多上下文和 token，不适合简单问题。官方也说明 Codex 只会在用户明确要求时创建新的 Agent。([OpenAI 开发者](https://developers.openai.com/codex/subagents?utm_source=chatgpt.com))

---

### 十六、Codex 配置文件 config.toml

#### 1. 配置文件位置

用户级配置：

text 复制代码

```
C:\Users\你的用户名\.codex\config.toml
```

项目级配置：

text 复制代码

```
D:\ai\test\.codex\config.toml
```

Codex 配置文档说明，`config.toml` 用于配置模型、审批策略、沙箱、MCP 等内容；Codex CLI 会继承 `~/.codex/config.toml` 中的大多数默认设置。([OpenAI 开发者](https://developers.openai.com/codex/config-reference?utm_source=chatgpt.com))

---

#### 2. 推荐配置

toml 复制代码

```
approval_policy = "on-request"
sandbox_mode = "workspace-write"

[agents]
max_threads = 4
max_depth = 1
```

如果你主要使用 VSCode，不建议过度依赖 profile。官方高级配置文档中说明，profiles 目前主要用于 CLI，暂不支持 Codex IDE extension。([OpenAI 开发者](https://developers.openai.com/codex/config-advanced?utm_source=chatgpt.com))

如果你使用 CLI，可以再增加：

toml 复制代码

```
[profiles.readonly]
approval_policy = "on-request"
sandbox_mode = "read-only"

[profiles.dev]
approval_policy = "on-request"
sandbox_mode = "workspace-write"

[profiles.strict]
approval_policy = "untrusted"
sandbox_mode = "read-only"
```

然后在终端中使用：

powershell 复制代码

```
codex --profile readonly
```

或者：

powershell 复制代码

```
codex --profile dev
```

---

### 十七、推荐项目目录结构

如果你想长期稳定使用 Codex，建议项目结构整理成这样：

text 复制代码

```
D:\ai\test\
├─ AGENTS.md
├─ .codex\
│  ├─ config.toml
│  └─ agents\
│     ├─ project-explorer.toml
│     ├─ reviewer.toml
│     └─ mysql-guardian.toml
├─ .agents\
│  └─ skills\
│     ├─ code-review\
│     │  └─ SKILL.md
│     ├─ mysql-safe-migration\
│     │  └─ SKILL.md
│     ├─ dangerous-delete-guard\
│     │  └─ SKILL.md
│     ├─ mqtt-api-doc-writer\
│     │  └─ SKILL.md
│     └─ frontend-page-refactor\
│        └─ SKILL.md
├─ backend\
├─ frontend\
├─ README.md
└─ requirements.txt
```

---

### 十八、VSCode 中最常用的提示词模板

#### 1. 只读分析项目

text 复制代码

```
请读取 AGENTS.md，并只读分析当前项目结构。
不要修改任何文件。

请告诉我：
1. 项目整体结构
2. 后端入口
3. 前端入口
4. 数据库相关文件
5. 任务队列相关文件
6. 目录监听相关文件
7. 当前项目主要风险点
```

---

#### 2. 修改前给方案

text 复制代码

```
请给出修改方案。
要求说明：
1. 要修改哪些文件
2. 每个文件为什么要修改
3. 是否涉及数据库
4. 是否涉及删除操作
5. 风险点是什么
6. 如何验证

暂时不要修改。
```

---

#### 3. 使用 Skill 检查项目

text 复制代码

```
请使用 $code-review 检查当前项目的任务队列、watchdog 监听、断点续扫和分页逻辑。
先给出问题清单和修改方案，不要直接修改。
```

---

#### 4. 使用 Skill 检查删除风险

text 复制代码

```
请使用 $dangerous-delete-guard 检查当前项目中所有删除相关逻辑。

重点搜索：
- os.remove
- os.unlink
- shutil.rmtree
- rm -rf
- rmdir /s /q
- DELETE
- TRUNCATE
- DROP
- 批量删除接口
- 前端删除按钮

不要修改文件，只输出风险清单和修复建议。
```

---

#### 5. 使用 Skill 生成数据库迁移 SQL

text 复制代码

```
请使用 $mysql-safe-migration 分析这次数据库修改需求。

要求输出：
1. 涉及表
2. 备份 SQL
3. 修改 SQL
4. 回滚 SQL
5. 验证 SQL
6. 风险说明

不要直接执行 SQL。
```

---

#### 6. 多 Agent 并行审查项目

text 复制代码

```
请启动 3 个 subagents 并行审查当前项目：

1. project_explorer：只读分析项目结构和调用链。
2. reviewer：检查代码正确性、安全性和测试缺失。
3. mysql_guardian：检查数据库结构、删除逻辑和迁移风险。

要求：
- 不要直接修改代码。
- 每个 Agent 单独输出发现。
- 最后由主 Agent 汇总成一份修改优先级清单。
```

---

#### 7. 修改完成后总结

text 复制代码

```
请总结本次修改：

1. 修改了哪些文件
2. 每个文件修改了什么
3. 是否涉及数据库
4. 是否涉及删除操作
5. 如何启动后端
6. 如何启动前端
7. 如何验证功能
8. 如何回滚
```

---

### 十九、初学者使用 Codex 的注意事项

#### 1. 不要一上来就让 Codex 改代码

错误示例：

text 复制代码

```
帮我把整个项目优化一下。
```

更好的写法：

text 复制代码

```
请先只读分析当前项目结构，不要修改文件。
然后告诉我如果要优化任务恢复逻辑，需要改哪些文件。
```

---

#### 2. 涉及数据库时，不要让 Codex 直接执行 SQL

建议这样说：

text 复制代码

```
涉及数据库的部分只给 SQL，不要直接执行。
请同时给出备份 SQL、修改 SQL、回滚 SQL 和验证 SQL。
```

---

#### 3. 涉及删除功能时，一定要加限制

建议这样说：

text 复制代码

```
涉及删除文件、删除结果、清空数据库的功能，必须有二次确认、删除范围预览、操作日志和回滚说明。
```

---

#### 4. 不要只打开单个文件

使用 Codex 时，建议打开完整项目目录。否则 Codex 很难理解项目结构，也容易改错地方。

---

#### 5. 长会话要及时压缩或新开对话

如果你在一个任务中连续修改很多轮，可以使用：

text 复制代码

```
/compact
```

或者新建一个 Codex 对话，让上下文更清晰。

---

### 二十、最终建议

如果你主要在 VSCode 中使用 Codex，我建议你优先掌握这 6 件事：

text 复制代码

```
1. 打开完整项目目录
2. 打开 Codex 侧边栏
3. 使用 Add selected text to thread
4. 使用 Add file to thread
5. 编写 AGENTS.md
6. 使用 $skill-name 调用 Skills
```

然后再逐步掌握：

text 复制代码

```
.codex/config.toml
.codex/agents
.agents/skills
Subagents
Slash commands
Codex CLI
```

对真实项目来说，最推荐的组合是：

text 复制代码

```
AGENTS.md：项目总规则
Skills：专项操作手册
Custom Agents：专业角色
Subagents：多角色并行审查
config.toml：默认配置
VSCode Codex 扩展：日常主入口
```

一句话总结：

text 复制代码

```
在 VSCode 中使用 Codex，最好的方式不是直接让它乱改代码，而是：
先用 AGENTS.md 定规则，
再用 Skills 固化流程，
再用 Agent 分工审查，
最后让 Codex 在明确边界内修改和验证。
```

---

### 参考资料

本文主要参考 OpenAI Codex 官方文档，包括 Codex IDE 扩展、IDE 命令、[AGENTS.md](http://AGENTS.md)、Skills、Subagents、CLI Reference 和配置文档。([OpenAI 开发者](https://developers.openai.com/codex/ide?utm_source=chatgpt.com))