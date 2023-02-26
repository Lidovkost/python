import csv
file_1 = "info_1.txt" 
file_2 = "info_2.txt"
file_3 = "info_3.txt"
csv_file = "file.csv"
files_list = [
    file_1, file_2, file_3
]
texts_list = [
    "Изготовитель системы", "Название ОС", "Код продукта", "Тип системы", "Дата установки"
]
def get_info(file, text):
    import re
    new_file = open(file, "r")
    content = new_file.readlines()
    for element in content:
        if text in element:
            element = ' '.join(element.split()).replace(f"{text}: ", '')
            new_file.close
            return(element)
def get_data(files_list, texts_list):
    main_data = []
    main_data.append(texts_list)
    for file in files_list:
        file_data = []
        for text in texts_list:
            file_data.append(get_info(file, text))
        main_data.append(file_data)  
    return main_data
def write_to_csv(file_route, data):
    out_file = open(file_route, "w")
    for info in data:
        info = ';'.join(info)
        out_file.write(f"{info}\n")
    out_file.close()
data = get_data(files_list, texts_list)
write_to_csv(csv_file, data)   
with open(csv_file) as f_n:
    f_n_reader = csv.reader(f_n)
    f_n_headers = next(f_n_reader)
    print('Headers: ', f_n_headers)
    for row in f_n_reader:
        print(row)





    








