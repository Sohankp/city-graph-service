from fastapi import APIRouter 
from app.api.v1.controllers import ping, add_episode, retrieve_episode
from app.api.v1.models import PingPayload,EpisodePayload, RetrieveEpisodePayload


router = APIRouter()    

@router.post("/ping")
async def post_ping(payload: PingPayload):
    return await ping(payload)

@router.post("/add/episode")
async def add_episode_graph(payload: EpisodePayload):
    return await add_episode(payload)

@router.get("/get/graph")
async def get_episode_graph(payload: RetrieveEpisodePayload):
    return await retrieve_episode(payload)
