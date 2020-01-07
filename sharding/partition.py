"""水平分表（单库多表）示例"""
import sys
from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

echo = '-v' in sys.argv

if '--postgres' in sys.argv:
    dburl = 'postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/partition'
else:
    dburl = 'sqlite:///:memory:'

class_registry = {}
engine = create_engine(dburl, echo=echo)
Base = declarative_base(engine)
Session = sessionmaker(bind=engine)
session = Session()


class AbstractClass(Base):
    __abstract__ = True
    # __tablename__ should be 'model_%s'

    id = Column(Integer, primary_key=True)
    name = Column(String(11))
    password = Column(String(128))


def make_model(ident):

    def generate_class_name_and_table_name(ident):
        return 'ModelClass%s' % ident, 'model_%s' % ident

    if ident not in class_registry:
        cls_name, table_name = generate_class_name_and_table_name(ident)
        cls = type(cls_name, (AbstractClass, ), {'__tablename__': table_name})
        class_registry[ident] = cls

    return class_registry[ident]


model1 = make_model('201912')
model2 = make_model('202001')


Base.metadata.drop_all()
Base.metadata.create_all()

admin = model1(name='admin')
session.add(admin)
session.commit()
session.query(model1).all()

user1 = model2(name='user1')
user2 = model2(name='user3')
user3 = model2(name='user3')
session.add_all([user1, user2, user3])
session.commit()
