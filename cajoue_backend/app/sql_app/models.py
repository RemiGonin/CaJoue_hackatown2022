from sqlalchemy import Column, Integer, String, Float, Boolean

from app.db import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), nullable=False, unique=True, index=True)
    price = Column(Float(precision=2), nullable=False)
    description = Column(String(200))

    def __repr__(self):
        return 'ItemModel(name=%s, price=%s,store_id=%s)' % (self.name, self.price, self.store_id)

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
    jeu = Column(Boolean, nullable=False)

    def __repr__(self):
        return 'Patinoire(name=%s)' % (self.nom)