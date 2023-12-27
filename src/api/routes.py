from fastapi import APIRouter
from src.api.schemas import SecretGenerateInput

router = APIRouter()

@router.post(
    '/generate'
)
async def generate_secret(message: SecretGenerateInput):

    return message


