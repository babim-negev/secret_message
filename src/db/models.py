import uuid

from passlib.hash import pbkdf2_sha256
from sqlalchemy import Column, String, DateTime, func
from sqlalchemy import Integer

from src.db.database import Base



# TODO ДОПИСАТЬ BASE ИМПОРТ
class Secret(Base):
    __tablename__ = 'secret_table'

    secret_key = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    message = Column(String)
    hashed_passphrase = Column(String, nullable=True)
    create_date = Column(DateTime(timezone=True), default=func.now())
    TTL = Column(String)

    @classmethod
    def create_secret(cls, message: str, passphrase: str = None):
        hashed_passphrase = None
        if passphrase:
            # Хешируем пароль, используя passlib
            hashed_passphrase = pbkdf2_sha256.hash(passphrase)

        return cls(message=message, hashed_passphrase=hashed_passphrase)
