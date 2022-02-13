from sqlalchemy.orm import Session
import time
from . import models, schemas

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

    def fetch_all_playing(db: Session):
        return db.query(models.Patinoire).filter(models.Patinoire.jeu > time.time()).all()

    def fetch_all_open(db: Session):
        return db.query(models.Patinoire).filter(models.Patinoire.ouvert).all()

    async def delete(db: Session, patinoire_id):
        db_patinoire = db.query(models.Patinoire).filter_by(id=patinoire_id).first()
        db.delete(db_patinoire)
        db.commit()

    async def update(db: Session, patinoire_data):
        updated_patinoire = db.merge(patinoire_data)
        db.commit()
        return updated_patinoire
