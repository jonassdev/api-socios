import os
import motor.motor_asyncio
from bson.objectid import ObjectId


client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["DB_URL"])

database = client.socies

socie_collection = database.get_collection("socies_collections")

# helpers

def socie_helper(socie) -> dict:
    return {
        "id": str(socie["_id"]),
        "nombre": socie["nombre"],
        "apellido": socie["apellido"],
        "dni": str(socie["dni"]),
        "nro_socie": str(socie["nro_socie"]),
        "email": socie["email"],
        "telefono": socie["telefono"],
        "codigo_postal": socie["codigo_postal"],
        "tipo_socio": socie["tipo_socio"]
    }
    
# Operaciones CRUD en la base de datos


# Buscar todes las socies de la base de datos
async def retrieve_socies():
    socies = []
    async for socie in socie_collection.find():
        socies.append(socie_helper(socie))
    return socies

# Agregar un socie a la base de datos

async def add_socie(socie_data: dict) -> dict:
    socie = await socie_collection.insert_one(socie_data)
    new_socie = await socie_collection.find_one({"_id": socie.inserted_id})
    return socie_helper(new_socie)

# Buscar un socie a partir de un ID
async def retrieve_socie(id: str) -> dict:
    socie = await socie_collection.find_one({"_id": ObjectId(id)})
    if socie:
        return socie_helper(socie)


# Actulizar un socie a partir de un ID
async def update_socie(id: str, data: dict):
    # Devuelve falso si el cuerpo del request está vacio
    if len(data) < 1:
        return False
    socie = await socie_collection.find_one({"_id": ObjectId(id)})
    if socie:
        updated_socie = await socie_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_socie:
            return True
        return False

# Borrar un socie de la base de datos
async def delete_socie(id: str):
    socie = await socie_collection.find_one({"_id": ObjectId(id)})
    if socie:
        await socie_collection.delete_one({"_id": ObjectId(id)})
        return True