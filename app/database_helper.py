def consumo_helper(consumo) -> dict:
    return {
        "cantidad": consumo["cantidad"],
        "fuente": consumo["fuente"],
        "consumo": consumo["consumo"],
        "unidad_medida": consumo["unidad_medida"],
        "factor_emision": consumo["factor_emision"],
        "factor_emision_valor": consumo["factor_emision_valor"],
        "observaciones": consumo["observaciones"],
        "usuario": consumo["usuario"],
    }
