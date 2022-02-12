from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from sql_app import models
from db import get_db, engine
import sql_app.models as models
import sql_app.schemas as schemas
from sql_app.repositories import ItemRepo
from sql_app.repositories import PatinoireRepo
from sqlalchemy.orm import Session
import uvicorn
from typing import List, Optional
from fastapi.encoders import jsonable_encoder

app = FastAPI(title="CaJoue",
              description="CaJoue FastAPI Application with Swagger and Sqlalchemy",
              version="0.0.1", )

models.Base.metadata.create_all(bind=engine)


@app.exception_handler(Exception)
def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail: {err}"})


@app.get('/patinoires', tags=["Patinoire"], response_model=List[schemas.Patinoire])
def get_all_patinoires(db: Session = Depends(get_db)):
    return PatinoireRepo.fetch_all(db)


@app.get('/patinoires/{patinoire_id}', tags=["Patinoire"], response_model=schemas.Patinoire)
def get_patinoire(patinoire_id: int, db: Session = Depends(get_db)):
    db_patinoire = PatinoireRepo.fetch_by_id(db, patinoire_id)
    if db_patinoire is None:
        raise HTTPException(status_code=404, detail="Patinoire not found with the given ID")
    return db_patinoire

@app.put('/patinoires/{patinoire_id}/cajoue', tags=["Patinoire"], response_model=schemas.Patinoire)
async def cajoue_patinoire(patinoire_id: int, time: Optional[int] = 30, db: Session = Depends(get_db)):
    db_patinoire = PatinoireRepo.fetch_by_id(db, patinoire_id)
    if db_patinoire:
        db_patinoire.jeu = True
        # TODO : structure de donnée des patinoires où cajoue
        return await PatinoireRepo.update(db=db, patinoire_data=db_patinoire)
    else:
        raise HTTPException(status_code=400, detail="Patinoire not found with the given ID")

@app.put('/patinoires/{patinoire_id/cajoueplus', tags=["Patinoire"], response_model=schemas.Patinoire)
async def cajoue_plus_patinoire(patinoire_id: int, db: Session = Depends(get_db)):
    db_patinoire = PatinoireRepo.fetch_by_id(db, patinoire_id)
    if db_patinoire:
        db_patinoire.jeu = False
        # TODO : retirer la patinoire de la strucuture de donnée où cajoue
        return await PatinoireRepo.update(db=db, patinoire_data=db_patinoire)
    else:
        raise HTTPException(status_code=400, detail="Patinoire not found with the given ID")

@app.post('/items', tags=["Item"], response_model=schemas.Item, status_code=201)
async def create_item(item_request: schemas.ItemCreate, db: Session = Depends(get_db)):
    """
    Create an Item and store it in the database
    """

    db_item = ItemRepo.fetch_by_name(db, name=item_request.name)
    if db_item:
        raise HTTPException(status_code=400, detail="Item already exists!")

    return await ItemRepo.create(db=db, item=item_request)

@app.get('/items', tags=["Item"], response_model=List[schemas.Item])
def get_all_items(name: Optional[str] = None, db: Session = Depends(get_db)):
    """
    Get all the Items stored in database
    """
    if name:
        items = []
        db_item = ItemRepo.fetch_by_name(db, name)
        items.append(db_item)
        return items
    else:
        return ItemRepo.fetch_all(db)


@app.get('/items/{item_id}', tags=["Item"], response_model=schemas.Item)
def get_item(item_id: int, db: Session = Depends(get_db)):
    """
    Get the Item with the given ID provided by User stored in database
    """
    db_item = ItemRepo.fetch_by_id(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found with the given ID")
    return db_item


@app.delete('/items/{item_id}', tags=["Item"])
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    """
    Delete the Item with the given ID provided by User stored in database
    """
    db_item = ItemRepo.fetch_by_id(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found with the given ID")
    await ItemRepo.delete(db, item_id)
    return "Item deleted successfully!"


@app.put('/items/{item_id}', tags=["Item"], response_model=schemas.Item)
async def update_item(item_id: int, item_request: schemas.Item, db: Session = Depends(get_db)):
    """
    Update an Item stored in the database
    """
    db_item = ItemRepo.fetch_by_id(db, item_id)
    if db_item:
        update_item_encoded = jsonable_encoder(item_request)
        db_item.name = update_item_encoded['name']
        db_item.price = update_item_encoded['price']
        db_item.description = update_item_encoded['description']
        db_item.store_id = update_item_encoded['store_id']
        return await ItemRepo.update(db=db, item_data=db_item)
    else:
        raise HTTPException(status_code=400, detail="Item not found with the given ID")


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)