from fastapi import APIRouter
from src.api.schemas import SecretGenerateInput
from src.services.secrets_logic import create_secret
import hashlib

router = APIRouter(tags=['Create Read'])


@router.post(
    '/generate'
)
async def generate_secret(message: SecretGenerateInput):
    result = create_secret(message)
    return result