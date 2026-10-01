# Locks 索引

只加载可见且需控制的对象：[identity](identity-lock.md)、[body](body-lock.md)、[wardrobe/shoes](wardrobe-lock.md)、[product](product-lock.md)、[prop](prop-lock.md)、[text/brand](text-brand-lock.md)。
每项记录来源、可见结构、保护字段、允许修改字段、semantic 或 pixel 强度。衣鞋归 wardrobe；商品与辅助道具按当前画面商业角色区分，同一物件不要建立互相竞争的两个锁。
像素锁由 product-lock 定义，也适用于需要原像素保留的道具/其他补丁。提示词表达要求，工具是否真正保留须另行核验。
