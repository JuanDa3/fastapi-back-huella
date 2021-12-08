from enum import Enum
from pydantic import BaseModel, Field, EmailStr
from datetime import date, datetime
from typing import List, Optional


class ResiduoEnum(str, Enum):
    peligrosos = "PELIGROSOS"
    solidos = "SOLIDOS"
    organicos = "ORGANICOS"
    aprovechados = "APROVECHADOS"


class ConsumoEnum(str, Enum):
    gas = "GAS"
    energia = "ENERGIA"
    agua = "AGUA"
    papel_carta = "PAPEL_CARTA"
    papel_oficio = "PAPEL_OFICIO"
    gasolina = "GASOLINA"


class Consumo(BaseModel):
    cantidad: float
    fuente: str
    consumo: ConsumoEnum
    unidad_medida: str
    factor_emision: str
    factor_emision_valor: float
    observaciones: str
    emision: Optional[float]
    usuario: str
    # periodo

    class Config:
        schema_extra = {
            "example": {
                "cantidad": 0.0,
                "fuente": "",
                "consumo": "GAS",
                "unidad_medida": "Lb/mes",
                "factor_emision": "kWtCO2eq",
                "factor_emision_valor": 1.98,
                "observaciones": "",
                "emision": 13.0,
                "usuario": "admin",
            }
        }


class Residuo(BaseModel):
    cantidad: int
    fuente: str
    residuo: ResiduoEnum
    unidad_medida: str
    factor_emision: float
    observaciones: str

    class Config:
        schema_extra = {
            "example": {
                "cantidad": 100,
                "fuente": "Activos Fijos",
                "consumo": "peligrosos",
                "unidad_medida": "Lb/mes",
                "factor_emision": 0.08,
                "observaciones": "tomada del año 2021",
            }
        }
