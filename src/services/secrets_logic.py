from passlib.hash import pbkdf2_sha256
from src.db.models import Secret
import uuid
def create_secret(message, db):
    hashed_passphrase = None
    if message.passphrase:
        hashed_passphrase = pbkdf2_sha256.hash(message.passphrase)

    secret_model = Secret(
        message=message.secret_message,
        hashed_passphrase=hashed_passphrase,
        TTL=message.ttl  # Добавляем TTL в модель
    )
    secret_model.secret_key = str(uuid.uuid4())

    db.add(secret_model)
    db.commit()

    return {"secret_key": secret_model.secret_key, "message": secret_model.message}


def get_secret_message(secret_key: str, passphrase: str, db):
    secret = db.query(Secret).filter(Secret.secret_key == secret_key).first()

    if not secret:
        return None
    
    if secret.hashed_passphrase:
        if not passphrase:
            return None
        if not pbkdf2_sha256.verify(passphrase, secret.hashed_passphrase):
            return None

    return secret.message