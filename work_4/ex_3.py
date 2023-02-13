list2 = [1, 2, 3, 4, 3, 2, 7, 0, 2]
for n in list2:
    if list2.count(n) > 1:
        while list2.count(n) > 0:
            list2.remove(n)        
print(list2)

