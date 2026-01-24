from sqlalchemy import Column, Integer, String
from app.database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)  # 添加长度限制
    description = Column(String(255), index=True)  # 添加长度限制
    price = Column(Integer)