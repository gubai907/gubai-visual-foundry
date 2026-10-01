# Gubai Visual Foundry

**把你的画面需求、参考图和修改要求，整理成可执行的视觉提示词。**

面向产品、电商、广告、时尚、人像、海报和短视频创作。你可以指定每张参考图负责什么、哪些内容要保留、这次允许改什么，再为目标平台整理提示词或分镜。

V2 公开版：`2.0.0-public.4` · 维护署名：**Gubai**

[快速上手](docs/quick-start.md) · [安装教程](docs/installation.md) · [完整案例](docs/examples.md) · [常见问题](docs/faq.md) · [版本记录](CHANGELOG.md) · [下载页面](https://github.com/gubai907/gubai-visual-foundry/releases)

## 能帮你做什么

| 任务 | 示例用途 | 交付内容 |
|---|---|---|
| 产品、电商与广告 | 产品主图、场景图、广告视觉 | 产品特征、构图、光线与材质明确的提示词 |
| 时尚与人物 | 指定人物、衣着和参考构图 | 分配参考图职责的提示词 |
| 图片编辑与精修 | 更换指定背景、保留原图主体、修复局部问题 | 修改目标与保留要求清楚的编辑提示词 |
| 海报与社交内容 | 组织视觉主体、文案和版面 | 画面及排版提示词 |
| 短视频与分镜 | 产品展示、连续镜头、首尾状态规划 | 分镜表及每镜提示词 |

需要实际生成图片或视频时，请明确提出，并使用当前环境可用的生成工具；只写出提示词不代表媒体已经生成。

## 核心能力

- **让多张参考图各司其职**：分别指定人物、衣物、产品、道具、构图、环境或光线来源。
- **区分修改与保留**：本轮允许改变的内容单独说明，其余要求继续保持。
- **根据用途组织表达**：产品图、人物、编辑、海报与分镜使用对应模块。
- **处理系列连续性**：复用已确认的角色、服装、物件与场景设定。
- **局部修正失败结果**：指出当前问题，围绕一个主要变量提出修复要求。

这些是提示词与验收规则。身份、产品细节、文字和局部保留的实际效果，仍需查看生成结果确认。

## 一分钟上手

安装后，在 Codex 中选择此技能，或输入下面的请求。示例中的保温杯为虚构对象；如需保留真实产品，请同时提供产品参考图。

```text
请使用 $gubai-visual-foundry：
为一只无品牌的哑光浅灰色保温杯写一条产品场景图提示词。
用途：电商详情页。
画面：杯子直立在浅色木桌上，窗侧柔和自然光，背景简洁。
比例：4:5。
保留要求：杯身比例、杯盖结构和浅灰色表面。
不要新增品牌标志、文字、水滴或装饰道具。
只输出中文提示词，暂不生成图片。
```

有参考图时，上传图片后说明职责，例如：图 A 负责产品外形，图 B 只参考构图和光线。更多用法见 [快速上手](docs/quick-start.md) 和 [完整案例](docs/examples.md)。

## 安装

当前仓库根目录就是 Skill 本体，入口为 [SKILL.md](SKILL.md)。安装时保留完整目录。

1. 从仓库 **Code → Download ZIP** 下载源码；有已发布的安装包时，也可以从 [Releases](https://github.com/gubai907/gubai-visual-foundry/releases) 下载。
2. 解压，找到直接包含 `SKILL.md` 的文件夹。源码文件夹若叫 `gubai-visual-foundry-main`，将其改名为 `gubai-visual-foundry`。
3. 将完整文件夹放入个人技能目录，或当前项目的 `.agents/skills/`。

| 系统 | 个人安装位置 |
|---|---|
| macOS / Linux | `~/.agents/skills/gubai-visual-foundry/` |
| Windows | `%USERPROFILE%\.agents\skills\gubai-visual-foundry\` |

也可以请求内置的 `skill-installer` 从本仓库安装，明确指定仓库根目录为技能路径、技能名为 `gubai-visual-foundry`。

详细步骤、更新与排错见 [安装教程](docs/installation.md)。技能发现与调用方式依据 [OpenAI 官方技能文档](https://learn.chatgpt.com/docs/build-skills)。

## 平台与输出

| 适配规则 | 用途 |
|---|---|
| 通用 | 平台未指定时，输出自然语言提示词 |
| ChatGPT Image | 整理图像创作与编辑要求 |
| 即梦 | 按当前请求组织图像或视频提示词 |
| TapNow | 使用精简表达，保留必要控制要求 |

适配规则负责提示词表达；实际参考图数量、编辑方式、尺寸和视频时长取决于当前工具。语言和长短遵循你的请求。品牌文案、产品尺寸等未知信息不会作为真实参数补入。

## 目录说明

| 路径 | 职责 |
|---|---|
| [SKILL.md](SKILL.md) | 技能入口、任务处理与读取规则 |
| `agents/` | 技能显示信息 |
| `core/` | 任务路由、参考图职责、输出与连续性规则 |
| `locks/` | 身份、身材、衣着、产品、道具和文字的保留规则 |
| `modules/` | 11 个专业任务模块 |
| `platforms/` | 4 个平台表达适配器 |
| `knowledge/` | 摄影、光线、构图、材质与色彩参考 |
| `profiles/` | 通用默认规则及外部品牌、角色资料接口 |
| `qa/` | 结果检查和局部修复规则 |
| `docs/` | 安装、上手、案例与常见问题 |
| `examples/` | 虚构品牌资料示例 |
| `scripts/`、`tests/` | 包结构检查和回归规格 |

## 项目资料与隐私

真实品牌、产品和角色资料由当前项目提供。字段说明见 [品牌资料约定](profiles/profile-schema.md)、[角色资料接口](profiles/model-library.md)；[品牌示例](examples/brand-profile-example.md)使用虚构资料。

自己的项目资料、照片、凭据、历史对话和备份请保存在公开仓库之外。`.gitignore` 用于忽略匹配的未跟踪文件，不能替代上传前检查，也不能清除已经提交的内容。

## 维护者检查

日常写提示词不需要 Python。运行检查脚本需要 Python 3.10 或以上版本，无第三方依赖。在技能目录中执行：

```sh
python3 scripts/validate_skill.py
python3 scripts/run_prompt_regression.py
python3 tests/test_validation.py
```

可用 `--private-terms-file` 指向公开包外的本地排除词表。检查规格见 [回归清单](tests/regression-cases.md)。确定性检查不能代替独立模型测试、真实生图测试或像素区域比对。

## 许可与发布

本项目采用 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)（署名—非商业性使用 4.0 国际）许可。允许非商业使用、修改和分享；分享时须保留署名、许可及来源，修改后注明改动。商业使用需要另行获得维护者授权。

署名：**Gubai**。完整条款见 [LICENSE](LICENSE)，权利与署名说明见 [NOTICE.md](NOTICE.md)。含非商业限制，因此不将本项目描述为开放源代码许可项目。

发布说明见 [RELEASE_NOTES.md](RELEASE_NOTES.md)，维护步骤见 [PUBLISHING.md](PUBLISHING.md)。下载页面中实际发布的版本为准；本文件中的版本号不表示 Release 已创建。
