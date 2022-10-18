# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

a = [2, 3, 5, 9, 3]
summ = 0
for i in range(1, len(a), 2):
summ += a[i]

print(f"{a} -> Cумма элементов на нечётных позициях: {summ}")

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

number = int(input('Введите размер списка '))
list = []
list2 = []

for i in range(number):
list.append(randint(0, 9))

for i in range(len(list)):
while i < len(list)/2 and number > len(list)/2:
number = number - 1
a = list[i] * list[number]
list2.append(a)
i += 1

print(list)
print(list2)

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.2, 1.3, 3.2, 6, 11.05]
min = 1
max = 0
for i in list:
if (i - int(i)) <= min:
min = i - int(i)
if (i - int(i)) >= max:
max = i - int(i)

print(max-min)

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

print(bin(100)) #Встроенная функция


a = int(input('Введите число: '))
b = ''
while a > 0:
b = str(a % 2) + b
a = a // 2
print(f'Двоичное число: {b}')


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def Fibonacci(n):
    if n in [1, 2]:                       
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def NegaFibonacci(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2

list = [0]
userNumber = int(input('Enter any number: '))
for e in range(1, userNumber + 1):
    list.append(Fibonacci(e))
    list.insert(0, NegaFibonacci(e))
print(list)