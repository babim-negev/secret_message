from pydantic import BaseModel

from typing import Optional
from src.services.constants import TTL


class SecretGenerateInput(BaseModel):
    secret_message: str
    passphrase: Optional[str] = None
    ttl: TTL



