<!-- ppt-master-schema: design-spec/v1 -->
# Codex, Git and Reproducible Research Workflow - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | Codex、Git 与可复现科研工作流 |
| Canvas Format | PPT 16:9, 1280 × 720 |
| Page Count | 16 |
| Primary Language | zh-CN |
| Target Audience | 课题组导师与研究生；多数人熟悉 ChatGPT 和 VS Code，但对 Codex、Git 以及两者在科研中的协同方式了解程度不同 |
| Communication Intent | 先建立 Codex 的正确认知并讲清其在 VS Code 中的基本使用，再补充 Git 的原理与日常操作，最后把两者组合成可追踪、可复现的科研工作流 |
| Desired Audience Outcome | 听众能说清 Codex 与 ChatGPT 的区别，理解典型 Codex 项目文件的作用，掌握 VS Code 中的基本操作与 Git 的核心流程，并能把这套方法迁移到自己的科研项目 |
| Core Message / Ask / Action | Codex 负责在项目上下文中理解并执行任务，Git 负责记录、比较和恢复每一次变化；两者结合，才能把 AI 辅助编程变成可信、可复现的科研实践 |
| Delivery Context | 主要用于约 20–25 分钟、有主讲人的中文课题组现场汇报；次要用于会后独立浏览和新人上手 |
| Artifact Afterlife | 作为课题组内部培训、会后复习和科研项目协作规范的入门材料长期留存 |
| Reading Mode | balanced |
| Content Strategy | 在源材料范围内进行合理发散，不要偏离主题就行 |
| Design Style | 编辑器叙事工作台：浅色编辑式版面与真实 VS Code 工作区贯穿全篇 |
| AI Image Acquisition Path | not applicable |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — final Stage-2 proactive policy confirmed in chat |
| Custom Animations | disabled — final Stage-2 proactive policy confirmed in chat |
| Narration Audio | disabled — final Stage-2 proactive policy confirmed in chat |
| Created Date | 2026-09-20 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | ppt169 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 64 px safe margin on all sides |
| Content Area | x=64..1216, y=64..656 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: instructional, narrative
- **Mode Behavior**: 以逐步教学为主线，并用“从会聊天到会执行，再到可复现”的转折推进：先回答 Codex 是什么，接着示范项目结构和 VS Code 操作，再引入 Git，最后在科研闭环中完成收束。每页只承担一个清晰学习动作，章节入口通过工作状态变化衔接。
- **Visual style**: custom
- **Visual Style References**: editorial, soft-rounded
- **Visual Style Behavior**: 以右侧编辑器或终端界面为持续视觉锚点，左侧使用编辑式大标题、细规则与少量圆角说明块；页面保持浅色大留白，步骤、路径和关键命令用蓝色标注。融合出版式层级与友好圆角容器，但弱化卡片堆叠，让同一张“研究工作台”贯穿全篇。
- **Theme**: 一条由 Codex、Git 到科研复现的三段式工作轨道；窗口标题栏、文件路径和提交节点作为跨页识别元素。
- **Tone**: 清楚、克制、可信，像一份能直接照着操作的科研工作台说明。

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #F6F8FB | 全局浅色工作区背景 |
| Secondary background | #FFFFFF | 截图承载区、正文面板与代码窗口 |
| Primary | #14213D | 标题、主线结构和深色编辑器外框 |
| Accent | #377DFF | 当前步骤、命令、路径与 Codex 重点 |
| Secondary accent | #20B8CD | Git 流转、协同关系和完成状态 |
| Body text | #1D2939 | 正文与主要标签 |
| Secondary text | #667085 | 注释、来源、次级说明 |
| Divider | #D9E1EC | 细规则、边框与界面分隔 |
| Surface | #FFFFFF | 浮层与浅色内容面 |
| Grid | #E9EEF5 | 低对比网格与流程轨道 |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 现代编辑式无衬线，清晰而不生硬 | Microsoft YaHei | Arial | sans-serif |
| Body | 中性、适合投影阅读的无衬线 | Microsoft YaHei | Arial | sans-serif |
| Code | 等宽、用于路径与命令 | Consolas | Consolas | monospace |

