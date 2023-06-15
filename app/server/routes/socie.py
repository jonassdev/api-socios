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
@router.post("/", response_description="Datos de socie agregados a la base de datos")
async def add_socie_data(socie: SchemaDeSocie = Body(...)):
    socie = jsonable_encoder(socie)
    new_socie = await add_socie(socie)
    return ResponseModel(new_socie, "Socie agregado.")

# READ
@router.get("/", response_description="Socies retrieved")
async def get_socies():
    socies = await retrieve_socies()
    if socies:
        return ResponseModel(socies, "Se consiguieron los datos de les Socies")
    return ResponseModel(socies, "Vuelvión una lista vacía")


@router.get("/{id}", response_description="Dato se socie recuperado")
async def get_socie_data(id):
    socie = await retrieve_socie(id)
    if socie:
        return ResponseModel(socie, "Se consiguieron los datos del Socie")
    return ErrorResponseModel("Ocurrió un error", 404, "El socie no existe.")

