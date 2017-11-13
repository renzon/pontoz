from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Partner(Base):
    __tablename__ = 'partner'
    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    segment = Column(String(60))


engine = create_engine(
    "mssql+pyodbc://SA:Passw0rd@MYMSSQL"
)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


