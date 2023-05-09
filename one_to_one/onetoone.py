from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__)) #Define dir where is running
conn_str = os.path.join(BASE_DIR,'db_data.txt') #Join the db data file to the base dir
with open(conn_str, 'r') as db_string: #Read the data inside the file
    db_data = db_string.read().strip()

engine = create_engine(db_data,echo=True) #echo show in terminals querys executed.
Base = declarative_base()

class Husband(Base):
    __tablename__ = 'husbands_list'

    husband_id = Column(Integer(),primary_key=True)
    husband_name = Column(String(25))
    husband_lastname = Column(String(25))
    wife = relationship('Wife', back_populates='husband',uselist=False, cascade = 'all, delete')

    def __repr__(self):
        return f'Mr. {self.husband_name} {self.husband_lastname}'


class Wife(Base):
    __tablename__ = 'wifes_list'

    wife_id = Column(Integer(),primary_key=True)
    wife_name = Column(String(25))
    wife_lastname = Column(String(25))
    husband_id = Column(Integer(),ForeignKey('husbands_list.husband_id', ondelete='CASCADE'))
    husband = relationship('Husband', back_populates='wife')

    def __repr__(self):
        return f'Ms. {self.wife_name} {self.wife_lastname}'


Base.metadata.create_all(engine) #Only the first time to create tables
session = sessionmaker()(bind=engine)