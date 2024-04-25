from pymongo import MongoClient
from pymongo.server_api import ServerApi


uri = 'mongodb+srv://arthur_silva:SiXEK5SCsNLhhPc2QcSAdxZJ4cXuckrN'\
    '@arthursilva.p0wb4ss.mongodb.net/'\
    '?retryWrites=true&w=majority&appName=ArthurSilva'
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))  # type: ignore
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
