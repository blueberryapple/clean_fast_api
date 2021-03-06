"""
Entrypoint to application
"""
from fastapi import FastAPI
from modules.flower.controller import router as flower_router

app = FastAPI()
app.include_router(flower_router)
