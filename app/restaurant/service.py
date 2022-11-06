from distutils.command.upload import upload
from hashlib import new
import gspread
import random


def get_all_restaurants():
    gc = gspread.service_account(filename='credentials.json')
    sheet = gc.open_by_key("1505B7TfqY2ITcBxCNinbnia_MYhXwBFyXyrPY94mnyk")
    return sheet.sheet1.get_all_records()


def add_new_restaurant(name, star):
    gc = gspread.service_account(filename='credentials.json')
    page_1 = gc.open_by_key("1505B7TfqY2ITcBxCNinbnia_MYhXwBFyXyrPY94mnyk").worksheet(
        "Liste de restaurants")

    restaurant_cell = page_1.find(name)

    if restaurant_cell:
        page_1.update_cell(restaurant_cell.row, restaurant_cell.col + 1, star)
    else:
        new_idx = len(page_1.get_all_records()) + 2
        new_cell_A = "A" + str(new_idx)
        new_cell_B = "B" + str(new_idx)
        page_1.update(new_cell_A, name)
        page_1.update(new_cell_B, star)


def delete_restaurant(name):
    gc = gspread.service_account(filename='credentials.json')
    page_1 = gc.open_by_key("1505B7TfqY2ITcBxCNinbnia_MYhXwBFyXyrPY94mnyk").worksheet(
        "Liste de restaurants")

    cell = page_1.find(name)
    return page_1.delete_row(cell.row) if cell else "ok"


def select_rand_restaurant():
    gc = gspread.service_account(filename='credentials.json')
    page_1 = gc.open_by_key("1505B7TfqY2ITcBxCNinbnia_MYhXwBFyXyrPY94mnyk").worksheet(
        "Liste de restaurants")
    page_2 = gc.open_by_key(
        "1505B7TfqY2ITcBxCNinbnia_MYhXwBFyXyrPY94mnyk").worksheet("Historique")

    nb_restaurant = len(page_1.get_all_records())
    random_restaurant_nb = random.randint(1, nb_restaurant) + 1
    random_restaurant_name = page_1.acell("a"+str(random_restaurant_nb)).value

    nb_historical = len(page_2.get_all_records()) + 1
    last_historical_restaurant_name = page_2.acell(
        "a" + str(nb_historical)).value
    if random_restaurant_name == last_historical_restaurant_name:
        return select_rand_restaurant()
    else:
        page_2.update("A" + str(nb_historical + 1), random_restaurant_name)
        return {"name": random_restaurant_name}


def add_restaurant_me(name):
    gc = gspread.service_account(filename='credentials.json')
    python_page2 = gc.open_by_key(
        "1505B7TfqY2ITcBxCNinbnia_MYhXwBFyXyrPY94mnyk").worksheet("Historique")
    count_resto = len(python_page2.get_all_records())
    new_idx = count_resto + 2
    cell = "a" + str(new_idx)
    return python_page2.update(cell, name)
