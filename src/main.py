from fastapi import FastAPI
import uvicorn

from api.routes import router as secret_router

app = FastAPI()

app.include_router(secret_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8080, reload=True)
