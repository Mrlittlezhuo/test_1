"""Mechanical cleanup of the existing 16-page SVG deck.

This preserves diagrams, code, screenshots and information groups while
removing repeated UI-like chrome and applying a restrained seminar palette.
"""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent
SLIDES = ROOT / "svg_output"

TITLES = {
    "ChatGPT 更像思考伙伴，Codex 更像项目执行者": "ChatGPT 与 Codex：分别适合什么工作",
    "Codex 的价值在“闭环执行”，不只在生成代码": "Codex 处理代码任务的基本流程",
    "Codex 项目没有神秘格式：": "科研代码项目的常见目录",
    "关键是上下文清楚、边界明确": "规则、代码、测试与结果",
    "AGENTS.md 规定“怎么做”，Skills 封装“重复怎么做”": "项目规则与可复用技能",
    "AGENTS.md：写给 Codex 的项目说明书": "AGENTS.md：项目级工作约定",
    "AGENTS.md 示例：把科研约定写成可执行规则": "科研项目中的 AGENTS.md 示例",
    "Skill：把重复任务封装成可复用工作手册": "Skill 的结构与调用方式",
    "Skill 示例：把“实验结果复核”变成固定流程": "Skill 示例：实验结果复核",
    "在 VS Code 中使用 Codex：安装、给上下文、审查变更": "在 VS Code 中使用 Codex",
    "Git 不是“网盘”：它是每个人都拥有完整历史的版本系统": "Git 的分布式版本管理",
    "一次 Git 提交，要经过四个位置": "Git 的四个工作位置",
    "日常只需掌握一条安全 Git 循环": "Git 的日常操作顺序",
    "科研使用 Git：版本应回答“这次实验为什么不同”": "用 Git 管理科研实验版本",
    "Codex 负责执行，Git 负责建立可信检查点": "Codex 与 Git 的协作流程",
    "三条规则，把 AI 辅助编程变成可复现科研": "科研项目中的三项基本检查",
}

COLORS = {
    "#F6F8FB": "#FFFFFF",
    "#14213D": "#263238",
    "#377DFF": "#456779",
    "#20B8CD": "#648681",
    "#245FD1": "#355F70",
    "#168FA0": "#527A75",
    "#7EE0CF": "#A9C9BB",
    "#EAF2FF": "#F2F5F5",
    "#EFF5FF": "#F2F5F5",
    "#EAF8FA": "#F1F5F3",
    "#BFD2FA": "#D7DFE0",
    "#BFE8ED": "#D7DFE0",
    "#D9E1EC": "#D8DEE0",
    "#98A2B3": "#819096",
    "#667085": "#607078",
    "#1D2939": "#263238",
    "#1E2E4A": "#34434C",
    "#1E2E4D": "#34434C",
    "#334768": "#53626B",
    "#8FA3C3": "#AEBBC1",
    "#B8C7E0": "#C3CDD2",
    "#7EB1FF": "#AFC6C5",
    "#7EB0FF": "#AFC6C5",
    "#FFD166": "#D2C49B",
}


def cleanup_svg(source: str, number: int) -> str:
    result = source
    for before, after in TITLES.items():
        result = result.replace(before, after)
    for before, after in COLORS.items():
        result = result.replace(before, after)

    # This three-part progress strip was repeated on every page without
    # conveying new information. Page numbering remains in the footer.
    result = re.sub(
        r'\s*<g transform="translate\(1016 48\)"[^>]*>.*?</g>',
        "",
        result,
        flags=re.DOTALL,
    )
    result = re.sub(r'<rect([^>]*)\brx="\d+(?:\.\d+)?"', r'<rect\1rx="4"', result)
    result = result.replace('font-size="44"', 'font-size="38"')
    result = result.replace('font-size="42"', 'font-size="38"')

    # Remove literal mock-app window controls; code samples remain intact.
    result = re.sub(
        r'<circle[^>]*fill="#FF6B6B"[^>]*/>\s*'
        r'<circle[^>]*fill="(?:#F5C451|#D2C49B|#FFD166)"[^>]*/>\s*'
        r'<circle[^>]*fill="(?:#43C59E|#20B8CD|#648681)"[^>]*/>',
        "",
        result,
    )
    # Red/green/yellow window controls appear in several source variants.
    result = re.sub(
        r'<circle[^>]*fill="#FF6B6B"[^>]*/>\s*'
        r'<circle[^>]*fill="#D2C49B"[^>]*/>\s*'
        r'<circle[^>]*fill="#648681"[^>]*/>',
        "",
        result,
    )

    # Remove decorative English headings, which read like a generic template.
    result = re.sub(r'\s*<text[^>]*>ONE TASK · ONE VERIFIABLE LOOP</text>', "", result)
    result = re.sub(r'\s*<text[^>]*>ONE QUESTION · SMALL BRANCHES · EXPLAINABLE MERGE</text>', "", result)
    result = re.sub(r'\s*<text[^>]*>TASK DONE\?</text>', "", result)

    # Turn bottom "takeaway cards" into ordinary editorial footnotes.
    for group_id in ("footer", "bottom-note", "practice-and-links", "risk-warning", "closing"):
        pattern = rf'(<g id="{group_id}"[^>]*>)(.*?)(</g>)'
        match = re.search(pattern, result, flags=re.DOTALL)
        if match:
            body = re.sub(r'<rect\b[^>]*/>', "", match.group(2))
            result = result[:match.start()] + match.group(1) + body + match.group(3) + result[match.end():]

    # Keep a single subtle separator under each title instead of UI navigation.
    if number >= 2:
        result = re.sub(
            r'(<g id="header"[^>]*data-pptx-bounds="64 [^"]*"[^>]*>)(.*?)(</g>)',
            lambda m: m.group(1).replace(
                re.search(r'data-pptx-bounds="[^"]+"', m.group(1)).group(),
                'data-pptx-bounds="64 32 1152 130"',
            ) + m.group(2) + '<line x1="64" y1="154" x2="1216" y2="154" stroke="#D8DEE0" stroke-width="1"/>' + m.group(3),
            result,
            count=1,
            flags=re.DOTALL,
        )
    return result


for page in range(2, 17):
    file = SLIDES / f"slide-{page:02}.svg"
    file.write_text(cleanup_svg(file.read_text(encoding="utf-8"), page), encoding="utf-8")

print("Cleaned 15 SVG slides. Cover is authored separately.")
