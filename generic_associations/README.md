# Generic Associations

Illustrates various methods of associating multiple types of parents with a particular child object.

The examples all use the declarative extension along with declarative mixins. Each one presents the identical use case at the end - two classes, Customer and Supplier, both subclassing the HasAddresses mixin, which ensures that the parent class is provided with an addresses collection which contains Address objects.

The discriminator_on_association.py and generic_fk.py scripts are modernized versions of recipes presented in the 2007 blog post Polymorphic Associations with SQLAlchemy.

Listing of files:

- table_per_association.py - Illustrates a mixin which provides a generic association via a individually generated association tables for each parent class. The associated objects themselves are persisted in a single table shared among all parents.

- table_per_related.py - Illustrates a generic association which persists association objects within individual tables, each one generated to persist those objects on behalf of a particular parent class.

- discriminator_on_association.py - Illustrates a mixin which provides a generic association using a single target table and a single association table, referred to by all parent tables. The association table contains a “discriminator” column which determines what type of parent object associates to each particular row in the association table.

- generic_fk.py - Illustrates a so-called “generic foreign key”, in a similar fashion to that of popular frameworks such as Django, ROR, etc. This approach bypasses standard referential integrity practices, in that the “foreign key” column is not actually constrained to refer to any particular table; instead, in-application logic is used to determine which table is referenced.

---

- doc: https://docs.sqlalchemy.org/en/13/orm/examples.html#module-examples.generic_associations
