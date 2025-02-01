import json
import propertySearch as ps
import random

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Angular app URL
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.get("/random")
def get_random_number():
    return {"random_number": random.randint(1, 100)}

@app.get("/getProperties")
def get_properties(location: str, limit: int, minPrice: int, maxPrice: int, listingType: str):
    return {"properties": ps.propSearch(location, limit, minPrice, maxPrice, listingType)}