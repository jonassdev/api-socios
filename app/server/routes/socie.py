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
    SchemaDeSocie,
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
    return ResponseModel(socies, "Devuelvo una lista vacía")


@router.get("/{id}", response_description="Dato se socie recuperado")
async def get_socie_data(id):
    socie = await retrieve_socie(id)
    if socie:
        return ResponseModel(socie, "Se consiguieron los datos del Socie")
    return ErrorResponseModel("Ocurrió un error", 404, "El socie no existe.")

# UPDATE
@router.put("/{id}")
async def update_socie_data(id: str, req: SchemaDeSocie.as_optional() = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_socie = await update_socie(id, req)
    if updated_socie:
        return ResponseModel(
            "Se pudo actualizar el Socie con el ID: {} ".format(id),
            "Socio Actualizado correctamente",
        )
    return ErrorResponseModel(
        "Ocurrió un error",
        404,
        "Hubo una falla actualizando los datos del Socie",
    )
    
# DELETE
@router.delete("/{id}", response_description="Socie data deleted from the database")
async def delete_socie_data(id: str):
    deleted_socie = await delete_socie(id)
    if deleted_socie:
        return ResponseModel(
            "Socie ID: {} borrado".format(id), "Socio Borrado exitosamente"
        )
    return ErrorResponseModel(
        "Hubo un error", 404, "Socio con id {0} no existe".format(id)
    )