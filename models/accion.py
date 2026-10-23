from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .carta import Carta


class Accion(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    nombre: str
    tipo: str

    carta: Optional["Carta"] = Relationship(
        back_populates="accion"
    )