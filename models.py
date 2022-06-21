from typing import Union, List
from pydantic import BaseModel

class Certamen(BaseModel):
    id: int
    nota: int

class Control(BaseModel):
    nota: int
    tiempo: Union[int, None] = None
    intento: int

class Tarea(BaseModel):
    nota: int

class EvaluacionFormativa(BaseModel):
    id: int
    nota: int
    tiempo: int
    intento: int

class UVA(BaseModel):
    id: int
    control: Control
    tarea: Tarea
    evaluacionesFormativas: List[EvaluacionFormativa] = []

class Performance(BaseModel):
    UVAS: List[UVA] = []
    certamanes: List[Certamen] = []

class StudentData(BaseModel):
    firstName: str
    lastName: str
    rol: str
    performance: Performance


class Request(BaseModel):
    student: str
    uva: int