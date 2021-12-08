import motor.motor_asyncio
from bson import ObjectId
from decouple import config
import datetime
from datetime import date
from database_helper import *
from models import *

MONGO_DETAILS = config("MONGO_DETAILS")

client = motor.motor_asyncio.AsyncIOMotorClient(
    MONGO_DETAILS, serverSelectionTimeoutMS=10000
)
database = client.huella_carbono

consumos_collection = database.get_collection("consumos")


async def db_add_consumo(consumo: dict) -> dict:
    partners_entity = await consumos_collection.insert_one(consumo)
    new_consumo = await consumos_collection.find_one(
        {"_id": partners_entity.inserted_id}, {"_id": 0}
    )
    return {"data": new_consumo}


async def db_get_consumos() -> dict:
    consumos = []
    async for consumo in consumos_collection.find({}, {"_id": 0}):
        consumos.append(consumo_helper(consumo))
    return consumos
