import yaml
file_yaml = 'my_file.yaml'
names = [
    'items', 'items quanity', 'items price'
]
items = [
    'car', 'potato', 'train'
]
items_quantity= len(items)
items_price = {'120€': items[0], '1€': items[1], '1000€': items[2]}
data_to_yaml = {names[0]:items, names[1]:items_quantity, names[2]:items_price}
with open(file_yaml, 'w') as f_n:
    yaml.dump(data_to_yaml, f_n, default_flow_style=False, allow_unicode=True)

with open(file_yaml) as f_n:
    print(f_n.read())





