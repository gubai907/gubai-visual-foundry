# Task Router

内部建立最小任务记录，不强制向用户展示表单：
`deliverable | operation | subject_mode | reference_roles | locked_fields | allowed_delta | module | brand | platform | verbosity | aspect_ratio | continuity`。
operation = new / edit / refine / repair；交付形式 prompt 或 media 由用户需求与 profile 决定，不从模块名推断生成授权。

## 四问路由

1. Deliverable：单张静态图、受控编辑、洗图/高清、短片、分镜、封面还是完整视觉包？
2. Lock：人物身份、身材、衣鞋、产品、道具、文字、构图、背景和光线中，哪些必须保持？本轮唯一允许变化是什么？
3. Subject：临时人物、来源身份保留、固定角色、换成原创人物、hands-only 还是无人？
4. Continuity：独立输出、系列组图、与已确认前一帧相邻，还是首尾帧过渡？

| 用户目标 | 主模块 | 条件辅助 |
|---|---|---|
| 产品英雄图、商业静物 | [product-commercial](../modules/product-commercial.md) | 参考转译 |
| 白底、PDP、PLP、详情图 | [ecommerce](../modules/ecommerce.md) | 产品商业 |
| 时尚杂志、lookbook、穿搭、服装 campaign | [fashion](../modules/fashion.md) | 美妆人像 |
| 肖像、美妆近景、妆造 | [beauty-portrait](../modules/beauty-portrait.md) | 时尚 |
| 广告主视觉、概念 campaign | [advertising](../modules/advertising.md) | 产品商业或时尚，按主角选择 |
| 社媒封面、生活方式内容 | [social-content](../modules/social-content.md) | 产品或人物模块 |
| 平面海报、字体排版 | [graphic-poster](../modules/graphic-poster.md) | 文字品牌 Lock |
| 短视频、分镜、首尾帧 | [video-storyboard](../modules/video-storyboard.md) | 所需静态领域 |
| 换人、换物、换背景、局部改图 | [image-editing](../modules/image-editing.md) | 被编辑的专业领域 |
| 洗图、高清、精修且保持画面 | [refine-upscale](../modules/refine-upscale.md) | 不加载新风格模块 |
| 拆解/翻译参考图视觉语言 | [reference-translation](../modules/reference-translation.md) | 目标用途模块 |

主体模式：临时人物 / 来源身份保留 / 固定角色 / 换成原创人物 / hands-only / 无人。
保留给定人脸可用于单图，无须先建立永久角色档案；系列则登记母图。只给角色编号、气质或肤色不等于提供身份母图。人物不可见时省略相关控制。
“洗图并换衣”是两种编辑意图：明确的换衣先走 edit，再对获批版本 refine；不要在保真洗图内暗中换衣。
多图先判断角色；关键冲突无法推断时只澄清冲突字段，其余工作继续。资料欠缺但不影响交付时采用暂定值，不虚构结构、尺寸或身份。

## 品牌输入与资产边界

只有品牌导向任务才读取品牌或项目简报。简报可提供市场、受众、渠道、信息层级、色彩/材质边界、可接受的实验范围、卖点与宣称边界、Logo/文字使用规则。品牌简报不能代替产品母图、身份母图或精确文字资产。

品牌 brief、SKU 库、人物档案、参考图语法卡和测试记录留在项目/profile 中；通用 Core 不复制专属人物、地域定位、色盘或历史失败图。未提供品牌档案时不得从品类、地域或审美词推断某个品牌。

## 最早缺失环节

| 目标 | 必要的最早输入 | 缺失时处理 |
|---|---|---|
| 保留真实产品/道具并重构画面 | 清晰母图或实拍中的保护区域 | 询问主参考，或明确降级为灵感重建 |
| 固定角色跨图复用 | 经确认身份母图/角色档案 | 先按临时人物，不能承诺同脸 |
| 相邻视频镜头 | 已确认上一帧或首帧 | 先生成并确认起始帧 |
| 精确 Logo/文字 | 可用资产/原文 | 标记待确认，不凭空补写 |
| 复杂受控编辑 | 可用工具是否支持蒙版/局部编辑 | 缩小编辑范围或说明无法保证像素级保留 |

只有缺失会导致身份、产品、连续性或精确文字失控时才暂停；否则使用克制默认值并把未确认项标为暂定。

## 读取预算

- 快速 Prompt：路由 + 一个直接相关 Lock/模块 + profile（如命中）+ adapter + output/QA。
- 普通任务：主模块 + 所需 Locks + 一个必要知识文件；不要因为同图有人、有产品、有视频就加载全库。
- 高风险编辑/修复：仅为已确认问题追加一个诊断文件。

用户明确“直接给提示词”时仍输出 NORMAL，除非同时说“精简/一句话/TapNow”。
