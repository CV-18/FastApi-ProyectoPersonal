from pydantic import BaseModel
from typing import Optional, List

class Genero(BaseModel):
    id: int | None = None
    nombre: str
    historia: str
    filosofia: str
    artistas_destacados: List[str] 
    subgeneros: Optional[List[str]] = []