- **Title stack**: Microsoft YaHei, Arial, sans-serif
- **Body stack**: Microsoft YaHei, Arial, sans-serif
- **Code stack**: Consolas, monospace
- **Role rationale**: Code 为跨多页重复出现的命令、文件名、路径和 Git 操作提供稳定的等宽识别。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Cover title | 64 |
| Chapter title | 52 |
| Title | 44 |
| Subtitle | 32 |
| Lead | 30 |
| Body | 24 |
| Code | 20 |
| Annotation | 18 |
| Footnote | 14 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 先读左侧结论或问题，再进入右侧工作区、流程或证据，最后回到页底的一句行动提示。
- **Composition tendency**: 非对称编辑式分栏；界面截图、代码窗口或流程关系承担主要视觉重量，正文只保留能支持现场讲解的必要信息。
- **Cross-page continuity**: 页顶保留三段式进度标识 Codex / Git / Research；编辑器窗口的深色标题栏在需要展示执行与验证时重复出现，章节切换只改变高亮节点。
- **Spacing posture**: 随 page rhythm 在开放与信息密集之间变化，避免连续多页相同卡片网格。
- **Spacing anchors**: page margin 64 px; block gap 24 px; column gutter 36 px; corner radius 18 px; body leading 36 px.

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-outline
- **Stroke Width**: 2
- **Brand-logo library**: simple-icons

| Icon Path | Suitable Scenarios |
| --- | --- |
| tabler-outline/message-circle | 对话与解释 |
| tabler-outline/code | 代码与修改 |
| tabler-outline/folder | 项目结构与上下文 |
| tabler-outline/settings | 项目规则与配置 |
| tabler-outline/terminal-2 | 命令、运行与验证 |
| tabler-outline/git-branch | 分支与版本流转 |
| tabler-outline/stack-2 | 工作区、暂存区与仓库层级 |
| tabler-outline/check | 验证与完成条件 |
| tabler-outline/arrow-right | 顺序和状态推进 |
| tabler-outline/flask | 科研实验与复现 |
| tabler-outline/history | 历史与恢复 |
| tabler-outline/refresh | 迭代循环 |
| simple-icons/git | Git 品牌识别 |
| simple-icons/visualstudiocode | VS Code 品牌识别 |
| simple-icons/openai | OpenAI / Codex 品牌识别 |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P02 | table | comparison_matrix | 对照 ChatGPT 与 Codex 的工作重心、上下文、输出和人的角色 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| exec-c60951e0-9251-4198-bc55-5086aaea3ef7.png | 1672 × 941 | 1.78 | 封面主视觉与整套浅色编辑器叙事方向的身份锚点 | Existing visual direction | 全画布作为开场工作台，保留完整标题、三步说明和右侧编辑器场景 | no-crop | user | Existing | Product Design 方向 3，当前项目已生成并导入 | embedded | hero_page |
| vscode-codex-extension-marketplace.png | 2440 × 946 | 2.58 | 展示 VS Code 中安装或启用 Codex 扩展 | Screenshot | 与另外两张截图组成从安装到使用的顺序证据 | no-crop | user | Existing | https://codexguide.ai/start/13-ide-vscode.html | n/a | local |
| vscode-codex-chat-panel.png | 1938 × 1578 | 1.23 | 展示 Codex 侧边栏和聊天入口 | Screenshot | 作为步骤中部的主截图，突出编辑器内上下文 | no-crop | user | Existing | https://codexguide.ai/start/13-ide-vscode.html | n/a | local |
| vscode-codex-file-reference.png | 1950 × 1538 | 1.27 | 展示使用文件引用提供精确上下文 | Screenshot | 作为步骤末端的局部证据，与上下文提示并列 | no-crop | user | Existing | https://codexguide.ai/start/13-ide-vscode.html | n/a | local |
| 0D32F290-80B0-4EA4-9836-CA58E22569B3.jpg | 707 × 398 | 1.78 | 对比集中式 SVN 与分布式 Git 的仓库关系 | Diagram | 图像承担分布式概念的直观证据，旁边只补一句解释 | no-crop | user | Existing | https://www.runoob.com/git/git-tutorial.html | n/a | local |

