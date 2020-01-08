# dogpile_caching

Illustrates how to embed dogpile.cache functionality within the Query object, allowing full cache control as well as the ability to pull “lazy loaded” attributes from long term cache.

In this demo, the following techniques are illustrated:

- Using custom subclasses of Query
- Basic technique of circumventing Query to pull from a custom cache source instead of the database.
- Rudimental caching with dogpile.cache, using “regions” which allow global control over a fixed set of configurations.
- Using custom MapperOption objects to configure options on a Query, including the ability to invoke the options deep within an object graph when lazy loads occur.

The demo scripts themselves, in order of complexity, are run as Python modules so that relative imports work:

```
python -m dogpile_caching.helloworld
python -m dogpile_caching.relationship_caching
python -m dogpile_caching.advanced
python -m dogpile_caching.local_session_caching
```

## 注意

dogpile_caching 只能在 Linux 环境下才能正常运行

---

- doc: https://docs.sqlalchemy.org/en/13/orm/examples.html#module-examples.dogpile_caching
- dogpile.cache doc: https://dogpilecache.sqlalchemy.org/en/latest/
- dogpile.cache github: https://github.com/sqlalchemy/dogpile.cache
