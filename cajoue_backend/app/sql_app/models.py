from sqlalchemy import Column, Integer, String, Float, Boolean
from enum import Enum

from app.db import Base

class Patinoire(Base):
    __tablename__ = "patinoires"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(80), nullable=False, unique=True, index=True)
    genre = Column(String(5))
    description = Column(String(200))
    adresse = Column(String(100))
    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)
    ouvert = Column(Boolean)
    jeu = Column(Integer, nullable=False)

    def __repr__(self):
        return 'Patinoire(name=%s)' % (self.nom)

class FetchOption(Enum):
    all = "all"
    cajoue = "cajoue"
    ouverte = "ouverte"