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
    nom: Optional[str] = ""
    genre: Optional[str] = ""
    description: Optional[str] = ""
    adresse: Optional[str] = ""
    lat: float
    lng: float
    ouvert: Optional[bool] = None
    jeu: bool = False

class PatinoireCreate(PatinoireBase):
    pass

class Patinoire(PatinoireBase):
    id: int

    class Config:
        orm_mode = True