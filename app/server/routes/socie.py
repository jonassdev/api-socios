from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_socie,
    delete_socie,
    retrieve_socie,
    retrieve_socies,
    update_socie,
)
from server.models.socie import (
    ErrorResponseModel,
    ResponseModel,
    SchemaDeSocie
)

router = APIRouter()

# CRUD

# CREATE
@router.post("/", response_description="Datos de socie agregados ala base de datos")
async def add_socie_data(socie: SchemaDeSocie = Body(...)):
    socie = jsonable_encoder(socie)
    new_socie = await add_socie(socie)
    return ResponseModel(new_socie, "Socie agregado.")