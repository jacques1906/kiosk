from hashlib import new
import gspread
import random

def get_all_restaurants():
    gc = gspread.service_account(filename='credentials.json')
    sheet = gc.open_by_key("1505B7TfqY2ITcBxCNinbnia_MYhXwBFyXyrPY94mnyk")
    return sheet.sheet1.get_all_records()

def select_rand_restaurant():
    gc = gspread.service_account(filename='credentials.json')
    page_1 = gc.open_by_key("1505B7TfqY2ITcBxCNinbnia_MYhXwBFyXyrPY94mnyk").worksheet("Liste de restaurants")
    count_resto = len(page_1.get_all_records())
    cell_num= random.randint(1,count_resto)+1
    cell_line = "a"+str(cell_num)
    page_2 = gc.open_by_key("1505B7TfqY2ITcBxCNinbnia_MYhXwBFyXyrPY94mnyk").worksheet("Historique")
    count_resto2= len(page_2.get_all_records())
    count_resto2 = count_resto2 + 1
    count_resto3 = count_resto2 + 1
    cellb = "a" + str(count_resto2)
    select = page_1.acell(cell_line)
    print(select,cell_line)
    if page_1.acell(cell_line) == page_2.acell(cellb):
        return select_rand_restaurant()
    else : 
        autre = "a" + str(count_resto3)
        page_2.update(autre,page_1.acell(cell_line).value)
        return select 

def add_restaurant_me(name):
    gc = gspread.service_account(filename='credentials.json')
    python_page2 = gc.open_by_key("1505B7TfqY2ITcBxCNinbnia_MYhXwBFyXyrPY94mnyk").worksheet("Historique")
    count_resto = len(python_page2.get_all_records())
    new_idx = count_resto + 2
    cell = "a" + str(new_idx)
    return python_page2.update(cell,name)

def add_new_restaurant(names,stars): 
    gc = gspread.service_account(filename='credentials.json')
    page_1 = gc.open_by_key("1505B7TfqY2ITcBxCNinbnia_MYhXwBFyXyrPY94mnyk").worksheet("Liste de restaurants")
    if page_1.find(names) :
        cella = page_1.find(names)
        page_1.update_cell(cella.row,cella.col +1 ,stars)
    elif page_1.find(names) == None: 
        count_resto = len(page_1.get_all_records())
        new_idx = count_resto + 2
        cell = "a" + str(new_idx)
        celly = "b" + str(new_idx)
        return page_1.update(cell,names),page_1.update(celly,stars)

def delete_restaurant(delete_names):
    gc = gspread.service_account(filename='credentials.json')
    page_1 = gc.open_by_key("1505B7TfqY2ITcBxCNinbnia_MYhXwBFyXyrPY94mnyk").worksheet("Liste de restaurants")
    page_1.find(delete_names) 
    cell = page_1.find(delete_names)
    return  page_1.delete_row(cell.row)
    

