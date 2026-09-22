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
| Design Style | 学术交流版式：白底、深灰文字、细分隔线；只在代码和真实界面截图处使用深色区域 |
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
- **Visual Style Behavior**: 使用白底、深灰正文、低饱和蓝灰强调和细分隔线；以文本、目录树、原始截图、表格与必要流程图承载信息。封面与总结页尤其克制，不使用重复章节导航、装饰卡片或拟态软件控件。
- **Theme**: 一条由 Codex、Git 到科研复现的三段式工作轨道；窗口标题栏、文件路径和提交节点作为跨页识别元素。
- **Tone**: 清楚、克制、可信，像一份能直接照着操作的科研工作台说明。

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FFFFFF | 全局白色背景 |
| Secondary background | #FFFFFF | 截图承载区、正文面板与代码窗口 |
| Primary | #263238 | 标题与代码面板 |
| Accent | #456779 | 关键路径与必要的流程强调 |
| Secondary accent | #648681 | 辅助区分与状态 |
| Body text | #263238 | 正文与主要标签 |
| Secondary text | #607078 | 注释与来源 |
| Divider | #D8DEE0 | 分栏与表格线 |
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
| Cover title | 56 |
| Chapter title | 52 |
| Title | 38 |
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

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vscode-codex-extension-marketplace.png | 2440 × 946 | 2.58 | 展示 VS Code 中安装或启用 Codex 扩展 | Screenshot | 与另外两张截图组成从安装到使用的顺序证据 | no-crop | user | Existing | https://codexguide.ai/start/13-ide-vscode.html | n/a | local |
| vscode-codex-chat-panel.png | 1938 × 1578 | 1.23 | 展示 Codex 侧边栏和聊天入口 | Screenshot | 作为步骤中部的主截图，突出编辑器内上下文 | no-crop | user | Existing | https://codexguide.ai/start/13-ide-vscode.html | n/a | local |
| vscode-codex-file-reference.png | 1950 × 1538 | 1.27 | 展示使用文件引用提供精确上下文 | Screenshot | 作为步骤末端的局部证据，与上下文提示并列 | no-crop | user | Existing | https://codexguide.ai/start/13-ide-vscode.html | n/a | local |
| 0D32F290-80B0-4EA4-9836-CA58E22569B3.jpg | 707 × 398 | 1.78 | 对比集中式 SVN 与分布式 Git 的仓库关系 | Diagram | 图像承担分布式概念的直观证据，旁边只补一句解释 | no-crop | user | Existing | https://www.runoob.com/git/git-tutorial.html | n/a | local |

## IX. Content Outline

### Part 1: Codex 与 VS Code

#### Slide 01 - Codex、VS Code 与 Git 在科研项目中的使用

- **Audience move**: 从把三者看成零散工具 → 看到一条从想法到可复现结果的完整路径
- **Relationships**: Codex、VS Code、Git 按使用顺序连接，并共同指向可复现科研结果
- **Composition**: 白底纯文字封面，给出主题、场景和日期，不使用生成式工作台插画。
- **Page rhythm**: anchor
- **Title**: Codex、VS Code 与 Git 在科研项目中的使用
- **Core message**: 更好的工具链，目标不是更快地产生代码，而是更可靠地产生研究结果。
- **Content**:
  - Codex：理解任务并执行修改 · VS Code：观察与交互工作区 · Git：记录、比较与恢复
- **Cover impact**: 以学术交流封面直接交代主题；无装饰性图片。

#### Slide 02 - ChatGPT 与 Codex 的工作方式

