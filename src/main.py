
import uvicorn
from fastapi import FastAPI
from api.routes import router as secret_router
from src.db.database import Base, engine

app = FastAPI()

app.include_router(secret_router)

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    uvicorn.run("main:app", host='0.0.0.0', port=8080, reload=True)
