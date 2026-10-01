# Model Library Interface

仅在用户指定角色或需要系列复用时加载项目内相关记录；不遍历全库。
最小记录：`namespace / model_id / revision / status / identity_master / auxiliary_views / stable_identity_anchors / body_reference / allowed_styling / verified_views / known_failures`。
status：临时、候选、可复用。可复用只表示在记录的用途与角度验证过，不保证跨工具一致。
风格/人群模板与身份记录是不同类型：模板可用于原创临时人物，只有可用母图才提供明确的同一身份依据。
品牌专属 ID 留在各自命名空间，禁止映射成所有品牌的默认模特。不自动新增、删除或改写项目人物；临时 Prompt 不沉淀成永久角色，除非用户要求。

## 最小角色档案

```text
角色名称或临时代号：
namespace / model_id / revision：
当前状态：临时 / 候选 / 可复用
主身份母图：
辅助角度图：
Body Reference：
不可变身份锚点：脸型骨相、关键五官比例、肤色范围、发际线、自然发色、耳位、稳定识别点
允许变化：服装、发型表达、姿态、背景、道具、光线、季节
排除项：不得继承的其他人物特征
已验证角度/用途：
已知失败风险：
```

- 临时：只服务当前一张图。
- 候选：已有母图和锚点，但跨角度/造型尚未验证。
- 可复用：仅在记录的用途和角度验证过，不代表所有平台绝对一致。

没有主身份母图时不得把文字模板或人群标签当成同脸依据。