## IX. Content Outline

### Part 1: Codex 与 VS Code

#### Slide 01 - Codex + VS Code + Git：科研中的使用方法

- **Audience move**: 从把三者看成零散工具 → 看到一条从想法到可复现结果的完整路径
- **Relationships**: Codex、VS Code、Git 按使用顺序连接，并共同指向可复现科研结果
- **Composition**: 以选定的整幅编辑器工作台视觉建立第一印象，页脚仅补充本次汇报的三段结构。
- **Page rhythm**: anchor
- **Title**: Codex + VS Code + Git：科研中的使用方法
- **Core message**: 更好的工具链，目标不是更快地产生代码，而是更可靠地产生研究结果。
- **Content**:
  - Codex：理解任务并执行修改 · VS Code：观察与交互工作区 · Git：记录、比较与恢复
- **Images**: exec-c60951e0-9251-4198-bc55-5086aaea3ef7.png 完整呈现，不裁切。
- **Cover impact**: 绑定钩子“从想法到可复现结果”；构图以真实研究项目工作台同时出现代码、终端和差异为起点。

#### Slide 02 - ChatGPT 更像思考伙伴，Codex 更像项目执行者

- **Audience move**: 从按“谁更聪明”比较产品 → 按工作中心和交付物选择工具
- **Relationships**: ChatGPT 与 Codex 在四个共同维度上形成对照；两者能力有重叠，但工作重心不同
- **Composition**: 一句结论占据上方，下面用两列对照；最底部用一条共识说明“不是绝对边界”。
- **Page rhythm**: dense
- **Title**: ChatGPT 更像思考伙伴，Codex 更像项目执行者
- **Core message**: ChatGPT 以对话、理解和内容产出为中心；Codex 以代码库、编辑、测试和差异审查为中心。
- **Content**:
  - 工作重心：解释与讨论 / 理解代码库并完成变更
  - 主要上下文：问题、文件与知识 / 仓库、编辑器、终端与 Git
  - 典型交付：答案、方案、文档 / 可审查的代码变更、测试结果与 diff
  - 人的角色：判断内容是否有用 / 定义目标、检查变更并批准关键操作
- **Visualization**: chatgpt-codex-comparison — 两列文本比较矩阵，行是四个比较维度。
- **Native-ready**: chatgpt-codex-comparison=yes
- **Hyperlinks**: “OpenAI ChatGPT 与 Codex 能力概览” → https://learn.chatgpt.com/

#### Slide 03 - Codex 的价值在“闭环执行”，不只在生成代码

- **Audience move**: 从把 Codex 当作代码补全 → 理解它围绕任务完成一轮可验证闭环
- **Relationships**: 目标、读取上下文、计划、修改、运行验证、总结差异按顺序连接；验证结果可返回修改环节
- **Composition**: 一条从左到右的执行轨道贯穿页面，右侧以小型编辑器状态显示“修改 + 测试通过”。
- **Page rhythm**: breathing
- **Title**: Codex 的价值在“闭环执行”，不只在生成代码
- **Core message**: 真正可用的输出不是一段代码，而是经过上下文理解、修改、验证和说明的结果。
- **Content**:
  - 明确目标 → 读取项目 → 拆解计划 → 修改文件 → 运行检查 → 审查 diff → 汇报结果
  - 人在关键节点确认范围、风险和完成标准

#### Slide 04 - Codex 项目没有神秘格式：关键是上下文清楚、边界明确

