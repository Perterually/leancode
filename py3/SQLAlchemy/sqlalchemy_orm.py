import time 
import sqlite3

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()
session = scoped_session(sessionmaker())

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

def init_db(dbname='sqlite:///example.db'):
    engine = create_engine(dbname, echo=True)
    session.remove()
    session.configure(bind=engine, autoflush=False, expire_on_commit=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    return engine

def test_sqlchemy_orm(numbe_of=10000):
    init_db()
    start = time.time()
    for i in range(numbe_of):
        user = User()
        user.name = 'name' + str(i)
        session.add(user)
    session.commit()
    end = time.time()
    print("SQLAlchemy ORM: Insert {0} records in {1} seconds".format(str(numbe_of),str(end - start)))


def test_sqlalchemy_core(number_of=10000):
    engine = init_db()
    

test_sqlchemy_orm()
