from fastapi import FastAPI
from server.routes.socie import router as SocieRouter

app = FastAPI()

app.include_router(SocieRouter, tags=["Socie"], prefix="/socie")



@app.get("/", tags=['root'])
async def read_root():
    return {"message": "Bienvenidos a esta fantátrtertrstica aplicación"}
