# Codex 聊天分叉与 Git 分支：它们各自如何运行

> 这里把 Codex 中从一段对话另开一条路线称为“聊天分叉”；把 Git 中从同一提交开始尝试不同代码方案称为“Git 分支”。两个“分支”看起来相似，管理的东西却不同。

## 先说结论

**聊天分叉管理讨论，Git 分支管理代码版本。**新聊天继承分叉点之前的对话，之后两边的消息分别继续；新聊天里的提问和回答不会自动写回原聊天。但是，如果两条聊天操作的是同一个项目目录，一边修改的文件仍可能被另一边看到。要同时隔离对话和工作文件，需要给不同路线安排不同的工作目录，例如 Git worktree。

## 1. Codex 的聊天分叉怎样运行

假设原聊天已经讨论到“反射面数量未知，准备比较两种估计方法”。这时从该位置分叉：

```text
共同的讨论记录：问题、已知条件、已有判断
            ├─ 原聊天 A：继续研究完整搜索
            └─ 新聊天 B：研究粗糙度引导的受限搜索
```

新聊天 B 带着分叉点之前的讨论继续，因此不用从头解释课题背景。如果从较早的一轮分叉，原聊天在那一轮之后的新内容也不会被带进 B。分叉后，A 中的新消息只进入 A，B 中的新消息只进入 B。**回到原聊天 A 时，B 后来讨论的内容不会自动成为 A 的对话上下文；反过来也一样。**如果希望 A 知道 B 得出的结论，需要主动把结论写入 A，或整理进双方都能读取的项目文档。这是根据官方“复制指定轮次以前的历史并创建新聊天 ID”的机制得出的结论。[OpenAI Docs：Codex App Server](https://learn.chatgpt.com/docs/app-server)

Codex 桌面端的 `/fork` 可把本地聊天复制成新的本地聊天，或放到新的 worktree 中；可用选项会随环境和权限变化。这里的“复制”针对聊天历史，**不能据此认定已经创建了 Git 分支**。[OpenAI Docs：斜杠命令](https://learn.chatgpt.com/docs/reference/slash-commands)

### 回到原聊天，会受到新聊天干扰吗？

要分两层回答：

| 层次 | 回到原聊天时会怎样 |
|---|---|
| 对话记录 | 新聊天后续的问答不会自动出现在原聊天中，讨论路线彼此独立。 |
| 项目文件 | 如果两条聊天使用同一个工作目录，新聊天改过的代码、配置或实验记录可能已经改变了这个目录；原聊天再次读取文件时就可能看到这些变化。 |

例如，原聊天 A 以为自己还在稳定基线，新聊天 B 却在同一个目录里切换了 Git 分支并修改了 `estimate.m`。此时回到 A，A 的聊天记录虽然没有 B 的新消息，但它读取到的文件可能已经是 B 的版本。**这属于工作目录的变化，不是聊天上下文自动串线。**要避免这种情况，应在开始实验前确认当前目录和 Git 状态，或者让 B 在独立 worktree 中工作。[OpenAI Docs：Git worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees)

## 2. Git 分支怎样运行

Git 的一次提交保存当时的项目快照，并指向之前的提交。分支可以理解为一个指向某次提交的、会随着新提交前进的名字。创建实验分支时，两条路线可以从同一个基线提交出发：[Git 官方教程：Branches in a Nutshell](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)

```text
共同基线提交 C0
       ├─ main：继续维护当前可用方法，提交 C1
       └─ exp/roughness：尝试受限搜索，提交 E1、E2
```

实验分支上的提交不会自动进入 `main`。切回 `main`，看到的是 `main` 对应的已提交版本；验证有效后，才考虑把实验分支的修改合入主线。[Git 官方教程：Branches in a Nutshell](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)、[Git 官方文档：git-merge](https://git-scm.com/docs/git-merge)

但要特别注意：**Git 分支隔离的是提交历史，不会把未提交的修改自动封存在原分支。**同一工作目录切换分支时，未提交的修改可能继续留在目录中，也可能使切换被 Git 拒绝。所以切换路线前，先检查并妥善处理当前修改；不要把“已经建分支”理解成“两份代码可以同时在一个目录中运行”。[Git 官方文档：git-switch](https://git-scm.com/docs/git-switch)

如果需要同时运行 A、B 两条路线，可以使用 Git worktree：同一个仓库关联多个工作目录，每个目录有自己的文件状态，可以分别检出不同路线。Codex 的 worktree 模式也用于让不同聊天并行处理同一项目；不过 Codex 创建的 worktree 可能起始于 detached HEAD，是否建立正式 Git 分支仍需确认。worktree 只隔离各自目录中的文件；如果实验都写向同一个目录外的结果路径，输出仍可能互相覆盖。[Git 官方文档：git-worktree](https://git-scm.com/docs/git-worktree)、[OpenAI Docs：Git worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees)

## 3. 两种分支如何配合

| 问题 | 聊天分叉 | Git 分支 |
|---|---|---|
| 从哪里开始 | 从某个对话节点继承此前的讨论 | 从某次提交继承此前的代码历史 |
| 分叉后分别积累什么 | 各自的新问题、推理和结论 | 各自的代码、配置、文档提交 |
| 是否自动合并到原路线 | 不会 | 不会 |
| 能否单独隔离工作文件 | 不能保证 | 已提交版本可分开；并行工作宜配合独立 worktree |

科研中可以把它们一一对应：

```text
研究问题与已验证的基线
    ├─ 聊天 A：沿用原算法的理由与讨论
    │    └─ Git 路线 A：原算法代码、配置、实验记录
    └─ 聊天 B：改造算法的理由与讨论
         └─ Git 路线 B：改造代码、配置、实验记录
```

这只是一种**人为建立的对应关系**。聊天名称、工作目录、Git 分支和实验结果应明确记录，Codex 不会自动替研究者判断两条路线是否等价、哪条更好。

## 4. 一次科研尝试的稳妥做法

1. **固定起点。**先确认当前可信基线，把代码和必要配置提交，记下起始提交。
2. **分开讨论。**从共同问题分叉聊天，每条聊天集中研究一种方案。新聊天继承分叉前的背景，各自后续的讨论独立。
3. **核对代码位置。**开始改文件前，确认当前工作目录和 Git 状态。需要两条路线同时运行时，为新路线使用独立 worktree；在对应目录中确认或创建 Git 分支。
4. **分别实现和记录。**把论文复现、项目接入、算法改造等变化分开提交，记录运行配置与版本号。
5. **同条件比较。**固定数据、随机种子和评价指标，尤其检查最终科研目标，而不只看某个内部残差。
6. **依据结果继续。**有效方案经验证后再合入主线；不合适的方案保留关键提交、结果和失败原因，随后回到问题与假设继续研究。

在终端中，开始任务或返回某条路线时，至少可以用下面两个命令核对现场：

```bash
git status -sb        # 当前分支以及未提交修改
git worktree list     # 当前仓库关联了哪些工作目录
```

## 用于汇报的一句话

> 聊天分叉让我们从同一研究问题继续讨论不同思路，Git 分支保存每条路线实际运行的代码版本。分叉后的对话不会互相回写；若共用工作目录，文件仍可能互相影响。给并行路线安排清楚的 Git 分支与工作目录，再用同条件实验决定下一步。

## 参考资料

- [OpenAI Docs：Codex App Server，聊天分叉机制](https://learn.chatgpt.com/docs/app-server)
- [OpenAI Docs：斜杠命令](https://learn.chatgpt.com/docs/reference/slash-commands)
- [OpenAI Docs：Git worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees)
- [Git 官方教程：Branches in a Nutshell](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
- [Git 官方文档：git-switch](https://git-scm.com/docs/git-switch)
- [Git 官方文档：git-worktree](https://git-scm.com/docs/git-worktree)
