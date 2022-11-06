from fastapi import FastAPI
from restaurant import controller as restaurant

app = FastAPI()

app.include_router(restaurant.router)
