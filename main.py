from importlib.resources import Resource
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from spreadsheet import get_all_restaurants,select_rand_restaurant,add_restaurant_me,add_new_restaurant,delete_restaurant

app = FastAPI()

@app.get("/restaurants")
def read_root():
    return get_all_restaurants()


class Restaurant(BaseModel):
    name: str
    star: int | None = None

class add_Restaurant(BaseModel):
    names: str
    stars: int | None = None

class delete_Restaurant(BaseModel):
    delete_names: str

@app.get("/me/restaurant/rands")
def read_root():
    return select_rand_restaurant()

@app.put("/me/restaurant/ajouter")
def post_data(add_restaurant: add_Restaurant):
    add_new_restaurant(add_restaurant.names,add_restaurant.stars)
    return {"name": add_restaurant.names, "star": add_restaurant.stars}



@app.delete("/me/restaurant/delete")
def post_data(supprimer: delete_Restaurant):
    delete_restaurant(supprimer.delete_names)
    return {"delete_names": supprimer.delete_names},


