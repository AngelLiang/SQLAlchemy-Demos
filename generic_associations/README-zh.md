# 通用关联

- table_per_association.py: 定义一个mixin，它通过为每个父类单独生成的关联表，并提供一个泛型关联。关联的对象本身被持久化到所有父对象共享的一个表中。

- table_per_related.py: 定义一个泛型关联，该关联将关联对象持久存储在单个表中，每个表生成一个泛型关联，以代表特定的父类持久存储这些对象。

- discriminator_on_association.py: 定义一个mixin，它使用一个目标表和一个由所有父表引用的关联表来提供一个通用关联。关联表包含一个“discriminator” column ，该列确定父对象的类型与关联表中的每个特定行相关联。

- generic_fk.py: 类似于Django、ROR等流行框架的方式声明所谓的“通用外键”。这种方法绕过了标准的引用完整性实践，因为“外键” column 实际上并不局限于引用任何特定的表；相反，应用程序内逻辑用于确定引用哪个表。

---

- doc: https://docs.sqlalchemy.org/en/13/orm/examples.html#module-examples.generic_associations
