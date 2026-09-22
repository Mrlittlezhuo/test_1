# Git 原理与基础使用教程

这是一份面向初学者的 Git 教程。它不要求你有版本控制经验，也不要求你先注册 GitHub。读完并完成练习后，你应该能够：

- 理解 Git 为什么采用“快照”记录项目。
- 分清工作区、暂存区、本地仓库和远程仓库。
- 独立完成初始化、暂存、提交、查看历史和推送。
- 使用分支开展新任务，并处理常见的合并冲突。
- 根据修改所处的阶段，选择相对安全的撤销方法。

> 一句话理解 Git：Git 是一个给项目保存历史快照、比较变化并合并不同工作成果的工具。

## 目录

1. [Git 是什么](#1-git-是什么)
2. [Git 的基本原理](#2-git-的基本原理)
3. [安装与首次配置](#3-安装与首次配置)
4. [创建或取得 Git 仓库](#4-创建或取得-git-仓库)
5. [最重要的日常工作流](#5-最重要的日常工作流)
6. [分支与合并](#6-分支与合并)
7. [远程仓库与团队协作](#7-远程仓库与团队协作)
8. [撤销修改与恢复版本](#8-撤销修改与恢复版本)
9. [从零开始的完整练习](#9-从零开始的完整练习)
10. [常见问题与排查方法](#10-常见问题与排查方法)
11. [推荐的使用习惯](#11-推荐的使用习惯)
12. [常用命令速查表](#12-常用命令速查表)
13. [参考资料](#13-参考资料)

---

## 1 Git 是什么

### 1.1 为什么需要版本控制

假设你在修改论文、实验代码或项目文档，可能会保存出这样的文件：

```text
论文最终版.docx
论文最终版2.docx
论文最终版_真的最终版.docx
论文最终版_导师修改后.docx
```

这种方式短期内能用，但很快会出现问题：

- 不知道两个版本具体差在哪里。
- 不知道某项修改是什么时候、为什么加入的。
- 想撤销一部分修改，却只能整份文件回退。
- 多个人同时修改时，很难合并各自的成果。
- 文件名越来越混乱，仍然不能保证历史完整。

版本控制系统用一套结构化的历史记录解决这些问题。Git 可以记录每次有意义的修改，让你查看差异、恢复版本、创建并行分支，也能把不同人的工作合并起来。

Git 最常用于源代码，但它同样适合管理：

- Markdown、LaTeX 和纯文本论文稿；
- MATLAB、Python、C/C++ 等实验代码；
- 配置文件和自动化脚本；
- 项目说明、会议记录和技术文档。

对于经常变化的大型二进制文件，例如视频、原始数据集和频繁编辑的 Word 文件，普通 Git 的使用体验和存储效率可能不理想，需要结合 Git LFS 或专门的数据存储方案。

### 1.2 Git 与 GitHub 不是一回事

| 名称 | 是什么 | 主要作用 |
|---|---|---|
| Git | 安装在电脑上的版本控制工具 | 记录提交、比较差异、创建分支、合并历史 |
| GitHub、GitLab、Gitee | 托管 Git 仓库的网络平台 | 共享仓库、管理权限、代码评审、议题跟踪和自动化 |

你可以在没有 GitHub 的情况下使用 Git，也可以在断网时继续提交和查看历史。等网络恢复后，再把本地提交推送到远程仓库。

可以把两者类比为：

- Git 是相机和相册管理系统。
- GitHub 等平台是供团队使用的网络共享相册。

---

## 2 Git 的基本原理

### 2.1 Git 保存的是项目快照

Git 在每次提交时，记录项目在那个时刻的状态，也就是一份“快照”。每个提交还会保存作者、时间、提交说明以及父提交等信息。

连续的提交可以想象成：

```text
C1 ---- C2 ---- C3 ---- C4
初始版   修复问题  增加功能  更新文档
```

每个 `C` 都代表一次提交。后一个提交通常会指向前一个提交，所以 Git 能沿着父提交关系追溯项目历史。

“快照”并不表示 Git 每次都机械地复制全部文件。对于没有改变的内容，Git 可以复用已经保存的数据，因此仍能高效存储历史。

### 2.2 一次提交包含什么

一次提交主要包括：

- 项目快照：这次提交所记录的文件状态。
- 父提交：当前提交从哪个历史节点发展而来。
- 作者和提交者信息：谁创建和记录了这次修改。
- 时间：修改和提交发生的时间。
- 提交说明：这次修改做了什么。
- 哈希标识：根据内容计算出的提交标识，例如 `a1b2c3d`。

分支名、标签名和提交短哈希，都是为了让人更方便地定位历史中的某个位置。

### 2.3 四个重要位置

日常使用 Git 时，最需要分清下面四个位置：

```text
┌──────────┐   git add    ┌──────────┐  git commit  ┌──────────┐   git push   ┌──────────┐
│  工作区  │ ───────────> │  暂存区  │ ───────────> │ 本地仓库 │ ───────────> │ 远程仓库 │
│ 编辑文件 │              │ 下次提交 │              │ 完整历史 │              │ 共享历史 │
└──────────┘              └──────────┘              └──────────┘              └──────────┘
```

#### 工作区 Working Tree

工作区就是你平时能看到和编辑的项目文件夹。你在编辑器中修改的内容，首先只存在于工作区。

#### 暂存区 Staging Area 或 Index

暂存区保存“下一次提交准备包含什么”。执行 `git add` 后，文件当前的内容被放进暂存区。

暂存区的作用类似购物车：你可以修改很多文件，但只选择其中与同一任务有关的部分放进本次提交。

#### 本地仓库 Local Repository

执行 `git commit` 后，暂存区中的快照会进入本地仓库。仓库数据通常保存在项目的 `.git` 目录中。

提交是本地操作。即使没有网络，你仍然可以提交、查看历史、建立分支和合并分支。

#### 远程仓库 Remote Repository

远程仓库是位于 GitHub、GitLab、Gitee、团队服务器或其他路径上的另一个 Git 仓库。它主要用于协作、共享和异地保存。

### 2.4 文件的三个主要状态

| 状态 | 含义 | 常用的下一步操作 |
|---|---|---|
| 已修改 modified | 文件已改变，但当前版本还没有进入暂存区 | `git diff`、`git add` |
| 已暂存 staged | 文件当前版本已被选入下一次提交 | `git diff --staged`、`git commit` |
| 已提交 committed | 快照已经写入本地仓库 | `git log`、`git push` |

最重要的一点是：

> `git commit` 提交的是暂存区里的内容，不是工作区中的所有修改。

### 2.5 分支 HEAD 和远程跟踪分支

- **分支 branch**：一个指向某次提交、并会随新提交向前移动的名字，例如 `main`。
- **HEAD**：表示你当前检出的位置，通常指向当前分支。
- **远程跟踪分支**：本地保存的远程状态记录，例如 `origin/main`。执行 `git fetch` 后，它会更新。

分支本质上是轻量的指针，不是复制整份项目文件。因此，为每个任务创建分支通常很快。

---

## 3 安装与首次配置

### 3.1 安装 Git

建议从 [Git 官方下载页面](https://git-scm.com/downloads/) 获取安装方式。

- Windows：安装 Git for Windows，之后可以使用 Git Bash，也可以在 PowerShell 中使用 Git。
- macOS：可以根据官方说明安装，或使用系统包管理器。
- Linux：通常通过发行版的包管理器安装。

安装完成后运行：

```bash
git --version
```

如果能看到版本号，说明 Git 命令已经可用。

### 3.2 设置提交身份

首次使用时，需要设置用户名和邮箱：

```bash
git config --global user.name "你的名字"
git config --global user.email "you@example.com"
```

这些信息会写入提交记录，但它们不是 GitHub 等平台的登录密码。

如果团队通过邮箱识别贡献，应使用与平台账户关联的邮箱，或者使用平台提供的隐私邮箱。

可以设置新仓库的默认主分支名：

```bash
git config --global init.defaultBranch main
```

查看当前配置以及每项配置来自哪个文件：

```bash
git config --list --show-origin
```

只查看用户名和邮箱：

```bash
git config user.name
git config user.email
```

### 3.3 全局配置与项目配置

带 `--global` 的配置对当前用户的所有仓库生效。

如果某个项目需要使用不同身份，可以进入该项目目录，运行不带 `--global` 的命令：

```bash
git config user.name "项目使用的名字"
git config user.email "project@example.com"
```

项目级配置会覆盖全局配置。

### 3.4 不要盲目复制换行符配置

Windows、macOS 和 Linux 的文本换行方式可能不同。新手经常从网上直接复制 `core.autocrlf` 配置，但不同团队的规则可能不同。

更稳妥的做法是：

1. 优先遵守仓库已有的 `.gitattributes`。
2. 遵守团队约定。
3. 如果 Git 突然把整份文件显示为已修改，先检查换行符和编码，不要立即提交。

---

## 4 创建或取得 Git 仓库

### 4.1 把现有目录初始化为仓库

进入项目目录后运行：

```bash
git init
git status
```

`git init` 会创建隐藏的 `.git` 目录，其中保存仓库历史、暂存区、分支引用和项目级配置等信息。

普通使用中不要手工修改 `.git` 内部文件。

### 4.2 克隆已有仓库

如果项目已经存在于远程仓库中，使用：

```bash
git clone <仓库地址>
```

例如：

```bash
git clone https://example.com/team/project.git
```

指定本地目录名：

```bash
git clone https://example.com/team/project.git my-project
```

`git clone` 不只是下载当前文件。它通常还会：

1. 创建本地目录和本地仓库。
2. 下载远程仓库的历史。
3. 把来源仓库配置为 `origin`。
4. 检出一个可以直接工作的版本。

### 4.3 使用 gitignore 排除不应提交的文件

在仓库根目录创建 `.gitignore`，可以告诉 Git 忽略某些尚未被跟踪的文件。

示例：

```gitignore
# 本地环境变量和密钥
.env

# 日志
*.log

# 构建产物
build/
dist/

# Python 缓存
__pycache__/
*.pyc

# 操作系统临时文件
.DS_Store
Thumbs.db
```

`.gitignore` 应根据项目实际情况编写，并提交到仓库，让团队共享忽略规则。

> 注意：`.gitignore` 只影响尚未被 Git 跟踪的文件。已经提交过的文件不会因为后来加入忽略规则就自动从历史中消失。

如果只想停止跟踪某个文件，同时保留工作区中的文件，可以使用：

```bash
git rm --cached <文件>
```

然后提交这次变化。

---

## 5 最重要的日常工作流

一个可靠的日常循环是：

```text
status → diff → add → diff --staged → commit → log
```

### 5.1 第一步 查看状态

```bash
git status
```

它会告诉你：

- 当前位于哪个分支；
- 哪些文件已经修改；
- 哪些文件还未被跟踪；
- 哪些修改已经进入暂存区；
- 当前是否正在合并或解决冲突；
- Git 建议的下一步操作。

`git status` 不会修改任何内容。遇到不确定的情况时，先运行它通常不会错。

### 5.2 第二步 检查修改

查看工作区与暂存区之间的差异：

```bash
git diff
```

查看暂存区与最近一次提交之间的差异，也就是“下一次提交准备包含什么”：

```bash
git diff --staged
```

只查看某个文件：

```bash
git diff -- README.md
```

先检查差异，可以发现调试输出、无关格式化、误删内容和不应提交的本地配置。

### 5.3 第三步 选择要提交的内容

暂存单个文件：

```bash
git add README.md
```

暂存多个文件：

```bash
git add src/app.py tests/test_app.py
```

按修改片段选择：

```bash
git add -p
```

暂存当前目录下的全部变化：

```bash
git add .
```

`git add .` 很方便，但也容易把临时文件和无关修改一起加入。执行前应先看 `git status`，执行后再看 `git diff --staged`。

### 5.4 第四步 创建提交

```bash
git commit -m "docs: 补充安装步骤"
```

一次提交最好只表达一个完整、清楚的意图。例如：

| 不清楚的说明 | 更清楚的说明 |
|---|---|
| `update` | `docs: 补充分支冲突处理步骤` |
| `fix bug` | `fix: 避免空输入导致程序崩溃` |
| `final` | `analysis: 更新实验参数说明` |

提交说明应尽量回答“这次修改带来了什么”，而不是只写自己做过“修改”。

### 5.5 第五步 查看历史

查看完整日志：

```bash
git log
```

查看简洁的分支图：

```bash
git log --oneline --graph --decorate --all
```

查看某次提交的内容：

```bash
git show <提交标识>
```

查看某个文件的提交历史：

```bash
git log -- README.md
```

### 5.6 已跟踪与未跟踪

Git 会把工作区文件分成两类：

- 已跟踪：Git 已经认识的文件，可能处于未修改、已修改或已暂存状态。
- 未跟踪：还没有被纳入版本控制的文件。

新建文件后，`git status` 通常会把它显示在 `Untracked files` 中。运行 `git add` 后，它才会被纳入下一次提交。

---

## 6 分支与合并

### 6.1 为什么使用分支

如果直接在主分支上尝试新功能，未完成的修改可能影响稳定版本。分支让你可以从当前历史位置开出一条独立工作线。

```text
                         C4 ---- C5  feature/notes
                        /          \
C1 ---- C2 ---- C3 ---------------- M  main
```

分支不是复制整个项目目录，而是一个指向提交的轻量名称。

常见做法是：

- `main` 保留相对稳定的版本；
- 每个功能、修复或实验使用单独分支；
- 完成并验证后，再合并回 `main`。

### 6.2 查看和创建分支

查看本地分支：

```bash
git branch
```

创建并切换到新分支：

```bash
git switch -c feature/notes
```

切换到已有分支：

```bash
git switch main
```

回到上一个分支：

```bash
git switch -
```

老教程经常使用 `git checkout` 切换分支。较新的 Git 提供了职责更明确的命令：

- `git switch`：主要用于切换分支。
- `git restore`：主要用于恢复文件。

### 6.3 合并分支

假设 `feature/notes` 已经完成，需要合并到 `main`：

```bash
git switch main
git merge feature/notes
```

要点是：`git merge <分支>` 会把指定分支合并到当前分支。因此，合并前必须先确认自己位于正确的接收分支。

合并完成后，可以删除已经完成的本地分支：

```bash
git branch -d feature/notes
```

### 6.4 什么是合并冲突

如果两个分支修改了同一个文件的同一部分，Git 可能无法自动判断应该保留哪一份内容，于是暂停合并并报告冲突。

冲突文件中可能出现：

```text
<<<<<<< HEAD
当前分支中的内容
=======
正在合并进来的分支中的内容
>>>>>>> feature/notes
```

解决步骤：

1. 运行 `git status`，找出冲突文件。
2. 打开文件，比较冲突标记之间的两部分内容。
3. 编辑出最终要保留的内容。
4. 删除 `<<<<<<<`、`=======`、`>>>>>>>` 等标记。
5. 运行测试或检查文件结果。
6. 用 `git add` 标记冲突已解决。
7. 运行 `git commit` 完成合并。

```bash
git status
git add <已解决的文件>
git commit
```

如果不想继续本次合并，可以在完成合并提交前运行：

```bash
git merge --abort
```

冲突不是项目损坏，而是 Git 把无法替你做出的内容决定交还给你。

---

## 7 远程仓库与团队协作

### 7.1 查看远程仓库

```bash
git remote -v
```

输出中的 `fetch` 地址用于获取数据，`push` 地址用于推送数据。它们通常相同，也可以不同。

### 7.2 添加远程仓库

```bash
git remote add origin <仓库地址>
```

`origin` 只是一个常用简称，不是特殊关键字。一个本地仓库也可以配置多个远程仓库。

查看某个远程地址：

```bash
git remote get-url origin
```

### 7.3 fetch pull 和 push 的区别

| 命令 | 作用 | 特点 |
|---|---|---|
| `git fetch` | 下载远程的新提交和分支信息 | 不自动改变当前工作文件，适合先看再合并 |
| `git pull` | 获取远程变化并立即尝试整合到当前分支 | 方便，但具体整合方式受配置影响 |
| `git push` | 把本地提交发送到远程分支 | 需要远程权限和身份验证 |

给初学者推荐一种更容易观察的同步方式：

```bash
git fetch origin
git log --oneline --graph --decorate --all
git merge origin/main
```

这样可以先看到本地与远程历史的关系，再决定是否合并。

如果团队已经明确 `pull` 的策略，也可以使用：

```bash
git pull
```

### 7.4 第一次推送

```bash
git push -u origin main
```

`-u` 会设置当前本地分支的上游关系。以后通常可以简写为：

```bash
git push
git pull
```

如果主分支实际叫 `master` 或其他名字，应使用仓库的真实分支名，而不是机械地照抄 `main`。

### 7.5 一个简单可靠的团队流程

1. 开始任务前，切回 `main` 并获取最新状态。
2. 从最新 `main` 创建任务分支。
3. 在任务分支上小步提交。
4. 推送任务分支到远程仓库。
5. 在托管平台创建 Pull Request 或 Merge Request。
6. 通过评审和测试后合并。
7. 删除已经完成的任务分支。

示例：

```bash
git switch main
git pull
git switch -c feature/export-report

# 编辑、检查、提交
git status
git add <相关文件>
git commit -m "feat: add report export"

git push -u origin feature/export-report
```

Pull Request 或 Merge Request 是托管平台提供的协作功能，不是 Git 自身的命令。它的底层仍然依赖分支、提交、比较和合并。

---

## 8 撤销修改与恢复版本

Git 的撤销命令之所以容易混淆，是因为修改可能位于不同位置。执行撤销前，先运行：

```bash
git status
git diff
git diff --staged
```

然后判断修改位于工作区、暂存区，还是已经进入提交历史。

### 8.1 取消暂存但保留文件修改

```bash
git restore --staged <文件>
```

这会把文件移出暂存区，但不会删除工作区中的修改，风险较低。

### 8.2 丢弃未暂存的文件修改

```bash
git restore <文件>
```

这会用暂存区或当前版本覆盖工作区文件。未提交的修改通常无法从 Git 找回，所以执行前必须确认确实不再需要。

### 8.3 修改最近一次提交

如果最近一次提交漏了文件，且还没有共享给别人：

```bash
git add <遗漏的文件>
git commit --amend
```

如果只是修改提交说明：

```bash
git commit --amend -m "新的提交说明"
```

`--amend` 会创建一个替代提交，提交标识也会改变。已经推送并被他人使用的提交不要随意修改。

### 8.4 安全撤销已经共享的提交

```bash
git revert <提交标识>
```

`revert` 会创建一个新的反向提交，用新历史抵消旧提交的效果。它不需要改写公共历史，因此更适合协作场景。

### 8.5 临时收起未完成的修改

```bash
git stash push -m "临时保存说明"
```

查看临时记录：

```bash
git stash list
```

恢复最近一次临时修改：

```bash
git stash pop
```

恢复后仍应运行 `git status`，因为应用 stash 时也可能发生冲突。

### 8.6 谨慎使用 reset hard

下面的命令可能同时移动分支并丢弃工作区和暂存区中的内容：

```bash
git reset --hard <提交标识>
```

它不是通用的“撤销键”。如果你不清楚它将移动哪个分支、覆盖哪些文件，就不要执行。

撤销操作可以按下面的安全顺序理解：

| 目标 | 推荐方法 | 风险 |
|---|---|---|
| 取消暂存，保留修改 | `git restore --staged <file>` | 低 |
| 暂时收起修改 | `git stash` | 较低，但恢复后要检查 |
| 撤销公共提交 | `git revert <commit>` | 通常适合协作 |
| 修改尚未共享的最后提交 | `git commit --amend` | 会改写最后一次提交 |
| 丢弃未提交修改 | `git restore <file>` | 可能永久丢失内容 |
| 强制移动分支并覆盖文件 | `git reset --hard` | 高 |

---

## 9 从零开始的完整练习

下面的练习只需要 Git、一个空目录和文本编辑器。

### 9.1 建立本地仓库

创建并进入一个名为 `git-practice` 的目录，然后运行：

```bash
git init
git status
```

用编辑器创建 `README.md`：

```markdown
# Git Practice

这是我的 Git 入门练习仓库。
```

检查状态：

```bash
git status
```

你应该能看到 `README.md` 是未跟踪文件。

### 9.2 完成第一次提交

```bash
git add README.md
git diff --staged
git commit -m "docs: add project readme"
git log --oneline --decorate
```

完成后再运行：

```bash
git status
```

正常情况下，工作区应当是干净的。

### 9.3 完成第二次提交

在 `README.md` 中增加：

```markdown
## 使用方法

本仓库用于练习 Git 的基本命令。
```

然后依次运行：

```bash
git diff
git add README.md
git diff --staged
git commit -m "docs: add usage section"
git log --oneline --graph --decorate --all
```

### 9.4 创建并合并分支

创建任务分支：

```bash
git switch -c feature/notes
```

创建 `notes.md`，写入几条学习笔记，然后提交：

```bash
git add notes.md
git commit -m "docs: add Git learning notes"
```

切回主分支并合并：

```bash
git switch main
git merge feature/notes
git branch -d feature/notes
git log --oneline --graph --decorate --all
```

如果你的主分支名是 `master`，请把命令中的 `main` 替换成 `master`。

### 9.5 连接远程仓库

在 GitHub、GitLab、Gitee 或团队服务器上创建一个空仓库。为了让第一次推送更简单，不要让平台自动创建 README、许可证或 `.gitignore`。

复制平台提供的仓库地址，然后运行：

```bash
git remote add origin <你的远程仓库地址>
git remote -v
git push -u origin main
```

最后检查：

```bash
git status
git branch -vv
```

如果远程页面能看到两次以上的提交，并且本地工作区干净，说明练习成功。

---

## 10 常见问题与排查方法

### 10.1 fatal not a git repository

```text
fatal: not a git repository
```

原因通常是当前目录及其上级目录中没有 `.git`。

处理方法：

1. 确认终端当前路径。
2. 进入正确的项目目录。
3. 如果这是一个全新项目，再决定是否运行 `git init`。

不要因为看到这个报错，就在任意目录中盲目执行 `git init`。

### 10.2 nothing to commit

可能原因：

- 文件实际上没有变化；
- 编辑器还没有保存文件；
- 文件被 `.gitignore` 忽略；
- 修改已经提交。

可以运行：

```bash
git status
git status --ignored
```

### 10.3 push 被 non fast forward 拒绝

这通常表示远程分支包含本地尚未拥有的提交。

先获取并查看：

```bash
git fetch origin
git log --oneline --graph --decorate --all
```

然后按照团队规则选择 `merge` 或 `rebase`。不要为了“让推送成功”就直接强制推送，因为那可能覆盖他人的远程历史。

### 10.4 无法切换分支

Git 可能提示本地修改会被覆盖。这是保护机制。

根据实际情况选择：

- 修改已经完成：先提交。
- 修改尚未完成但需要保留：使用 `git stash`。
- 修改确定不要：检查差异后使用 `git restore`。

### 10.5 authentication failed

常见原因包括：

- 没有远程仓库权限；
- 凭据或访问令牌过期；
- SSH 密钥未正确配置；
- 托管平台不接受账户密码作为 Git HTTPS 凭据。

应查阅所用托管平台当前的身份验证文档，配置凭据管理器、访问令牌或 SSH。不要把令牌、密码或私钥写入项目文件。

### 10.6 整个文件突然都显示为修改

常见原因是：

- 换行符从 LF 变成 CRLF，或反过来；
- 文件编码发生变化；
- 编辑器自动格式化了整个文件；
- 生成工具重写了文件。

先停止暂存和提交，检查 `.gitattributes`、编辑器设置和团队规范。

### 10.7 不小心提交了密钥

仅仅删除文件或把它加入 `.gitignore`，并不能让密钥从已有历史中消失。

应立即：

1. 在对应服务中撤销或轮换密钥，让旧密钥失效。
2. 通知项目负责人和可能受影响的协作者。
3. 按团队流程清理 Git 历史。
4. 检查日志、自动化系统和其他副本中是否也存在泄露。

第一优先级永远是让泄露的密钥失效，而不是先研究如何让提交记录“看不见”。

---

## 11 推荐的使用习惯

1. 每次开始工作先运行 `git status`，确认目录和分支。
2. 提交前查看 `git diff`，暂存后查看 `git diff --staged`。
3. 一次提交只做一件事，使其可以独立理解和撤销。
4. 使用能描述结果和意图的提交说明。
5. 为新功能、修复和实验创建独立分支。
6. 合并或解决冲突后运行测试。
7. 不提交密码、令牌、私钥、个人数据和本机专用配置。
8. 不把大型生成文件直接放入普通 Git 历史，必要时评估 Git LFS 或外部存储。
9. 已共享的历史优先使用 `revert` 撤销，谨慎改写后强制推送。
10. 重要项目仍应保留可靠的远程副本和数据备份；Git 不是完整的备份方案。

### 一次高质量提交的检查清单

提交前确认：

- [ ] 当前分支正确。
- [ ] `git status` 中没有意外文件。
- [ ] `git diff` 已检查。
- [ ] 暂存内容只属于同一个任务。
- [ ] `git diff --staged` 已检查。
- [ ] 测试或必要的验证已经完成。
- [ ] 提交说明清楚描述修改结果。
- [ ] 没有密钥、令牌、隐私数据或大型临时文件。

---

## 12 常用命令速查表

### 仓库与配置

| 目标 | 命令 |
|---|---|
| 查看 Git 版本 | `git --version` |
| 初始化仓库 | `git init` |
| 克隆仓库 | `git clone <url>` |
| 查看配置来源 | `git config --list --show-origin` |

### 查看和提交

| 目标 | 命令 |
|---|---|
| 查看状态 | `git status` |
| 查看未暂存差异 | `git diff` |
| 查看已暂存差异 | `git diff --staged` |
| 暂存文件 | `git add <file>` |
| 按片段暂存 | `git add -p` |
| 提交 | `git commit -m "说明"` |
| 查看简洁历史图 | `git log --oneline --graph --decorate --all` |
| 查看某次提交 | `git show <commit>` |

### 分支与合并

| 目标 | 命令 |
|---|---|
| 查看本地分支 | `git branch` |
| 创建并切换分支 | `git switch -c <branch>` |
| 切换分支 | `git switch <branch>` |
| 合并分支到当前分支 | `git merge <branch>` |
| 删除已合并的本地分支 | `git branch -d <branch>` |
| 放弃正在进行的合并 | `git merge --abort` |

### 远程仓库

| 目标 | 命令 |
|---|---|
| 查看远程仓库 | `git remote -v` |
| 添加远程仓库 | `git remote add origin <url>` |
| 获取远程变化 | `git fetch origin` |
| 获取并整合上游变化 | `git pull` |
| 首次推送并设置上游 | `git push -u origin <branch>` |
| 推送当前上游分支 | `git push` |

### 撤销与临时保存

| 目标 | 命令 |
|---|---|
| 取消暂存并保留修改 | `git restore --staged <file>` |
| 丢弃未暂存修改 | `git restore <file>` |
| 修改尚未共享的最后提交 | `git commit --amend` |
| 安全撤销公共提交 | `git revert <commit>` |
| 临时保存修改 | `git stash push -m "说明"` |
| 恢复最近一次 stash | `git stash pop` |

常用占位符：

- `<file>`：文件或目录路径，例如 `README.md` 或 `src/`。
- `<branch>`：分支名，例如 `main` 或 `feature/export`。
- `<commit>`：提交标识，可使用 `git log` 中显示的短哈希。
- `<url>`：远程仓库地址，可以是 HTTPS 或 SSH 地址。

---

## 13 参考资料

本文以 Git 官方资料为主要依据，并参考了附件中提供的中文教程链接。资料访问日期为 2026 年 9 月 20 日。

### Git 官方资料

- [Pro Git：关于版本控制](https://git-scm.com/book/zh/v2/%E8%B5%B7%E6%AD%A5-%E5%85%B3%E4%BA%8E%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6)
- [Pro Git：What is Git](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F)
- [Pro Git：初次运行 Git 前的配置](https://git-scm.com/book/zh/v2/%E8%B5%B7%E6%AD%A5-%E5%88%9D%E6%AC%A1%E8%BF%90%E8%A1%8C-Git-%E5%89%8D%E7%9A%84%E9%85%8D%E7%BD%AE)
- [Pro Git：获取 Git 仓库](https://git-scm.com/book/zh/v2/Git-%E5%9F%BA%E7%A1%80-%E8%8E%B7%E5%8F%96-Git-%E4%BB%93%E5%BA%93)
- [Pro Git：记录每次更新到仓库](https://git-scm.com/book/zh/v2/Git-%E5%9F%BA%E7%A1%80-%E8%AE%B0%E5%BD%95%E6%AF%8F%E6%AC%A1%E6%9B%B4%E6%96%B0%E5%88%B0%E4%BB%93%E5%BA%93)
- [Pro Git：查看提交历史](https://git-scm.com/book/zh/v2/Git-%E5%9F%BA%E7%A1%80-%E6%9F%A5%E7%9C%8B%E6%8F%90%E4%BA%A4%E5%8E%86%E5%8F%B2)
- [Pro Git：分支的新建与合并](https://git-scm.com/book/zh/v2/Git-%E5%88%86%E6%94%AF-%E5%88%86%E6%94%AF%E7%9A%84%E6%96%B0%E5%BB%BA%E4%B8%8E%E5%90%88%E5%B9%B6)
- [Pro Git：项目分享与更新](https://git-scm.com/book/zh/v2/%E9%99%84%E5%BD%95-C%3A-Git-%E5%91%BD%E4%BB%A4-%E9%A1%B9%E7%9B%AE%E5%88%86%E4%BA%AB%E4%B8%8E%E6%9B%B4%E6%96%B0)
- [git switch 官方手册](https://git-scm.com/docs/git-switch)
- [git restore 官方手册](https://git-scm.com/docs/git-restore)
- [gitignore 官方手册](https://git-scm.com/docs/gitignore)
- [Git 官方命令总览](https://git-scm.com/docs/git)

### 附件中的中文教程

- [菜鸟教程 Git 教程](https://www.runoob.com/git/git-tutorial.html)
- [Git 安装配置](https://www.runoob.com/git/git-install-setup.html)
- [Git 工作流程](https://www.runoob.com/git/git-workflow.html)
- [Git 工作区 暂存区和版本库](https://www.runoob.com/git/git-workspace-index-repo.html)
- [Git 创建仓库](https://www.runoob.com/git/git-create-repository.html)
- [Git 基本操作](https://www.runoob.com/git/git-basic-operations.html)
- [Git 分支管理](https://www.runoob.com/git/git-branch.html)
- [Git 查看提交历史](https://www.runoob.com/git/git-commit-history.html)
- [Git 标签](https://www.runoob.com/git/git-tag.html)
- [Git Flow](https://www.runoob.com/git/git-flow.html)
- [Git 进阶操作](https://www.runoob.com/git/git-advance.html)
- [Git 远程仓库](https://www.runoob.com/git/git-remote-repo.html)

