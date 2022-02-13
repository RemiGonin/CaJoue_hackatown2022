from sqlalchemy.orm import Session

from . import models, schemas


class ItemRepo:

    async def create(db: Session, item: schemas.ItemCreate):
        db_item = models.Item(name=item.name, price=item.price, description=item.description)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def fetch_by_id(db: Session, _id):
        return db.query(models.Item).filter(models.Item.id == _id).first()

    def fetch_by_name(db: Session, name):
        return db.query(models.Item).filter(models.Item.name == name).first()

    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Item).offset(skip).limit(limit).all()

    async def delete(db: Session, item_id):
        db_item = db.query(models.Item).filter_by(id=item_id).first()
        db.delete(db_item)
        db.commit()

    async def update(db: Session, item_data):
        updated_item = db.merge(item_data)
        db.commit()
        return updated_item

class PatinoireRepo:

    async def create(db: Session, patinoire: schemas.PatinoireCreate):
        db_patinoire = models.Patinoire(id=patinoire.id, nom=patinoire.nom, genre=patinoire.genre, description=patinoire.description, adresse=patinoire.adresse, lat=patinoire.lat, lng=patinoire.lng, ouvert=patinoire.ouvert, jeu=patinoire.jeu)
        db.add(db_patinoire)
        db.commit()
        db.refresh(db_patinoire)
        return db_patinoire

    def fetch_by_id(db: Session, _id):
        return db.query(models.Patinoire).filter(models.Patinoire.id == _id).first()

    def fetch_by_name(db: Session, nom):
        return db.query(models.Patinoire).filter(models.Patinoire.nom == nom).first()

    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Patinoire).offset(skip).all()

    async def delete(db: Session, patinoire_id):
        db_patinoire = db.query(models.Patinoire).filter_by(id=patinoire_id).first()
        db.delete(db_patinoire)
        db.commit()

    async def update(db: Session, patinoire_data):
        updated_patinoire = db.merge(patinoire_data)
        db.commit()
        return updated_patinoire
