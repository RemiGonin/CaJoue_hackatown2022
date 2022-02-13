from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from app.db import get_db, engine
import app.sql_app.models as models
import app.sql_app.schemas as schemas
from app.sql_app.repositories import PatinoireRepo
from sqlalchemy.orm import Session
import uvicorn
from typing import List, Optional
from fastapi.encoders import jsonable_encoder
import time

app = FastAPI(title="CaJoue",
              description="CaJoue FastAPI Application with Swagger and Sqlalchemy",
              version="0.0.1", )

models.Base.metadata.create_all(bind=engine)


@app.exception_handler(Exception)
def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail: {err}"})


@app.get('/patinoires', tags=["Patinoire"], response_model=List[schemas.Patinoire])
def get_all_patinoires(opt: Optional[models.FetchOption] = "all", db: Session = Depends(get_db)):
    if opt == models.FetchOption.all:
        return PatinoireRepo.fetch_all(db)
    elif opt == models.FetchOption.cajoue:
        return PatinoireRepo.fetch_all_playing(db)
    elif opt == models.FetchOption.ouverte:
        return PatinoireRepo.fetch_all_open(db)
    else:
        raise HTTPException(status_code=404, detail="Fetch option unknown")

@app.get('/patinoires/{patinoire_id}', tags=["Patinoire"], response_model=schemas.Patinoire)
def get_patinoire(patinoire_id: int, db: Session = Depends(get_db)):
    db_patinoire = PatinoireRepo.fetch_by_id(db, patinoire_id)
    if db_patinoire is None:
        raise HTTPException(status_code=404, detail="Patinoire not found with the given ID")
    return db_patinoire

@app.put('/patinoires/{patinoire_id}/cajoue', tags=["Patinoire"], response_model=schemas.Patinoire)
async def cajoue_patinoire(patinoire_id: int, duration: Optional[int] = 30, db: Session = Depends(get_db)):
    db_patinoire = PatinoireRepo.fetch_by_id(db, patinoire_id)
    if db_patinoire:
        db_patinoire.ouvert = True
        db_patinoire.jeu = time.time() + duration*60
        return await PatinoireRepo.update(db=db, patinoire_data=db_patinoire)
    else:
        raise HTTPException(status_code=400, detail="Patinoire not found with the given ID")

@app.put('/patinoires/{patinoire_id/cajoueplus', tags=["Patinoire"], response_model=schemas.Patinoire)
async def cajoue_plus_patinoire(patinoire_id: int, db: Session = Depends(get_db)):
    db_patinoire = PatinoireRepo.fetch_by_id(db, patinoire_id)
    if db_patinoire:
        db_patinoire.jeu = time.time() - 1
        return await PatinoireRepo.update(db=db, patinoire_data=db_patinoire)
    else:
        raise HTTPException(status_code=400, detail="Patinoire not found with the given ID")

@app.post('/patinoires', tags=["Patinoire"], response_model=schemas.Patinoire, status_code=201)
async def create_patinoire(patinoire_request: schemas.PatinoireCreate, db: Session = Depends(get_db)):
    """
    Create an Item and store it in the database
    """
    print(patinoire_request)
    db_item = PatinoireRepo.fetch_by_id(db, patinoire_request.id)
    if db_item:
        raise HTTPException(status_code=400, detail="Item already exists!")

    return await PatinoireRepo.create(db=db, patinoire=patinoire_request)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
