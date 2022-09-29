import parsing
import parsecomplex
import os

def menu() :
    '''Меню программы, возвращает выбранный пкунт'''
    os.system('cls')
    print('1 Калькулятор рациональных чисел')
    print('2 Калькулятор комплексных чисел')
    print('3 Завершить работу')
    return int(input())

def ratiocalc() :
    '''Вызывает калькулятор рациональных чисел'''
    os.system('cls')
    while True :
        expr = input('Введите выражение (для завершения просто Enter) : ')
        if expr == '' :
            break
        if parsing.checkstring(expr) != -1 :
            print(parsing.calculate(expr))
        input('Для продолжения нажмите Enter')

def complexcalc() :
    '''Вызывает калькулятор рациональных чисел'''
    os.system('cls')
    while True :
        print('Комплексное число заключаем в [], у мнимой части на конце - i')
        expr = input('Введите выражение (для завершения просто Enter) : ')
        if expr == '' :
            break
        if parsecomplex.checkstring(expr) != -1 :
            print(parsecomplex.calculate(expr))
        input('Для продолжения нажмите Enter')

os.system('chcp 65001')
while True :
    key = menu()
    if key == 3 :
        break
    if key == 1 :
        ratiocalc()
    if key == 2 :
        complexcalc()
print('Работа завершена')