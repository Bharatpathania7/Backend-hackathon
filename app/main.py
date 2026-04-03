from fastapi import FastAPI
from app.routes.detect import router as detect_router

app = FastAPI(title="SLM Backend")

app.include_router(detect_router)


@app.get("/")
def home():
    return {"message": "FastAPI running successfully 🚀"}