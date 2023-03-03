list = input('Введите целые числа через пробел ').split()
text = 'result: '
index_1 = 0
index_2 = 1
while index_1 < len(list)-1:
    list[index_1], list[index_2] = list[index_2], list[index_1]
    index_1 += 2
    index_2 += 2
print(text, list)