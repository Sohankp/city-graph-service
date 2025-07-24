from fastapi import APIRouter 
from app.api.v1.controllers import ping, add_episode
from app.api.v1.models import PingPayload,EpisodePayload


router = APIRouter()    

@router.post("/ping")
async def post_ping(payload: PingPayload):
    return await ping(payload)

@router.post("/add/episode")
async def add_episode_graph(payload: EpisodePayload):
    return await add_episode(payload)