- **Audience move**: 从寻找“标准 Codex 项目模板” → 能为科研代码组织一个容易理解和验证的目录
- **Relationships**: 项目根目录是父级；规则、说明、代码、测试、数据、配置、结果和文档是职责不同的成员
- **Composition**: 左侧给出科研项目目录树，右侧解释“必需、常见、按需”三类文件职责。
- **Page rhythm**: dense
- **Title**: Codex 项目没有神秘格式：关键是上下文清楚、边界明确
- **Core message**: 好的目录结构让人和 Codex 都能快速回答：规则是什么、代码在哪、如何运行、怎样验证、结果放哪。
- **Content**:
  - `AGENTS.md` 项目规则 · `README.md` 入口说明 · `src/` 代码 · `tests/` 验证
  - `configs/` 参数 · `data/` 数据约定 · `results/` 输出 · `docs/` 方法记录
  - `.gitignore` 排除缓存、密钥、大型原始数据和可再生成文件 · 依赖文件锁定环境

#### Slide 05 - AGENTS.md 规定“怎么做”，Skills 封装“重复怎么做”

- **Audience move**: 从每次重新解释规则 → 知道如何把项目规范和重复流程持久化
- **Relationships**: AGENTS.md 为项目提供持续指令；Skills 为特定任务提供可复用流程；两者共同约束 Codex 的执行
- **Composition**: 中央放置“Codex 执行”核心，左侧规则流、右侧技能流汇入，并以两个最小示例说明差异。
- **Page rhythm**: dense
- **Title**: AGENTS.md 规定“怎么做”，Skills 封装“重复怎么做”
- **Core message**: 把稳定规则写进 AGENTS.md，把多步骤方法封装成 Skill，能减少口头约定和提示词漂移。
- **Content**:
  - AGENTS.md：测试命令、目录约定、提交规则、禁止事项、领域背景
  - Skill：`SKILL.md` 指令 + 可选 scripts / references / assets，按显式点名或任务匹配触发
  - 实践：规则保持短而稳定；技能解决边界清楚、会重复出现的工作流
- **Hyperlinks**: “OpenAI AGENTS.md 文档” → https://learn.chatgpt.com/docs/agent-configuration/agents-md; “OpenAI Skills 文档” → https://learn.chatgpt.com/docs/build-skills

#### Slide 06 - AGENTS.md：写给 Codex 的项目说明书

- **Audience move**: 从知道有一个规则文件 → 理解 Codex 如何发现、叠加并执行不同作用域的项目指令
- **Relationships**: 全局规则、仓库根目录规则和当前目录附近的规则按路径形成指令链；越靠近当前目录的规则越具体
- **Composition**: 左侧用一句定义建立概念，中间以纵向路径展示全局到局部的加载顺序，右侧归纳适合写入的五类内容。
- **Page rhythm**: breathing
- **Title**: AGENTS.md：写给 Codex 的项目说明书
- **Core message**: AGENTS.md 不是临时提示词，而是 Codex 开始工作前读取的、可随项目持续生效的执行约定。
- **Content**:
  - 全局层：`~/.codex/AGENTS.md` 保存个人长期习惯；项目层：仓库根目录 `AGENTS.md` 保存团队约定
  - Codex 从项目根目录向当前工作目录逐层读取；更靠近当前目录的规则在指令链中更晚出现，可提供更具体的覆盖
  - 适合写：项目背景、启动与测试命令、目录边界、风险与审批要求、任务完成后的输出标准
  - 不适合写：只对一次任务有效的临时需求、含糊口号、无法执行或验证的要求
- **Hyperlinks**: “OpenAI AGENTS.md 文档” → https://learn.chatgpt.com/docs/agent-configuration/agents-md; “参考教程第八节” → https://jishuzhan.net/article/2053301309797892098

#### Slide 07 - AGENTS.md 示例：把科研约定写成可执行规则

- **Audience move**: 从理解概念 → 能为自己的科研仓库写出一个最小可用的 AGENTS.md
- **Relationships**: 项目背景决定工作规则；工作规则约束修改范围；验证与完成标准定义任务出口
- **Composition**: 左侧为编辑器中的完整最小示例，右侧用“具体、可执行、可验证”三个检查点解释为什么这样写。
- **Page rhythm**: dense
- **Title**: AGENTS.md 示例：把科研约定写成可执行规则
- **Core message**: 好的 AGENTS.md 把隐含经验变成命令、边界和完成条件，让每次任务从同一套规则开始。
- **Content**:
  - 示例背景：MATLAB R2024a 科研项目，主入口 `main.m`，测试入口 `tests/run_all.m`
  - 工作规则：先检查 `git status`；只修改当前任务文件；不改 `data/raw/`；新增依赖前先说明理由
  - 验证规则：运行测试并记录命令；图表变化需说明配置与数据来源
  - 完成标准：列出修改文件、测试结果、风险、回滚方式和关联提交
