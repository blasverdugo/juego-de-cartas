
from typing import Optional, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .pila import Pila
    from .accion import Accion


class Carta(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    nombre: str

    disponible: bool = Field(default=True)

    costoenergia: int = Field(
        default=0,
        ge=0
    )

    ataque: int = Field(
        default=0,
        ge=0
    )

    defensa: int = Field(
        default=0,
        ge=0
    )

    # Una carta puede tener una acción asociada
    id_accion: Optional[int] = Field(
        default=None,
        foreign_key="accion.id"
    )

    accion: Optional["Accion"] = Relationship(
        back_populates="carta"
    )

    # Cada carta pertenece a una pila
    id_pila: int = Field(
        foreign_key="pila.id",
        index=True
    )

    pila: "Pila" = Relationship(
        back_populates="cartas"
    )
