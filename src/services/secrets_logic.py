import hashlib
from src.api.schemas import SecretGenerateInput


def create_secret(message):
    secret_message = message.secret_message
    hash_value = hashlib.sha256(secret_message.encode()).hexdigest()
    return hash_value, f'{hash_value}'
