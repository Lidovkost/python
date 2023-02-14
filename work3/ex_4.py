goods = []
name = 'название'
names = 'названия'
price = 'цена'
prices = 'цены'
count = 'количество'
counts = 'количества'
units = 'ед'
add_goods_info = True 
item_index = 0

def output_check():
    output = input(f'чтобы добавить еще товар введите любой символ, чтобы закончить - end ')
    if output == 'end':
        return False 
    return True

while(add_goods_info):
    item_index += 1
    goods_info = {name: None, price: None, count: None, units: None}
    for info in goods_info:
        goods_info[info] = input(f'введите {info} товара ')
    goods_info[price] = int(goods_info[price])
    goods_info[count] = int(goods_info[count])
    variable = (item_index, goods_info,)
    goods.append(variable)
    add_goods_info = output_check()

name_values = []
price_values = []
count_values = []
units_values = []
for item in goods:
    name_values.append(item[1][name])
    price_values.append(item[1][price])
    count_values.append(item[1][count])
    units_values.append(item[1][units])

goods_dict = {
names: name_values,
prices: price_values,
counts: count_values,
units: units_values
}       
print(*goods, sep = '\n')
print(goods_dict)
