from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    price : float
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

class PatinoireBase(BaseModel):
    id: int
    nom: str
    genre: str
    description: str
    adresse: str
    lat: float
    lng: float
    ouvert: bool
    jeu: bool

class PatinoireCreate(PatinoireBase):
    pass

class Patinoire(PatinoireBase):
    id: int

    class Config:
        orm_mode = True