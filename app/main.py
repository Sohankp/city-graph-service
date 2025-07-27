from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.core.config.app_config import app_config
from app.core.config.router_config import plugin_routers

app = FastAPI(
    title="City Graph API",
    docs_url="/docs"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

plugin_routers(app)

@app.get("/")
async def root():
    return {"message": "Welcome to the City Graph API"} 