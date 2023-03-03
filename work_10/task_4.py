"""
Задание 4.

Преобразовать слова "разработка", "администрирование", "protocol",
"standard" из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
texts = [
"разработка", "администрирование", "protocol","standard"
]
def String_to_bytes(val):
    return val.encode('utf-8')
def Bytes_to_str(val):
    return val.decode('utf-8')
for item in texts:
    a = String_to_bytes(item)
    print(a)
    print(Bytes_to_str(a))


