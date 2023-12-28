from fastapi import APIRouter, Depends
from typing import Optional
from src.api.schemas import SecretGenerateInput
from src.services.secrets_logic import create_secret
from src.services.secrets_logic import get_secret_message
from src.db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(tags=['Create Read'])


@router.post('/generate')
def generate_secret(message: SecretGenerateInput, db: Session = Depends(get_db)):
    return create_secret(message, db)


@router.get('/secrets/{secret_key)')
def get_secret(secret_key: str, passphrase: Optional[str] = None, db: Session = Depends(get_db)):
    message = get_secret_message(secret_key, passphrase, db)

    if message is not None:
        return {"message": message}
    else:
        return {"error": "Invalid secret_key or passphrase"}
