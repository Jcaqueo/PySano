from API import *
from BD.BD import *

from models import *
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.put("/incorrect")
async def incorrect(student: str = "", uva: str = ""):
    decreaseScore(student, uva)
    return {"message": "Success"}

@app.put("/correct")
async def correct(student: str = "", uva: str = ""):
    increaseScore(student, uva)
    return {"message": "Success"}


@app.get("/")
async def main(student: str = "", uva: str = ""):
    print(student)
    print(uva)
    return identifyStudent(student, uva)