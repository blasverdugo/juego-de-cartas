
from typing import Optional, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .pelea import Pelea
    from .pila import Pila


class Jugador(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    tipo: str = Field(default="jugador")

    vida: int = Field(default=100, ge=0, le=100)
    energia: int = Field(default=50, ge=0, le=50)

    # Relación con Pelea
    id_pelea: Optional[int] = Field(
        default=None,
        foreign_key="pelea.id"
    )
    pelea: Optional["Pelea"] = Relationship(
        back_populates="jugadores"
    )

    # Relación con Pila
    pila: Optional["Pila"] = Relationship(
        back_populates="jugador"
    )


class Maquina(Jugador):
    tipo: str = "maquina"

    

class Persona(Jugador):
    tipo: str = "persona"
    username: str = Field(unique=True, index=True)