- **Audience move**: 从抽象地比较工具 → 用同一个 MATLAB 任务理解普通对话与项目内开发的区别
- **Relationships**: 普通 ChatGPT 对话与 Codex 在同一扩展卡尔曼滤波任务中形成对照；一边给出解释与示例，另一边可在授权项目中完成并验证修改
- **Composition**: 沿用白底、深灰标题和细线，左右两栏分别放简短定义、任务示例和预期结果；底部保留人工审查提醒。
- **Page rhythm**: dense
- **Title**: ChatGPT 与 Codex 的工作方式
- **Core message**: 普通 ChatGPT 对话适合解释原理并给出参考代码；Codex 可以读取授权项目、修改真实文件并运行验证。
- **Content**:
  - 普通 ChatGPT 对话：解释扩展卡尔曼滤波原理，给出 MATLAB 示例代码；用户还需自己放进项目并验证
  - Codex：定位项目中的状态更新函数，加入扩展卡尔曼滤波，保持接口不变，补充测试并说明改动
  - Codex 的交付可包括真实文件改动、测试结果和 Git 差异；最终改动仍需人工检查

#### Slide 03 - Codex 处理代码任务的基本流程

- **Audience move**: 从把 Codex 当作代码补全 → 理解它围绕任务完成一轮可验证闭环
- **Relationships**: 目标、读取上下文、计划、修改、运行验证、总结差异按顺序连接；验证结果可返回修改环节
- **Composition**: 一条从左到右的执行轨道贯穿页面，右侧以小型编辑器状态显示“修改 + 测试通过”。
- **Page rhythm**: breathing
- **Title**: Codex 处理代码任务的基本流程
- **Core message**: 真正可用的输出不是一段代码，而是经过上下文理解、修改、验证和说明的结果。
- **Content**:
  - 明确目标 → 读取项目 → 拆解计划 → 修改文件 → 运行检查 → 审查 diff → 汇报结果
  - 人在关键节点确认范围、风险和完成标准

#### Slide 04 - 科研代码项目的常见目录

- **Audience move**: 从寻找“标准 Codex 项目模板” → 能为科研代码组织一个容易理解和验证的目录
- **Relationships**: 项目根目录是父级；规则、说明、代码、测试、数据、配置、结果和文档是职责不同的成员
- **Composition**: 左侧给出科研项目目录树，右侧解释“必需、常见、按需”三类文件职责。
- **Page rhythm**: dense
- **Title**: 科研代码项目的常见目录
- **Core message**: 好的目录结构让人和 Codex 都能快速回答：规则是什么、代码在哪、如何运行、怎样验证、结果放哪。
- **Content**:
  - `AGENTS.md` 项目规则 · `README.md` 入口说明 · `src/` 代码 · `tests/` 验证
  - `configs/` 参数 · `data/` 数据约定 · `results/` 输出 · `docs/` 方法记录
  - `.gitignore` 排除缓存、密钥、大型原始数据和可再生成文件 · 依赖文件锁定环境

#### Slide 05 - 项目规则与可复用技能

- **Audience move**: 从每次重新解释规则 → 知道如何把项目规范和重复流程持久化
- **Relationships**: AGENTS.md 为项目提供持续指令；Skills 为特定任务提供可复用流程；两者共同约束 Codex 的执行
- **Composition**: 两栏并列对照，左侧列 AGENTS.md 的长期约定，右侧列 Skill 的目录结构；用一条细线分隔。
- **Page rhythm**: dense
- **Title**: 项目规则与可复用技能
- **Core message**: 把稳定规则写进 AGENTS.md，把多步骤方法封装成 Skill，能减少口头约定和提示词漂移。
- **Content**:
  - AGENTS.md：测试命令、目录约定、提交规则、禁止事项、领域背景
  - Skill：`SKILL.md` 指令 + 可选 scripts / references / assets，按显式点名或任务匹配触发
  - 实践：规则保持短而稳定；技能解决边界清楚、会重复出现的工作流
- **Hyperlinks**: “OpenAI AGENTS.md 文档” → https://learn.chatgpt.com/docs/agent-configuration/agents-md; “OpenAI Skills 文档” → https://learn.chatgpt.com/docs/build-skills

#### Slide 06 - AGENTS.md：项目级工作约定

