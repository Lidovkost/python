def input_number():
    try:
        return int(input('введите число '))
    except:
        print('вы ввели не число')
        return input_number()
def check_parity(number):
    return number % 2 == 0
def count_even_uneven(number, count_even = 0, count_uneven = 0):
    result = check_parity(number)  
    if result:
        count_even += 1
    else:
        count_uneven += 1
    number = number // 10
    if number == 0:
        print(f'Количество четных и нечетных цифр в числе равно: ({count_even}, {count_uneven})')
        return
    count_even_uneven(number, count_even, count_uneven)
number = input_number()
count_even_uneven(number)

    
    