from sqlalchemy import BigInteger, Column, Index, String, text, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Device(Base):
    __tablename__ = 'devices'
    __table_args__ = (
        Index('devices_dev_id_dev_type_index', 'dev_id', 'dev_type'),
    )

    id = Column(BigInteger, primary_key=True)
    dev_id = Column(String(200), nullable=False)
    dev_type = Column(String(120), nullable=False)


class Endpoint(Base):
    __tablename__ = 'endpoints'

    id = Column(BigInteger, primary_key=True)
    device_id = Column(ForeignKey('devices.id', ondelete='CASCADE', onupdate='CASCADE'))
    comment = Column(Text)

    device = relationship('Device')
