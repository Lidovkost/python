words = input('Введите слова через пробел: ').split()
i = 1
for element in words:
    print(f'{i}. {element[0:10]}')
    i += 1
