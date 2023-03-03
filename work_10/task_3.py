"""
Задание 3.

Определить, какие из слов "attribute", "класс", "функция", "type"
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
# """

#
# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

texts = ["attribute", "класс", "функция", "type"] 
for text in texts:
    try:
        if text.isascii():
            continue
        raise SyntaxError(text)
    except SyntaxError:
        print(f"{text} - error, bytes can only contain ASCII literal characters.")


