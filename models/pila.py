
from typing import Optional, List, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .jugador import Jugador
    from .carta import Carta


class Pila(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    # Cada pila pertenece a un jugador
    id_jugador: int = Field(
        foreign_key="jugador.id",
        unique=True,
        index=True
    )

    jugador: Optional["Jugador"] = Relationship(
        back_populates="pila"
    )

    # Una pila puede contener varias cartas
    cartas: List["Carta"] = Relationship(
        back_populates="pila"
    )
