first_element = int(input('введите первый элемент арефметической прогрессии '))
elements_count = int(input('введите количество элементов в прогресии, которое необходимо вывести '))
arithmetic_diff = int(input('введите разность(шаг прогресии) '))
def arithmetic_progression(first_element, elements_count, arithmetic_diff):
    arithmetic_progression_list = []
    for i in range(0, elements_count):
        n = first_element + i  * arithmetic_diff
        arithmetic_progression_list.append(n)
    print(*arithmetic_progression_list, sep = '\n')
arithmetic_progression(first_element, elements_count, arithmetic_diff)