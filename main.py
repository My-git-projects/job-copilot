from fastapi import FastAPI
from app.api.routes.ats_routes import router

app = FastAPI(title="ATS AI System")

app.include_router(router)