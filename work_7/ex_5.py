class TypeErorr(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else None
    def __str__(self):
        return f"Ошибка: {self.message}"

numbers_list = []

while True:
    i_num = input("Ввести число или stop для выхода: ")
    if i_num == 'stop':
        break
    try:
        if i_num.isnumeric() == False:
            raise TypeErorr
        i_num = int(i_num)
        numbers_list.append(i_num)
    except TypeErorr:
        print(TypeError(f"{i_num} - не число "))
print(numbers_list)

