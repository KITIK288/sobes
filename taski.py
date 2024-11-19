# Напишите программу, которая проверяет, является ли число числом Армстронга.
# Число Армстронга — натуральное число, которое в данной системе счисления равно сумме своих цифр, возведённых в степень, равную количеству его цифр.
# Пример: 3**3 + 7**3 + 1**3 = 371

import math

def task1(num):
    summa = 0
    s = 0
    print("Наше число -", num)
    for i in num:
        s += 1
    for i in num:
        i = int(i)
        i = i**s
        summa += i
    num = int(num)
    if summa == num:
        print("Число", num , "является числом армстронга")
    else:
        print("Число", num , "не является числом армстронга")

# task1("371")

# Напишите программу, которая посчитает факториал от заданного числа (через рекурсию).

def task2(num):
    fack = 1
    spisok = []
    counter = 1
    while counter <= num:
        spisok.append(counter)
        counter += 1
    print(spisok)
    for i in spisok:
        fack = fack * i
    print("Факториал числа", num, "-", fack)

# task2(4)

# Напишите программу, которая проверит, является ли число палиндромом.

def task3(num):
    num_lower = num.lower()
    print(num_lower == num_lower[::-1])

# task3("7889")

# Напишите программу, которая определит наибольшее из трех целых чисел

def task4():
    a = int(input())
    b = int(input())
    c = int(input())
    maxim = 0
    if a < b:
        maxim = b
    else:
        maxim = a
    if b < c:
        maxim = c
    else:
        maxim = b

    print("Максимальное число -", maxim)

# task4()

# Напишите программу, которая проверит, что число является совершенным.
# Совершенное число - натуральное число, равное сумме всех своих собственных делителей.
# Например, число 6 равно сумме своих собственных делителей 1 + 2 + 3.
# Примеры совершенных чисел: 6, 28, 496, 8128

def task5(num):
    d = 1
    result = 0
    spisok = []
    while d < num:
        if num % d == 0:
            spisok.append(d)
            d += 1
        else:
            d += 1
    for i in spisok:
        result += i
    if result == num:
        print("Число совершенное")
    else:
        print("Число не совершенное")
# task5(8128)

# Напишите программу, которая найдет среднее арифметическое списка чисел

def task6(lis):
    result = 0
    counter = 0
    for i in lis:
        result += i
        counter += 1
    result = result / counter
    print("Среднее арифметическое -", result)

# task6([1, 5, 10, 35, 234, 1, 6, 8])

# Описание: Напишите функцию, которая принимает строку и возвращает её в обратном порядке.

def task7(str):
    str = str[::-1]
    print(str)

# task7("Абобус")

# Описание: Напишите функцию, которая вычисляет факториал числа.

def task8(n):
    if n == 0:
        return 1
    else:
        return n * task8(n-1)

# print(task8(3))

def task9(pal):
    if pal == pal[::-1]:
        print("Число является палиндромом")
    else:
        print("Число не является палиндромом")

task9("1001")


