import random
number = random.randint(0,100)
def comparison(a, b, text_true, text_false):
    if a > b:
       print(text_true)
    else:
        print(text_false)
def input_number(text):
    try:
        return int(input(text))
    except:
        print('вы ввели не число')
        return input_number(text)   
def guess_number(number, attemtps = 10):
    if attemtps == 0:
        print(f'вы проиграли, загаданное число -> {number}')
        return
    answer = input_number(f'У вас осталось {attemtps} попыток, попробуйте отгадать число-> ')
    if answer == number:
        print(f'Вы отгадали число {number}! ')
        return
    comparison(number, answer, f'Введенное вами {answer} меньше загаданного', f'Введеное вами {answer} больше загаданного')
    guess_number(number, attemtps-1)
guess_number(number)
