# image-editing

先给出 source、protected_region、editable_region、allowed_delta。保护补丁包括连接点、遮挡、阴影和必要紧邻边界；不能只保护物体中央。
换原创人物：源人物仅提供被允许的构图，重建区不继承原脸、发、肤色和辨识特征；姿势/衣服仅在授权范围重置，并保持产品补丁需要的最小几何关系。
保留同一人物的编辑则读取 Identity Lock，不能混用“身份重置”语句。替换背景不自动改变人物打光，若明显不协调只指出具体冲突。
像素级保留依赖实际工具与验证；无局部能力时不承诺精准保护。洗细节走 refine；失败输出走单变量 repair。

## 换成原创人物的三段控制

```text
Protected Source Patch Lock: Treat the source product/object pixels, attachment
points, natural overlap, contact shadows and original perspective as one immutable
photographic patch. Do not repaint or reconstruct this protected patch.

Model/Character Identity Reset: The source person supplies composition only, not an
identity reference. Rebuild every unprotected human region as one clearly described
original person; do not inherit the source face, age impression, hair, skin, or
recognizable traits.

Authorized Pose / Wardrobe / Setting Changes: Change only the explicitly approved
fields in [allowed_delta]. Keep the source pose, wardrobe and setting unchanged
when they are outside that scope. Preserve the minimum local geometry needed by
the protected product/object patch; do not expand this into a full-scene redesign.
```

仅在任务存在源产品/物体保护区时加入第一段；第二段用于明确要求“换成原创人物”，不能扩大到保护区内的人体。第三段列出具体获准变化；没有获准变化时保持原姿势、衣着和场景。保留同一人物、仅换背景/衣服时不得使用 Identity Reset，并且只释放用户授权字段。
