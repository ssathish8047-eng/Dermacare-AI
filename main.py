from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

import models
from database import engine
from routes import analyze, history

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DermaCare AI API",
    description="Backend API for skin condition pre-screening",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs("uploads", exist_ok=True)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.include_router(analyze.router, prefix="/api", tags=["Analysis"])
app.include_router(history.router, prefix="/api", tags=["History"])

@app.get("/")
def read_root():
    return {"message": "Welcome to DermaCare AI API"}
