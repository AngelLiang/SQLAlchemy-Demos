# 垂直属性映射

Illustrates “vertical table” mappings.

A “vertical table” refers to a technique where individual attributes of an object are stored as distinct rows in a table. The “vertical table” technique is used to persist objects which can have a varied set of attributes, at the expense of simple query control and brevity. It is commonly found in content/document management systems in order to represent user-created structures flexibly.

Two variants on the approach are given. In the second, each row references a “datatype” which contains information about the type of information stored in the attribute, such as integer, string, or date.

---

- doc: https://docs.sqlalchemy.org/en/13/orm/examples.html#module-examples.vertical
