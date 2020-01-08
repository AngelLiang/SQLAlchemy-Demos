# 有向图（Directed Graphs）

一个有向图结构的持久性示例。图被存储为边的集合，每个边都引用节点表中的 `lower` 和 `upper` 节点。基本的持久性和查询 lower-and upper-neighbors 说明如下：

```Python
n2 = Node(2)
n5 = Node(5)
n2.add_neighbor(n5)
print n2.higher_neighbors()
```

---

- doc: https://docs.sqlalchemy.org/en/13/orm/examples.html#module-examples.graphs

