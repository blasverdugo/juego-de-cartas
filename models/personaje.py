
from typing import Optional, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship, List

if TYPE_CHECKING:
    from .accion import Accion


class Personaje(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    nombre: str

    acciones: List ["Accion"] = Relationship(
        back_populates="personaje"
    )