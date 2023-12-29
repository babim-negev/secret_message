import uuid

from passlib.hash import pbkdf2_sha256
from sqlalchemy import Column, String, DateTime, func
from sqlalchemy import Integer

from src.db.database import Base




class Secret(Base):
    __tablename__ = 'secret_table'

    secret_key = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    message = Column(String)
    hashed_passphrase = Column(String, nullable=True)
    create_date = Column(DateTime(timezone=True), default=func.now())
    TTL = Column(String)
