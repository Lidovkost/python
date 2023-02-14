def reverse_number(int_number): 
    if len(str(int_number)) == 1:
        return int_number 
    return str(int_number % 10) + str(reverse_number(int_number // 10))
def input_number():
    try:
        return int(input('введите число '))
    except:
        print('вы ввели не число')
        return input_number()
a = input_number()
print(reverse_number(a))