- **Hyperlinks**: “参考教程第八节” → https://jishuzhan.net/article/2053301309797892098

#### Slide 08 - Skill：把重复任务封装成可复用工作手册

- **Audience move**: 从把 Skill 当作一段更长的提示词 → 理解它是带触发条件、流程和资源的可复用能力目录
- **Relationships**: 名称与描述负责匹配任务；`SKILL.md` 提供完整流程；scripts、references 和 assets 按需支撑执行
- **Composition**: 左侧展示 Skill 目录与渐进加载，右侧展示显式调用和任务匹配两种触发方式；底部与 AGENTS.md 做一句区分。
- **Page rhythm**: breathing
- **Title**: Skill：把重复任务封装成可复用工作手册
- **Core message**: AGENTS.md 提供持续规则，Skill 只在特定任务出现时加载一套可复用流程和专业资料。
- **Content**:
  - 一个 Skill 是目录，必须包含带 `name` 与 `description` 的 `SKILL.md`
  - 可选目录：`scripts/` 可执行脚本、`references/` 参考资料、`assets/` 模板与资源
  - 渐进加载：先暴露名称与描述；选择使用后再读取完整 `SKILL.md`
  - 显式触发：在 Codex IDE 或 CLI 中用 `$skill-name`；隐式触发：任务与 `description` 匹配
  - 项目级 Skill 可放在 `.agents/skills/<skill-name>/`
- **Hyperlinks**: “OpenAI Skills 文档” → https://learn.chatgpt.com/docs/build-skills; “参考教程第九节” → https://jishuzhan.net/article/2053301309797892098

#### Slide 09 - Skill 示例：实验结果复核

- **Audience move**: 从理解 Skill 的结构 → 能识别一个边界清楚、可重复执行的科研 Skill
- **Relationships**: 触发描述选择 Skill；工作步骤从配置与提交映射开始，经过复跑和指标对比，最终形成复核记录
- **Composition**: 左侧以目录和 `SKILL.md` 代码示例为主，右侧以五步轨道展示执行流程，页底给出一次显式调用示例。
- **Page rhythm**: dense
- **Title**: Skill 示例：实验结果复核
- **Core message**: 把“每次都要重复解释的复核方法”封装成 Skill，才能让执行步骤、证据和输出格式保持一致。
- **Content**:
  - 路径：`.agents/skills/experiment-audit/SKILL.md`
  - `description` 明确触发边界：实验复跑、指标对比、结果来源核对、提交号记录
  - 工作流：读取配置 → 记录 Git 提交 → 运行最小复现实验 → 对比关键指标 → 写入结果摘要与风险
  - 禁止事项：不改原始数据，不覆盖历史结果，不在缺少配置或提交号时声称已复现
  - 调用示例：`请使用 $experiment-audit 复核本次定位实验，并输出配置、提交号、指标差异和风险。`
- **Hyperlinks**: “OpenAI Skills 文档” → https://learn.chatgpt.com/docs/build-skills; “参考教程第九节” → https://jishuzhan.net/article/2053301309797892098

#### Slide 10 - 在 VS Code 中使用 Codex：安装、给上下文、审查变更

- **Audience move**: 从知道有扩展 → 能按一条最短路径完成第一次可审查任务
- **Relationships**: 安装或启用、打开侧边栏、附加上下文、提出任务、审查与验证按顺序连接
- **Composition**: 三张真实截图按步骤排列，中间的聊天面板最大；每张图只配一条操作提示和一个检查点。
- **Page rhythm**: dense
- **Title**: 在 VS Code 中使用 Codex：安装、给上下文、审查变更
- **Core message**: 先打开项目，再把相关文件或选区带入提示，最后在编辑器中审查 diff 和验证结果。
- **Content**:
  - 1 安装或启用 Codex 扩展并登录 · 2 打开项目与 Codex 侧边栏
  - 3 引用打开文件、选区或相关上下文 · 4 提出具体任务并声明完成标准
  - 5 检查摘要与差异，运行测试；任务前后建立 Git 检查点
