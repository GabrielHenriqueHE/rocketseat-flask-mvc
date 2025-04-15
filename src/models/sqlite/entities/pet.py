from sqlalchemy import Column, BIGINT, String

from src.models.sqlite.settings.base import Base

class PetsTable(Base):
    __tablename__ = 'pets'

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)

    def __repr__(self):
        return f"<PetsTable(id={self.id}, name={self.name}, type={self.type})>"