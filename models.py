from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship

from database import Base

class Built(Base):
    __tablename__ = "built"
    
    serial = Column(Integer, primary_key=True, index=True)
    brand = Column(String, nullable=True)
    movement = Column(String, nullable=True)
    case_material = Column(String, nullable=True)
    bracelet_material = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    shape = Column(String, nullable=True)
    crystal = Column(String, nullable=True)
    dial= Column(String, nullable=True)
    bracelet_color = Column(String, nullable=True)
    clasp = Column(String, nullable=True)
    year = Column(Date,nullable=True)

    nums = relationship('Num',back_populates='built',uselist=False)

class Num(Base):
    __tablename__ = "num"

    serial = Column(Integer, ForeignKey('built.serial') ,primary_key=True, index=True)
    brand = Column(String, nullable=True)
    gender = Column(String, nullable=True)   
    price = Column(Integer,nullable=True)
    total_sale = Column(Integer,nullable=True)
    seller_reviews = Column(Integer,nullable=True)
    year = Column(Date,nullable=True)
    volume = Column(Integer,nullable=True)

    built = relationship("Built",back_populates="nums",uselist=False)