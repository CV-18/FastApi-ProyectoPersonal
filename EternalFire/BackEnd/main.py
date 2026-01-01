from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()
async def root():
    return {"message": "Welcome to the Eternal Fire API"}