- **Images**: vscode-codex-extension-marketplace.png → vscode-codex-chat-panel.png → vscode-codex-file-reference.png，按安装到使用顺序呈现，均不裁切。
- **Hyperlinks**: “OpenAI Codex IDE 扩展文档” → https://learn.chatgpt.com/docs/codex/ide; “参考教程” → https://codexguide.ai/start/13-ide-vscode.html

### Part 2: Git 原理与基本使用

#### Slide 11 - Git 不是“网盘”：它是每个人都拥有完整历史的版本系统

- **Audience move**: 从把 Git 等同于 GitHub 或文件备份 → 理解分布式版本控制与远程平台的区别
- **Relationships**: 集中式仓库依赖中心节点；分布式 Git 让多个本地仓库各自拥有历史并可同步；GitHub 是一种远程协作平台
- **Composition**: 左侧一句定义与 Git/GitHub 区分，右侧用现有对比图承担直观证据。
- **Page rhythm**: breathing
- **Title**: Git 不是“网盘”：它是每个人都拥有完整历史的版本系统
- **Core message**: Git 管理版本与历史，GitHub 等平台托管远程仓库并支持协作；没有网络也能在本地提交和查看历史。
- **Content**:
  - Git：分布式版本控制工具 · GitHub/GitLab：远程托管与协作平台
  - 提交保存的是项目状态快照及其父子关系，而不是随手复制一份文件夹
- **Images**: 0D32F290-80B0-4EA4-9836-CA58E22569B3.jpg 完整呈现，用于集中式与分布式关系对比。
- **Hyperlinks**: “Git 教程参考” → https://www.runoob.com/git/git-tutorial.html

#### Slide 12 - 一次 Git 提交，要经过四个位置

- **Audience move**: 从死记命令 → 用工作区、暂存区、本地仓库和远程仓库理解命令的作用
- **Relationships**: 文件修改从工作区经暂存区进入本地提交，再与远程仓库双向同步；status 和 diff 用于观察中间状态
- **Composition**: 四段状态轨道占据页面主体，命令贴在状态转移处；下方用一句话解释暂存区的价值。
- **Page rhythm**: dense
- **Title**: 一次 Git 提交，要经过四个位置
- **Core message**: `add` 决定本次提交包含什么，`commit` 固化本地历史，`push/pull` 才涉及远程同步。
- **Content**:
  - 工作区 Working Tree → `git add` → 暂存区 Staging Area
  - 暂存区 → `git commit` → 本地仓库 Local Repository
  - 本地仓库 ↔ `git push` / `git pull` ↔ 远程仓库 Remote Repository
  - `git status` 看状态 · `git diff` 看内容差异 · `git log` 看历史

#### Slide 13 - 日常只需掌握一条安全 Git 循环

- **Audience move**: 从面对大量命令无从下手 → 能完成一次小而清楚的提交并同步远程
- **Relationships**: 更新、修改、检查、暂存、提交、推送按顺序连接；发现问题可回到修改或暂存环节
- **Composition**: 左侧为六步命令轨道，右侧为终端窗口示例；风险命令单独放在页脚警示条。
- **Page rhythm**: dense
- **Title**: 日常只需掌握一条安全 Git 循环
- **Core message**: 先看状态和差异，再只暂存当前任务文件，验证通过后提交，最后推送。
- **Content**:
  - `git pull` 更新 · 修改与测试 · `git status` / `git diff` 检查
  - `git add <files>` 精确暂存 · `git commit -m "说明原因"` · `git push`
  - 提交信息回答“为什么改”，不要只写 update 或 fix
  - 未理解影响前，不使用会覆盖历史或丢失修改的强制命令

