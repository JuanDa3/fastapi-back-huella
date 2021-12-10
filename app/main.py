import string
import random
from bson.objectid import ObjectId
from fastapi import (
    Depends,
    FastAPI,
    HTTPException,
    params,
    status,
    Body,
    Request,
    Response,
)
from fastapi import responses
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import JSONResponse
from pydantic.types import Json
from conn_db_mongo import *
from models import *
import aiohttp
from auth.auth_handler import create_access_token, decodeJWT
from datetime import datetime, timedelta, date
from passlib.context import CryptContext
from database_helper import *
from fastapi.middleware.cors import CORSMiddleware

# Environment vars
from decouple import config

# send mails


ACCESS_TOKEN_EXPIRE_MINUTES = config("token_expire_minutes")
ACCESS_TOKEN_EXPIRE_HOURS = config("token_expire_hours")
# patch(fastapi=True)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/calculo/consumo/", tags=["consumo"])
async def calculo_consumo(consumo: Consumo):
    cantidad = consumo.cantidad
    consumo.emision = cantidad * consumo.factor_emision_valor
    json_compatible_item_data = jsonable_encoder(consumo)
    await db_add_consumo(json_compatible_item_data)
    mensaje = str(consumo.emision) + " " + consumo.factor_emision
    return mensaje


@app.get("/calculo/consumo/get-consumos/")
async def get_all_consumos():
    response = await db_get_consumos()
    return {"data": response}
