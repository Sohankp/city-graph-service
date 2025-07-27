from pydantic import BaseModel, Field
from typing import Optional

class PingPayload(BaseModel):
    name: str = Field(..., description="The name of the user")

class EpisodePayload(BaseModel):
    name: str
    episode_body: str
    source_description: str
    group_id: Optional[str] = None

class RetrieveEpisodePayload(BaseModel):
    user_query:str
    group_id: Optional[list[str]] = None