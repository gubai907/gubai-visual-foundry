# Prompt Compiler

先形成平台无关的内部记录：
```
Task: deliverable, operation, aspect_ratio, duration
Sources: ref_id, role, evidence, unknowns
Locks: field, source, strength(semantic/pixel), scope
Scene: subject, wardrobe, pose/action, prop, environment
Visual: composition, camera, lighting, material, mood
Continuity: approved_anchor, frozen_state, primary_delta
Output: language, verbosity, platform
QA: conflicts, missing_evidence, relevant_negatives
```
字段不适用就省略。Profile 在编译前补齐默认值；禁止补写未经证实的资产特征。

## 三种编译

- NORMAL：输出必要参考权限、所有适用锁、一个主动作及视觉层。摄影参数只选一套，不堆相机品牌。Negative 按本图可见风险选择，不复制全部负面库。
- COMPACT：合并重复锁为直白句，保留每个关键对象的来源和不可变项，再写主动作和主视觉。短到不能承载关键锁时允许略长，不能丢失语义。
- REFINE：只编译源图保留 + 可增强细节白名单 + 禁改字段。丢弃新造型、新姿态、新调色、新景深等候选，不追加 editorial/cinematic 美化前缀。

operation 决定修改权限，platform 决定表述；TapNow 的 refine 也只能洗细节，不能因短句模式丢掉冻结项。
专业前缀仅从匹配模块和用户偏好触发，写一次即可；前缀不获得任何覆盖 Lock 的权限。

编译后逐字段比对：源图角色是否被混用？锁是否在短版丢失？正负要求是否冲突？是否新增未授权变量？是否把像素保留要求写成了已实现的保证？通过后才交付。