- **Audience move**: 从知道有一个规则文件 → 理解 Codex 如何发现、叠加并执行不同作用域的项目指令
- **Relationships**: 全局规则、仓库根目录规则和当前目录附近的规则按路径形成指令链；越靠近当前目录的规则越具体
- **Composition**: 左侧列出从全局到局部的文件位置，右侧区分应该写入与不应写入的内容。
- **Page rhythm**: breathing
- **Title**: AGENTS.md：项目级工作约定
- **Core message**: AGENTS.md 不是临时提示词，而是 Codex 开始工作前读取的、可随项目持续生效的执行约定。
- **Content**:
  - 全局层：`~/.codex/AGENTS.md` 保存个人长期习惯；项目层：仓库根目录 `AGENTS.md` 保存团队约定
  - Codex 从项目根目录向当前工作目录逐层读取；更靠近当前目录的规则在指令链中更晚出现，可提供更具体的覆盖
  - 适合写：项目背景、启动与测试命令、目录边界、风险与审批要求、任务完成后的输出标准
  - 不适合写：只对一次任务有效的临时需求、含糊口号、无法执行或验证的要求
- **Hyperlinks**: “OpenAI AGENTS.md 文档” → https://learn.chatgpt.com/docs/agent-configuration/agents-md; “参考教程第八节” → https://jishuzhan.net/article/2053301309797892098

#### Slide 07 - 科研项目中的 AGENTS.md 示例

- **Audience move**: 从理解概念 → 能为自己的科研仓库写出一个最小可用的 AGENTS.md
- **Relationships**: 项目背景决定工作规则；工作规则约束修改范围；验证与完成标准定义任务出口
- **Composition**: 左侧为编辑器中的完整最小示例，右侧用“具体、可执行、可验证”三个检查点解释为什么这样写。
- **Page rhythm**: dense
- **Title**: 科研项目中的 AGENTS.md 示例
- **Core message**: 好的 AGENTS.md 把隐含经验变成命令、边界和完成条件，让每次任务从同一套规则开始。
- **Content**:
  - 示例背景：MATLAB R2024a 科研项目，主入口 `main.m`，测试入口 `tests/run_all.m`
  - 工作规则：先检查 `git status`；只修改当前任务文件；不改 `data/raw/`；新增依赖前先说明理由
  - 验证规则：运行测试并记录命令；图表变化需说明配置与数据来源
  - 完成标准：列出修改文件、测试结果、风险、回滚方式和关联提交
- **Hyperlinks**: “参考教程第八节” → https://jishuzhan.net/article/2053301309797892098

#### Slide 08 - Skill 的结构与调用方式

- **Audience move**: 从把 Skill 当作一段更长的提示词 → 理解它是带触发条件、流程和资源的可复用能力目录
- **Relationships**: 名称与描述负责匹配任务；`SKILL.md` 提供完整流程；scripts、references 和 assets 按需支撑执行
- **Composition**: 左侧是技能目录树，右侧按行解释按需加载过程和两种调用方式。
- **Page rhythm**: breathing
- **Title**: Skill 的结构与调用方式
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

#### Slide 10 - 在 VS Code 中使用 Codex

- **Audience move**: 从知道有扩展 → 能按一条最短路径完成第一次可审查任务
- **Relationships**: 安装或启用、打开侧边栏、附加上下文、提出任务、审查与验证按顺序连接
- **Composition**: 三张真实截图按操作顺序并列，每张图配一条简短说明；不使用卡片、徽章或仿界面装饰。
- **Page rhythm**: dense
- **Title**: 在 VS Code 中使用 Codex
- **Core message**: 先打开项目，再把相关文件或选区带入提示，最后在编辑器中审查 diff 和验证结果。
- **Content**:
  - 1 安装或启用 Codex 扩展并登录 · 2 打开项目与 Codex 侧边栏
  - 3 引用打开文件、选区或相关上下文 · 4 提出具体任务并声明完成标准
  - 5 检查摘要与差异，运行测试；任务前后建立 Git 检查点
