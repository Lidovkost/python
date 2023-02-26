def num_input(text):
    number = input(text)
    try:
        return int(number)
    except:
        print('вы ввели не число(( ')
        return num_input(text) 
number = num_input('Введите число, n = ')
def sum_arithmetic_progression(n):
    if  n == 1:
        return n
    return n + sum_arithmetic_progression(n - 1)
def gauss_formul_for_arithmetic_progress(n):
    return int(n * (n + 1) / 2)
number1 = sum_arithmetic_progression(number)
number2 = gauss_formul_for_arithmetic_progress(number)
if number1 == number2:
    print('для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.')
    
