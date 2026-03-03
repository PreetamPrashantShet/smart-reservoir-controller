from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Allow everything
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Smart Reservoir Controller",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Smart Reservoir Controller API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}