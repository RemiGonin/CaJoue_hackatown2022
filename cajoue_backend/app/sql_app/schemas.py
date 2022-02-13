from typing import List, Optional
from pydantic import BaseModel


class PatinoireBase(BaseModel):
    id: int
    nom: Optional[str] = ""
    genre: Optional[str] = ""
    description: Optional[str] = ""
    adresse: Optional[str] = ""
    lat: float
    lng: float
    ouvert: Optional[bool] = None
    jeu: int = 0


class PatinoireCreate(PatinoireBase):
    pass

class Patinoire(PatinoireBase):
    id: int

    class Config:
        orm_mode = True