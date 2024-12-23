# Placeholder for ORM implementation
# Directory: utils/orm.py
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///test_data.db')
Base = declarative_base()


class TestResult(Base):
    __tablename__ = 'test_results'
    id = Column(Integer, primary_key=True)
    test_name = Column(String)
    status = Column(String)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def save_test_result(test_name, status):
    result = TestResult(test_name=test_name, status=status)
    session.add(result)
    session.commit()
