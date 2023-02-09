a = float(input('введите а '))
b = float(input('введите b '))
k = 1
while a < b:
    a = a * 1.1
    k += 1
text = f'Ответ: на {k}-й день спортсмен достиг результата — не менее {int(b)} км.'
print(text)


