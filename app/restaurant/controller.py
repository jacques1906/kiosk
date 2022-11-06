from importlib.resources import Resource
from typing import Union
from fastapi import APIRouter
from pydantic import BaseModel
from .service import get_all_restaurants, select_rand_restaurant, add_new_restaurant, delete_restaurant

router = APIRouter()


class Restaurant(BaseModel):
    name: str
    star: int | None = None


@router.get("/restaurants")
def read_root():
    return get_all_restaurants()


@router.post("/restaurants")
def post_data(restaurant: Restaurant):
    add_new_restaurant(restaurant.name, restaurant.star)
    return {"ok"}


@router.delete("/restaurants")
def post_data(restaurant: Restaurant):
    delete_restaurant(restaurant.name)
    return {"ok"}


@router.get("/me/restaurants/random")
def read_root():
    return select_rand_restaurant()