- **Images**: vscode-codex-extension-marketplace.png → vscode-codex-chat-panel.png → vscode-codex-file-reference.png，按安装到使用顺序呈现，均不裁切。
- **Hyperlinks**: “OpenAI Codex IDE 扩展文档” → https://learn.chatgpt.com/docs/codex/ide; “参考教程” → https://codexguide.ai/start/13-ide-vscode.html

### Part 2: Git 原理与基本使用

#### Slide 11 - Git 的分布式版本管理

- **Audience move**: 从把 Git 等同于 GitHub 或文件备份 → 理解分布式版本控制与远程平台的区别
- **Relationships**: 集中式仓库依赖中心节点；分布式 Git 让多个本地仓库各自拥有历史并可同步；GitHub 是一种远程协作平台
- **Composition**: 左侧一句定义与 Git/GitHub 区分，右侧用现有对比图承担直观证据。
- **Page rhythm**: breathing
- **Title**: Git 的分布式版本管理
- **Core message**: Git 管理版本与历史，GitHub 等平台托管远程仓库并支持协作；没有网络也能在本地提交和查看历史。
- **Content**:
  - Git：分布式版本控制工具 · GitHub/GitLab：远程托管与协作平台
  - 提交保存的是项目状态快照及其父子关系，而不是随手复制一份文件夹
- **Images**: 0D32F290-80B0-4EA4-9836-CA58E22569B3.jpg 完整呈现，用于集中式与分布式关系对比。
- **Hyperlinks**: “Git 教程参考” → https://www.runoob.com/git/git-tutorial.html

#### Slide 12 - Git 的四个工作位置

- **Audience move**: 从死记命令 → 用工作区、暂存区、本地仓库和远程仓库理解命令的作用
- **Relationships**: 文件修改从工作区经暂存区进入本地提交，再与远程仓库双向同步；status 和 diff 用于观察中间状态
- **Composition**: 四段状态轨道占据页面主体，命令贴在状态转移处；下方用一句话解释暂存区的价值。
- **Page rhythm**: dense
- **Title**: Git 的四个工作位置
- **Core message**: `add` 决定本次提交包含什么，`commit` 固化本地历史，`push/pull` 才涉及远程同步。
- **Content**:
  - 工作区 Working Tree → `git add` → 暂存区 Staging Area
  - 暂存区 → `git commit` → 本地仓库 Local Repository
  - 本地仓库 ↔ `git push` / `git pull` ↔ 远程仓库 Remote Repository
  - `git status` 看状态 · `git diff` 看内容差异 · `git log` 看历史

#### Slide 13 - Git 的日常操作顺序

- **Audience move**: 从面对大量命令无从下手 → 能完成一次小而清楚的提交并同步远程
- **Relationships**: 更新、修改、检查、暂存、提交、推送按顺序连接；发现问题可回到修改或暂存环节
- **Composition**: 左侧为六步命令轨道，右侧为终端窗口示例；风险命令单独放在页脚警示条。
- **Page rhythm**: dense
- **Title**: Git 的日常操作顺序
- **Core message**: 先看状态和差异，再只暂存当前任务文件，验证通过后提交，最后推送。
- **Content**:
  - `git pull` 更新 · 修改与测试 · `git status` / `git diff` 检查
  - `git add <files>` 精确暂存 · `git commit -m "说明原因"` · `git push`
  - 提交信息回答“为什么改”，不要只写 update 或 fix
  - 未理解影响前，不使用会覆盖历史或丢失修改的强制命令

#### Slide 14 - 用 Git 管理科研实验版本

