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
    if consumo.consumo == "GAS":
        consumo.emision = consumo.cantidad * 1.98
    if consumo.consumo == "ENERGIA":
        consumo.emision = consumo.cantidad * 0.166
    if consumo.consumo == "PAPEL_CARTA":
        consumo.emision = consumo.cantidad * 0.61
    if consumo.consumo == "PAPEL_OFICIO":
        consumo.emision = consumo.cantidad * 0.61
    if consumo.consumo == "GASOLINA":
        consumo.emision = consumo.cantidad * 1.98
    if consumo.consumo == "AGUA":
        consumo.emision = consumo.cantidad * 0.0835
    json_compatible_item_data = jsonable_encoder(consumo)
    await db_add_consumo(json_compatible_item_data)
    mensaje = str(consumo.emision) + " " + consumo.factor_emision
    return mensaje


@app.get("/calculo/contsumo/get-consumos/")
async def get_all_consumos():
    response = await db_get_consumos()
    return {"data": response}


# @app.get("/partners/getbankinf/{email}/", tags=["bank"])
# async def get_bank_inf(email: str):
#     admin = await partner_bank_inf.find_one({"email": email})
#     if admin:
#         return {"bank information": partners_bank_inf_helper(admin)}
#     else:
#         return {"INFO": "No se encuentra informacion acerca de este email"}


# # actualizar informacion del banco
# @app.put("/partners/updatebankinf/", tags=["bank"])
# async def update_bank_inf(bankInf: BankInformation):
#     admin = await partners_collection.find_one({"email": bankInf.email})
#     bankInf.nit = admin["nit"]
#     if admin:
#         partner_bank_inf.find_one_and_update(
#             {"email": admin["email"]}, {"$set": dict(bankInf)}
#         )
#     else:
#         {"INFO": "El Email no existe"}
#     return {"INFO": "Informacion del banco actualizada"}


# metodos para guardar la informacion legal del partner
# guardar informacion legal
# @app.post("/partners/legalinf/", tags=["legal"])
# async def post_legal_info(legalInf: LegalInformation):
#     await validate_legal_inf(legalInf.email)
#     admin = await partners_collection.find_one({"email": legalInf.email})
#     if admin:
#         legalInf.nit = admin["nit"]
#         json_compatible_item_data = jsonable_encoder(legalInf)
#         partner_response = await add_legal_inf(json_compatible_item_data)
#     else:
#         return {"INFO": "El Email no existe"}
#     return {"partner": partner_response}
