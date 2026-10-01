# Source Governance

维护者明确指定维护源；完整 Skill、Chat 版和精简版记录来源版本。正常方向为：维护源 → 完整 Skill → Chat / 精简派生版。禁止派生版反向覆盖维护源。
反馈先形成变更建议，再在用户授权下更新维护源，然后重新生成派生版；本轮 Prompt 调整不等于永久改写 Skill。
治理记录最少包含 `canonical_source / source_revision_or_hash / derived_version / generated_at / changed_rule_ids`。项目源路径和私有记录保存在项目本地，不写入通用发布包。
无法确认来源或归属的规则不得启用为全局默认；先保留来源与未决原因，待来源确认后再纳入。
Chat/精简版压缩不得削弱引用权限、Hard Lock、编辑范围或单变量修复。平台 Prompt 适配和 Skill 派生版本是两件事，不把平台适配器作为第二维护源。
