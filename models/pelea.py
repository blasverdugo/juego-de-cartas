
from typing import Optional, List, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .jugador import Jugador


class Pelea(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    turno_actual: int = Field(default=1, ge=1)

    informe: str = Field(default="")

    # Jugadores que participan en la pelea
    jugadores: List["Jugador"] = Relationship(
        back_populates="pelea"
    )
