def create_diapason_list(min, max):
    list = []
    for i in range(min, max+1):
        list.append(len(list))
    return list
a = create_diapason_list(-2000, 2000)
print(*a)