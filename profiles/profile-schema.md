# External Brand Profile Schema

品牌 Profile 是项目资产，不属于通用 Skill。只有用户明确品牌，且当前项目提供对应 Profile 时才加载；品牌名或品类本身不能触发猜测。

建议字段：

```text
profile_id / brand_name / revision / source_of_truth
market / audience / positioning / price_or_value_tier
brand_tone / approved_copy / prohibited_claims
channel_rules / palette / material_language / composition_boundary
product_categories / product_facts_source / text_logo_rules
model_template_namespace / continuity_assets
known_failures / unresolved_rules
```

规则：

- `source_of_truth` 指向品牌自己的权威文件；通用 Skill 不反向覆盖。
- 品牌定位、色盘、渠道和模板只影响明确属于该品牌的任务。
- 产品结构与颜色以当前 SKU 资产为准，不能由品牌 Profile 代替。
- 人群/造型模板不是 Identity Master；同脸任务仍须身份母图。
- 未确认文案、HEX、宣称、尺寸和人物身份不得补造。
- Profile 与当前用户指令冲突时，先按字段判断本轮 `allowed_delta`；品牌事实不能覆盖用户明确选择的其他品牌或产品。
