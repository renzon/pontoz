from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, DateTime, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class Partner(Base):
    __tablename__ = 'partner'
    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    segment = Column(String(60))
    # regions = relationship('Region')


class Region(Base):
    __tablename__ = 'region'
    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    partner_id = Column(Integer, ForeignKey('partner.id'))
    partner = relationship(Partner)


class Store(Base):
    __tablename__ = 'store'
    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    region_id = Column(Integer, ForeignKey('region.id'))
    region = relationship(Region)


class Transaction(Base):
    __tablename__ = 'store'
    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey('store.id'))
    store = relationship(Store)
    creation = Column(DateTime())
    sale = Column(DECIMAL(2))
    ponitz_sale = Column(DECIMAL(2))


engine = create_engine(
    "mssql+pyodbc://SA:Passw0rd@MYMSSQL"
)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
