from app.api.v1.models import PingPayload, EpisodePayload, RetrieveEpisodePayload
from app.services.graph_service.graph_client import graphiti
import datetime
from app.services.graph_service.graph_schemas import entity_types, edge_types, edge_type_map

async def ping(payload: PingPayload):
    return {"message": f"Hi {payload.name}, welcome to the City Graph API!"}

async def add_episode(payload:EpisodePayload):

    if payload.group_id:
        await graphiti.add_episode(
            name=payload.name,
            episode_body=payload.episode_body,
            source_description=payload.source_description,
            entity_types=entity_types,
            edge_types=edge_types,
            reference_time=datetime.datetime.now(),
            edge_type_map=edge_type_map,
            group_id=payload.group_id
        )
    else:
        await graphiti.add_episode(
            name=payload.name,
            episode_body=payload.episode_body,
            source_description=payload.source_description,
            entity_types=entity_types,
            edge_types=edge_types,
            reference_time=datetime.datetime.now(),
            edge_type_map=edge_type_map
        )

async def retrieve_episode(payload: RetrieveEpisodePayload):
    try:
        if payload.group_id:
            return await graphiti.search(query=payload.user_query, group_ids=payload.group_id)
        else:
            return await graphiti.search(query=payload.user_query)
    except Exception as e:
        return {"error": str(e)}
