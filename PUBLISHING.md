# GitHub 公开发布清单

适用版本：2.0.0-public.4。此文件是发布准备清单，不表示仓库、Release 或远程设置已经创建。

## 目录与文件

将本目录的内容作为仓库根目录。完整保留 SKILL.md、agents、core、locks、modules、profiles、platforms、knowledge、qa、examples、tests 和 scripts；不要只上传入口或压缩包。

| 项目 | 当前状态 | 用途 |
|---|---|---|
| SKILL.md 与支持文件 | 已备齐 | 技能入口、路由、规则和示例 |
| README.md | 已备齐 | 简介、安装、使用、检查及能力边界 |
| .gitignore | 已备齐 | 排除本地配置、项目资料、缓存、凭据文件和备份 |
| CHANGELOG.md | 已备齐 | 公开版本记录 |
| 校验、合同检查与失败场景测试 | 已备齐 | 检查结构、规则样例及校验脚本行为 |
| LICENSE 与 NOTICE.md | 已备齐：CC BY-NC 4.0，Gubai 署名 | 明确非商业复用范围与署名要求 |

本项目采用 CC BY-NC 4.0，允许非商业使用、修改和分享，按条款保留署名、许可、来源并注明改动；商业使用须另获授权。含非商业限制，不将本项目描述为开放源代码许可项目。许可授予只能覆盖自己有权授权的材料；外部品牌、图片、字体和其他第三方资产须另核对来源及许可。[GitHub 许可说明](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)

## 发布前检查

- 仅从独立公开目录创建仓库；原技能、历史 ZIP、项目 Profile、证据目录、聊天记录、审计记录和私有词表保留在目录外。
- 检查实际待提交文件及内容；.gitignore 不能自动清除已经跟踪的文件或历史提交中的信息。[GitHub 忽略文件说明](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files)
- 已经存在的仓库应另外检查全部提交、标签、分支、LFS、附件与公开内容；本地 ZIP 检查不覆盖远程历史。已公开内容可能在其他副本中保留。[GitHub 历史敏感信息说明](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
- 公共项目名为 Gubai；公开的通用方法、提示词结构和代码会被别人看到。发布前确认愿意公开这些内容且拥有相应权利。
- 查看仓库名、描述、README、示例及发布附件中是否还有不希望公开的署名或业务线索。
- 在目录内运行以下检查；私有词表必须位于目录之外。不要把词表、输出中出现的真实姓名或本地审计记录提交。

```sh
python3 scripts/validate_skill.py
python3 scripts/run_prompt_regression.py
python3 tests/test_validation.py
```

可选的本地隐私检查：给 validate_skill.py 增加 `--private-terms-file` 参数。该检查读取 UTF-8 文本与文件名，不代替人工核对，也不审计 Git 历史。

## 账号与仓库设置

| 项目 | 建议 |
|---|---|
| 仓库名 | gubai-visual-foundry |
| 描述 | Controlled visual prompts for images, edits and storyboards |
| 默认分支 | main |
| 可见性 | 完成待提交文件核对后设为 Public |
| Topics | codex、skills、visual-prompts、image-editing、storyboard |
| 提交署名 | 选择愿意公开的作者名；使用 GitHub 账号提供的 noreply 邮箱 |
| 首次 Release | 标签 v2.0.0-public.4；说明功能、变化与测试范围；附清洁 ZIP 及 SHA-256 |

GitHub 账号、公开个人资料及提交作者名仍可见。隐藏邮箱设置不会替换已有提交中的邮箱；本地提交应单独使用账号的 noreply 地址，并核对提交作者及提交者元数据。[GitHub 邮箱隐私说明](https://docs.github.com/en/account-and-profile/concepts/email-addresses)

检查脚本允许工作副本存在 `.git` 元数据；打包时必须排除整个 `.git`。Release 的 ZIP 应只包含技能目录；校验和作为单独附件或发布说明提供。此次本地打包已排除 Git、系统元数据和本地记录。

## 可选维护项

- CONTRIBUTING.md：说明提问题、修改规则与提交贡献的方法。
- SECURITY.md：设定有效的私密问题反馈渠道；需要维护者提供真实可用的渠道。
- Issue / PR 模板：统一必要复现资料，提醒不要附私有资产或凭据。
- GitHub Actions：在后续修改时自动运行结构、合同及脚本行为检查。
- 分支保护与发布标签管理：协作维护时启用。

这些项目可后续补齐，不是 GitHub 公开仓库的强制文件。

## 验证边界

确定性合同检查核对固定样例和源规则；脚本行为测试验证正常及失败情况。未执行独立模型遵循性测试、真实媒体生成、厂商能力测试或像素保护区比对。许可已按维护者选择加入；发布前仍需核对材料权利、账号公开资料和最终远程提交内容。
