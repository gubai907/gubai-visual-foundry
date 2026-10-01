# 安装与更新

**简体中文** | [English](installation.en.md)

[返回首页](../README.md) · [快速上手](quick-start.md) · [常见问题](faq.md)

## 安装前需要什么

- 能读取本地 Skill 的 Codex 环境。
- 完整的 `gubai-visual-foundry` 文件夹。
- 编写提示词不需要 Python 或单独的生图 API 密钥。实际生成媒体需要可用的生成工具及相应权限。

## 方法一：让 Codex 帮你安装

如果环境提供内置的 `skill-installer`，可以复制以下请求：

```text
请使用 $skill-installer，从 https://github.com/gubai907/gubai-visual-foundry 安装技能。
该仓库根目录就是 Skill 本体，技能路径为 .，安装名称为 gubai-visual-foundry。
保留全部支持文件；如果同名技能已存在，先说明现有版本，不直接覆盖我的本地修改。
```

安装器的目标位置可能采用环境配置的技能目录；以实际安装结果为准。安装后，在下一轮对话检查是否可选。

## 方法二：手动下载源码

1. 打开 [GitHub 仓库](https://github.com/gubai907/gubai-visual-foundry)。
2. 点击绿色 **Code → Download ZIP**。
3. 解压下载文件，找到直接包含 `SKILL.md`、`agents`、`core` 等内容的文件夹。
4. 将它从 `gubai-visual-foundry-main` 改名为 `gubai-visual-foundry`。
5. 将整个文件夹复制到以下任一位置。

| 安装范围 | 位置 |
|---|---|
| macOS / Linux 个人使用 | `~/.agents/skills/gubai-visual-foundry/` |
| Windows 个人使用 | `%USERPROFILE%\.agents\skills\gubai-visual-foundry\` |
| 仅当前项目 | `项目目录/.agents/skills/gubai-visual-foundry/` |

macOS 可在 Finder 使用 **前往 → 前往文件夹**，输入 `~/.agents/skills/`；目录不存在时创建。Windows 可在文件资源管理器地址栏输入 `%USERPROFILE%`，再创建 `.agents` 和其中的 `skills` 文件夹。点号是名称的一部分。

安装后的层级应为：

```text
skills/
└── gubai-visual-foundry/
    ├── SKILL.md
    ├── agents/
    ├── core/
    ├── locks/
    └── 其余支持文件与目录
```

不要只复制 `SKILL.md`，也不要让它藏在第二层同名文件夹里。

## 方法三：下载 Release 安装包

打开 [Releases](https://github.com/gubai907/gubai-visual-foundry/releases)，选择实际已发布的版本，在 **Assets** 中下载项目提供的 `gubai-visual-foundry-…zip`。若还没有 Release，使用方法二。

项目安装包解压后应直接得到 `gubai-visual-foundry` 文件夹，按上面的路径放置即可。GitHub 自动生成的 **Source code (zip)** 是源码快照，可能仍需处理文件夹名称。

如发布时同时提供 `.zip.sha256`，可用于检查下载包是否与发布者提供的校验值一致。校验值不是作者身份签名。

## 如何调用

- 桌面界面若提供技能选择器，输入 `@` 查找 **Gubai Visual Foundry**。
- Codex CLI 或 IDE 扩展可使用 `/skills`，或输入 `$gubai-visual-foundry`。
- 也可以在请求中明确说“请使用 Gubai Visual Foundry”。技能能否被调用以当前环境发现结果为准。

首次验证可以发送：

```text
请使用 $gubai-visual-foundry，为一只无品牌白色陶瓷杯写中文产品图提示词。
浅灰背景、侧面柔光、4:5 构图。只给提示词，暂不生成图片。
```

如果未出现，检查路径、目录层级与 `SKILL.md` 文件名，再重启 Codex。以 [OpenAI 官方技能文档](https://learn.chatgpt.com/docs/build-skills) 和实际界面为准。

## 更新已有安装

1. 先把旧版完整复制到技能目录之外的备份位置。
2. 保存自己修改过的配置和外部项目资料。
3. 下载新版本，核对 `README.md`、`SKILL.md` 和 [CHANGELOG](../CHANGELOG.md) 中的版本。
4. 用完整新目录替换旧目录，避免把两版支持文件混在一起。
5. 新一轮对话验证发现与调用；未更新时重启。

若原技能使用另一个名称，它与 `gubai-visual-foundry` 可能同时存在。安装新名称不会自动覆盖或迁移旧名称的个人资料。需要停用旧版时，先确认它的安装位置与本地修改。

## 移除

将此技能文件夹移出实际技能目录即可。先保留自己的修改和项目资料。其他位置存在同名安装时，也需要检查该位置。
