import math
from fastapi import FastAPI
import propertySearch as ps
import random

app = FastAPI()

@app.get("/random")
def get_random_number():
    return {"random_number": random.randint(1, 100)}

@app.get("/getProperties")
def get_properties(location: str):
    return {"properties": ps.propSearch(location)}

