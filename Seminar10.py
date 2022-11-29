#контроллер

import user_interface as user
import model_sum as model
import model_div 
import model_mult
import model_sub

def button_click():
    print('1 = комплексное; 2 = float')
    value_item = int(input('выберите значение: '))
    print()
    if value_item == 1:
        value_a = user.input_complex()
        value_b = user.input_complex()
    if value_item == 2:
        value_a = user.input_data()
        value_b = user.input_data()
    ####
    print('1 = div; 2 = mult; 3 = sum; 4 = sub')
    print('выберите функцию: ')
    value_model = int(input('выберите значение: '))
    print()
    ####
    if value_model == 3: ###
        model.init(value_a, value_b)
        result = model.do_it()
        user.view_data(result)
    ###
    if value_model == 1:
        model_div.init(value_a, value_b)
        result = model_div.do_it() #
        user.view_data(result)
    ###
    if value_model == 2:
        model_mult.init(value_a, value_b)
        result = model_mult.do_it() #
        user.view_data(result)
    if value_model == 4:
        model_sub.init(value_a, value_b)
        result = model_sub.do_it() #
        user.view_data(result)


# 
        from datetime import datetime as dt
def log_to_file(arg1, arg2, operation, result):
    path = 'logging.csv'
    time_sign = dt.now().strftime('%D %H:%M')
    f = open(path, 'a')
    f.write(f'{time_sign}--> {arg1} {operation} {arg2} = {result}\n')
    f.close()

    import controller as c
c.button_click()


x = 0
y = 0

def init(a, b):
    global x
    global y
    x = a
    y = b

def do_it():
    return x // y

  def input_data():
    number = float(input('Введите рациональное число - '))
    return number

def input_complex():
    number = complex(input('Введите комплексное число - '))
    return number

def view_data(number):
    print(number)


