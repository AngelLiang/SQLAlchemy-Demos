# Large Collections

举例说明，当related对象非常巨大的时候，配置 `relationship()` 选项，包括：

- 使用 `dynamic` 关系查询被访问的数据片。
- 如何在删除级联中，与 `passive_deletes=True` 结合使用，从而大大提高相关集合删除的性能。

---

- doc: https://docs.sqlalchemy.org/en/13/orm/examples.html#module-examples.large_collection

