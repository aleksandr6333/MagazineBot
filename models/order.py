from sqlalchemy import Column, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from models.product import Products, Services
import datetime



Base = declarative_base()

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    data = Column(DateTime)
    product_id = Column(Integer, ForeignKey('product.id'))
    uder_id = Column(Integer)

    products = relationship(
        Products,
        backref = backref(
            'orders',
            uselist=True,
            cascade='delete,all'
        )
    )

    def __str__(self):
        return f"{self.quantity} {self.data}"

class ProvisionService(Base):
    __tablename__ = 'provision_services'

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    data = Column(DateTime, default=datetime.datetime.now)
    product_id = Column(Integer, ForeignKey('services.id'))

    services = relationship(
        Services,
        backref = backref(
            'provision_services',
            uselist=True,
            cascade='delete,all'
        )
    )

    def __str__(self):
        return f"{self.quantity}{self.data}"