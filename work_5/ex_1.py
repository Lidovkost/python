from operator import methodcaller 
import operator
operations = {
    '/':'truediv',
    '*': 'mul',
    '+': 'add',
    '-': 'sub',
    '0': 'exit'
    }
def calculate(sep, number1, number2):
    try:
        number = methodcaller(operations[sep], number1, number2)
        return number(operator)
    except:
        return 'Деление на ноль невозможно!'               
def sep_input():
    sep = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if sep in operations:
        return sep
    else:
        print('Вы ввели не операцию (((. Исправьтесь')
        return sep_input()
def num_input(text):
    number = input(text)
    try:
        return float(number)
    except:
        print('вы ввели не число(( ')
        return num_input(text)    
def calculating():
    sep = sep_input()
    if sep == '0':
        return
    number1 = num_input('введите первое число ')
    number2 = num_input('введите второе число ')
    print(f'{number1} {sep} {number2} = {calculate(sep, number1, number2)} ')
    calculating()
calculating()



