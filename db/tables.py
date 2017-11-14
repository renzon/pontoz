from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, DateTime, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class Partner(Base):
    __tablename__ = 'partner'
    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    segment = Column(String(60))


class Region(Base):
    __tablename__ = 'region'
    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    partner_id = Column(Integer, ForeignKey('partner.id'), nullable=False)
    partner = relationship(Partner, innerjoin=True)


class Store(Base):
    __tablename__ = 'store'
    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    region_id = Column(Integer, ForeignKey('region.id'), nullable=False)
    region = relationship(Region, innerjoin=True)


class Transaction(Base):
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey('store.id'), nullable=False)
    store = relationship(Store, innerjoin=True)
    creation = Column(DateTime())
    sale = Column(DECIMAL(2))
    pointz_sale = Column(DECIMAL(2))


engine = create_engine(
    "mssql+pyodbc://SA:Passw0rd@MYMSSQL"
)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