#### Slide 14 - 科研使用 Git：版本应回答“这次实验为什么不同”

- **Audience move**: 从只备份代码 → 能用分支、配置和提交把实验条件与结果来源关联起来
- **Relationships**: 研究问题派生实验分支；代码与配置生成结果；验证后合并；提交、环境和结果说明共同支持复现
- **Composition**: 一条主分支贯穿页面，三个实验分支显示不同配置与验证结果；右侧列出应追踪与应忽略内容。
- **Page rhythm**: dense
- **Title**: 科研使用 Git：版本应回答“这次实验为什么不同”
- **Core message**: Git 追踪代码、配置和方法变化；大型原始数据、密钥、缓存和可再生成结果应由专门机制管理。
- **Content**:
  - 一个研究假设或修复对应一个短分支；完成后以可解释提交合并
  - 追踪：源代码、配置、环境依赖、数据获取说明、评估脚本、图表生成方法
  - 忽略：密钥、缓存、临时文件、大型原始数据、可由脚本重建的输出
  - 结果目录保留 README、指标摘要或索引，使提交能指向实验记录

### Part 3: Codex + Git 的科研协同

#### Slide 15 - Codex 负责执行，Git 负责建立可信检查点

- **Audience move**: 从分别使用两个工具 → 能按角色分工完成一次可审查的科研任务
- **Relationships**: 人定义目标与验收标准；Codex 读取、修改并验证；Git 保存前后检查点和差异；人审查后决定保留、修正或回退
- **Composition**: 一个闭环从研究问题开始，经过 Codex 工作区和 Git 检查点回到可复现实验；人类判断位于入口和出口。
- **Page rhythm**: anchor
- **Title**: Codex 负责执行，Git 负责建立可信检查点
- **Core message**: 让 AI 产生变化之前先有基线，变化之后必须有 diff、验证证据和可恢复提交。
- **Content**:
  - 1 定义任务、相关文件与完成标准 · 2 建立干净 Git 基线
  - 3 让 Codex 分析、修改并运行检查 · 4 人审查 diff、结果与风险
  - 5 只提交当前任务文件并推送 · 6 用提交号记录论文图表或实验结果来源
- **Motion suggestion**: 从 Slide 14 的分支主线延续为闭环中的 Git 检查点，作为 Morph candidate；自定义动画保持关闭。

#### Slide 16 - 三条规则，把 AI 辅助编程变成可复现科研

- **Audience move**: 从理解方法 → 记住并能立即执行三条最低实践
- **Relationships**: 小任务与清楚边界减少误改；验证与审查建立证据；提交与推送形成可恢复历史；三者共同产生可复现结果
- **Composition**: 三条规则以大号序号纵向推进，右侧保留一个最终检查清单和“从代码到知识”的收束句。
- **Page rhythm**: anchor
- **Title**: 三条规则，把 AI 辅助编程变成可复现科研
- **Core message**: 每次任务结束，都留下可运行的变化、验证证据和 Git 检查点。
- **Content**:
  - 01 任务要小：说明目标、范围、相关文件与完成标准
  - 02 结果要验：看 diff、跑测试、核对数据与图表，不把“生成了”当作“正确了”
  - 03 历史要清：只提交当前任务文件，用信息说明原因，推送并记录提交号
  - 立即实践：选择一个现有科研脚本，让 Codex 做一个可验证的小改动，再用 Git 完成检查点
- **Closing impact**: 绑定收束“可复现不是最后补文档，而是每次任务结束时留下三样东西”；构图以三条规则汇入同一研究结果为终点。

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 以确认后的 12 页内容为依据，补充解释、转场、风险提示和来源说明；不引入源材料与官方文档之外的新事实或数据。
- **Total duration**: 20–25 minutes
- **Notes style**: conversational, patient, explanatory, with concise transitions
- **Presentation purpose**: 先建立 Codex 的正确认知并讲清其在 VS Code 中的基本使用，再补充 Git 的原理与日常操作，最后把两者组合成可追踪、可复现的科研工作流