- **Audience move**: 从只备份代码 → 能用分支、配置和提交把实验条件与结果来源关联起来
- **Relationships**: 研究问题派生实验分支；代码与配置生成结果；验证后合并；提交、环境和结果说明共同支持复现
- **Composition**: 一条主分支贯穿页面，三个实验分支显示不同配置与验证结果；右侧列出应追踪与应忽略内容。
- **Page rhythm**: dense
- **Title**: 用 Git 管理科研实验版本
- **Core message**: Git 追踪代码、配置和方法变化；大型原始数据、密钥、缓存和可再生成结果应由专门机制管理。
- **Content**:
  - 一个研究假设或修复对应一个短分支；完成后以可解释提交合并
  - 追踪：源代码、配置、环境依赖、数据获取说明、评估脚本、图表生成方法
  - 忽略：密钥、缓存、临时文件、大型原始数据、可由脚本重建的输出
  - 结果目录保留 README、指标摘要或索引，使提交能指向实验记录

### Part 3: Codex + Git 的科研协同

#### Slide 15 - Codex 在算法研究中能做什么

- **Audience move**: 从只把 Codex 用于改代码 → 理解它怎样协助论文核对、独立复现、项目接入和证据整理
- **Relationships**: 论文与假设、独立复现、接入与改造、整理证据按研究推进顺序排列；研究者依据假设和最终指标决定是否采用方法
- **Composition**: 白底四行文字说明，每行写一个科研动作和 Codex 可执行的具体工作；横线分隔，页底保留研究判断的边界。
- **Page rhythm**: anchor
- **Title**: Codex 在算法研究中能做什么
- **Core message**: Codex 可以协助把论文方法转为可检查的实现与实验，但是否采用仍由研究者判断。
- **Content**:
  - 论文与假设：梳理观测模型、变量和前提，核对项目能否提供所需输入
  - 独立复现：按论文条件搭建最小实验，解释与原文结果的差异
  - 接入与改造：定位现有模块接口，试做改造并与基线同条件比较
  - 整理证据：整理代码、配置、运行结果与失败原因，留下可复查记录
  - 研究者根据假设与最终指标决定是否采用方法

#### Slide 16 - Codex 与 Git：两条算法路线的对照

- **Audience move**: 从抽象地知道分支可用于科研 → 能把不同 Codex 讨论、Git 实现和实验记录对应到同一个研究问题
- **Relationships**: 同一研究问题与稳定基线分出完整全局动态规划和粗糙度引导受限搜索两条路线；Codex 协助各自的分析与实现，Git 保留基线并隔离新修改；同条件比较后由研究者决定是否合并
- **Composition**: 页顶标出共同起点，中部左右并列两条路线；下方列出同条件比较与研究者决策，页脚说明讨论、代码和结果各自留下的记录。
- **Page rhythm**: anchor
- **Title**: Codex 与 Git：两条算法路线的对照
- **Core message**: Codex 协助探索不同算法，Git 隔离并记录各路线的代码；只有在同条件实验后才能决定是否合并。
- **Content**:
  - Paper2 多反射面估计案例：完整全局动态规划作为可信基线，探索粗糙度引导受限搜索
  - 路线 A：Codex 复核基线算法与实验设置；Git 保存可复跑的代码和配置
  - 路线 B：Codex 检查瓶颈并协助实现受限搜索；Git 用独立分支隔离修改与实验
  - 固定数据、随机种子和指标，比较定位精度与计算量；由研究者决定合并或记录失败原因后回到基线
  - 聊天讨论保留思路，Git 分支隔离代码，实验记录连接结果；聊天分叉不会自动建立 Git 分支
- **Closing impact**: 以真实科研路线说明可比较、可回退的工作方式，不预设新路线更优。

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 以最终 16 页内容为依据，补充解释、转场、风险提示和来源说明；不引入源材料与官方文档之外的新事实或数据。
- **Total duration**: 20–25 minutes
- **Notes style**: conversational, patient, explanatory, with concise transitions
- **Presentation purpose**: 先建立 Codex 的正确认知并讲清其在 VS Code 中的基本使用，再补充 Git 的原理与日常操作，最后把两者组合成可追踪、可复现的科研工作流
