from fastapi import APIRouter
from src.models.entities.players import Player
from src.data.config.database import collection_name
from src.data.schemas.schemas import list_serial
from bson import ObjectId


router = APIRouter()


# GET Request Method
@router.get("/")
async def get_players():
    players = list_serial(collection_name.find())
    return players


# POST Request Method
@router.post("/")
async def post_player(player: Player):
    collection_name.insert_one(dict(player))


# PUT Request Method
@router.put("/{id}")
async def put_player(id: str, player: Player):
    collection_name.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(player)}
        )


# DELETE Request Method
@router.delete("/{id}")
async def delete_player(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
