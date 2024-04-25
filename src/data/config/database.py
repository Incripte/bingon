from pymongo import MongoClient


client = MongoClient(
    "mongodb+srv://arthur_silva:SiXEK5SCsNLhhPc2QcSAdxZJ4cXuckrN@arthursilva"
    ".p0wb4ss.mongodb.net/?retryWrites=true&w=majority&appName=ArthurSilva"
    )  # type: ignore


db = client.player.db


collection_name = db["player_collection"]
