# Gubai Visual Foundry

版本：2.0.0-public.3。

可复用的视觉提示词工作台，支持产品商业图、电商、广告、时尚、人像、海报、受控编辑、精修、短视频与分镜。先分配参考图职责和保护字段，再根据任务与平台编译提示词。

## 安装

将完整的 `gubai-visual-foundry` 文件夹放入个人技能目录 `~/.agents/skills/`，或项目的 `.agents/skills/`。入口为 [SKILL.md](SKILL.md)；支持文件须一起保留。桌面端可用 `@` 选择技能，CLI 可用 `$gubai-visual-foundry` 指定调用。未出现时重启后再检查。安装位置与调用方式见 [OpenAI 官方技能文档](https://learn.chatgpt.com/docs/build-skills)。

## 使用示例

- 用图 A 保留人物身份，图 B 保留身材和衣鞋，图 C 只参考构图与光线，输出完整时尚提示词。
- 以原图为依据做精修提示词，保持身份、姿势、衣物、物件、背景、光线和裁切。
- 给出三镜产品视频分镜，每镜写一个动作、时长和段末可见状态。

需要实际生成媒体时，在请求中明确生成目标，并使用当前环境可用的生成工具。提示词编写和媒体完成分别验收。

## 配置与项目资料

[通用默认规则](profiles/user-defaults.md)按当前请求补齐语言和输出形式。专业角色前缀按明确请求启用。TapNow 使用精简句法；其他平台与完整输出仍保留必要的参考权限和 Locks。

真实品牌、产品和角色资料保存在外部项目中；使用 [品牌字段约定](profiles/profile-schema.md)和[角色库接口](profiles/model-library.md)提供本次任务需要的记录。[品牌示例](examples/brand-profile-example.md)是虚构结构。

私有配置、资产、历史对话和来源清单应保存在发布目录之外。

## 检查

校验脚本需要 Python 3.10 或以上版本，不需要第三方依赖；提示词任务本身不依赖 Python。实际生成图片或视频另需环境中可用的生成工具。在技能目录中运行：

```sh
python3 scripts/validate_skill.py
python3 scripts/run_prompt_regression.py
python3 tests/test_validation.py
```

可选 `--private-terms-file` 指向发布包外的本地词表，每行一个需排除的名称；词表不随包分发。

回归规格见 [regression-cases.md](tests/regression-cases.md)，已执行合同检查见 [prompt-only-regression.md](tests/prompt-only-regression.md)。确定性检查验证规则与固定样例的一致性，不能代替独立模型测试、厂商能力测试、实际图片评分或像素区域比对。

## 公开发布

发布文件、账号隐私和许可选择见 [GitHub 发布清单](PUBLISHING.md)。当前包尚未附加开源许可证；公开可见不等于已授予开源复用许可。确定许可后再加入 LICENSE，并更新此说明。
