# Запуск программы

import controller 

controller.button()

# Контроллер

from sort import sort,get_da
from viev import get_number_operation,get_data
from write_read_file import read_file,write_file
from main import sort_data


def button():
    return sort_data(get_number_operation,read_file,write_file,sort,get_da,get_data)

# Сортировка

def get_da(n,f):
    li=[]
    for i in f:
        li.append(i.split()[n])
    return li


def sort(n,f):
    li=[]
    for i in f:
        if n in i:
            li.append(i)
    return li    

# Ввод-вывод

def write_file(data):
    with open('file.csv','a') as file:
        file.writelines(data)
          
def read_file():
    with open('file.csv','r') as file:
        return file.readlines()