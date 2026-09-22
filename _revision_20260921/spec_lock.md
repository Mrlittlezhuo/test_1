<!-- ppt-master-schema: spec-lock/v1 -->
# Execution Lock

## canvas
- viewBox: 0 0 1280 720
- format: PPT 16:9

## communication
- primary_language: zh-CN
- audience: 课题组导师与研究生；多数人熟悉 ChatGPT 和 VS Code，但对 Codex、Git 以及两者在科研中的协同方式了解程度不同
- objective: 依次讲清 Codex、Git 和二者的科研协同，使听众能够把可审查、可恢复、可复现的工作流迁移到自己的项目
- core_message: Codex 负责在项目上下文中理解并执行任务，Git 负责记录、比较和恢复每一次变化；两者结合，才能把 AI 辅助编程变成可信、可复现的科研实践
- consumption_mode: balanced

## mode
- mode: custom
- mode_references: instructional, narrative
- mode_behavior: 以逐步教学为主线，并用“从会聊天到会执行，再到可复现”的转折推进：先回答 Codex 是什么，接着示范项目结构和 VS Code 操作，再引入 Git，最后在科研闭环中完成收束。每页只承担一个清晰学习动作，章节入口通过工作状态变化衔接。

## visual_style
- visual_style: custom
- visual_style_references: editorial, soft-rounded
- visual_style_behavior: 以右侧编辑器或终端界面为持续视觉锚点，左侧使用编辑式大标题、细规则与少量圆角说明块；页面保持浅色大留白，步骤、路径和关键命令用蓝色标注。融合出版式层级与友好圆角容器，但弱化卡片堆叠，让同一张“研究工作台”贯穿全篇。

## colors
- background: #F6F8FB
- secondary_bg: #FFFFFF
- primary: #14213D
- accent: #377DFF
- secondary_accent: #20B8CD
- body_text: #1D2939
- secondary_text: #667085
- divider: #D9E1EC
- surface: #FFFFFF
- grid: #E9EEF5

## typography
- font_family: Microsoft YaHei, Arial, sans-serif
- title_family: Microsoft YaHei, Arial, sans-serif
- body_family: Microsoft YaHei, Arial, sans-serif
- code_family: Consolas, monospace
- cover_title: 64
- chapter_title: 52
- title: 44
- subtitle: 32
- lead: 30
- body: 24
- code: 20
- annotation: 18
- footnote: 14

## icons
- library: tabler-outline
- stroke_width: 2
- inventory: tabler-outline/message-circle, tabler-outline/code, tabler-outline/folder, tabler-outline/settings, tabler-outline/terminal-2, tabler-outline/git-branch, tabler-outline/stack-2, tabler-outline/check, tabler-outline/arrow-right, tabler-outline/flask, tabler-outline/history, tabler-outline/refresh, simple-icons/git, simple-icons/visualstudiocode, simple-icons/openai

## images
- cover_workbench: images/exec-c60951e0-9251-4198-bc55-5086aaea3ef7.png | source=user | crop=no-crop
- vscode_install: images/vscode-codex-extension-marketplace.png | source=user | crop=no-crop
- vscode_chat: images/vscode-codex-chat-panel.png | source=user | crop=no-crop
- vscode_file_ref: images/vscode-codex-file-reference.png | source=user | crop=no-crop
- git_distributed: images/0D32F290-80B0-4EA4-9836-CA58E22569B3.jpg | source=user | crop=no-crop

## page_visualizations
- P02: table/comparison_matrix

## page_rhythm
- P01: anchor
- P02: dense
- P03: breathing
- P04: dense
- P05: dense
- P06: breathing
- P07: dense
- P08: breathing
- P09: dense
- P10: dense
- P11: breathing
- P12: dense
- P13: dense
- P14: dense
- P15: anchor
- P16: anchor

## pptx_structure
- mode: flat

## forbidden
- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
- HTML named entities in text; write typography as raw Unicode and escape XML reserved characters
