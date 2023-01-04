from fastapi import APIRouter, FastAPI

import sys
sys.path.insert(0, '/home/hiraishin/Documents/layering-lab/service')

import bookapplication

app = FastAPI()

@app.get("/")
def homepage():
    return {"Layering": "SWA"}

app.include_router(bookapplication.app, prefix="/books", tags=["books"])