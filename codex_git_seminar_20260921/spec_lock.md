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
- mode_behavior: 以课题组方法交流为主线：先说明 Codex 的工作对象和项目约定，再介绍 VS Code 操作、Git 的基本机制，最后给出科研项目中的协作步骤。页面使用直接的主题标题和实例，不以口号式转折驱动叙事。

## visual_style
- visual_style: custom
- visual_style_references: editorial
- visual_style_behavior: 白底、深灰文字、低饱和蓝灰和细分隔线；让真实截图、代码片段、表格和必要的流程关系承担视觉信息。避免重复导航、彩色徽章、装饰卡片和口号式页脚。

## colors
- background: #FFFFFF
- secondary_bg: #FFFFFF
- primary: #263238
- accent: #456779
- secondary_accent: #648681
- body_text: #263238
- secondary_text: #607078
- divider: #D8DEE0
- surface: #FFFFFF
- grid: #E9EEF5

## typography
- font_family: Microsoft YaHei, Arial, sans-serif
- title_family: Microsoft YaHei, Arial, sans-serif
- body_family: Microsoft YaHei, Arial, sans-serif
- code_family: Consolas, monospace
- cover_title: 56
- chapter_title: 52
- title: 38
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
- vscode_install: images/vscode-codex-extension-marketplace.png | source=user | crop=no-crop
- vscode_chat: images/vscode-codex-chat-panel.png | source=user | crop=no-crop
- vscode_file_ref: images/vscode-codex-file-reference.png | source=user | crop=no-crop
- git_distributed: images/0D32F290-80B0-4EA4-9836-CA58E22569B3.jpg | source=user | crop=no-crop

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
