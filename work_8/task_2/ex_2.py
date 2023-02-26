import json
import datetime
file_json = 'mes_2.json'
def write_order_to_json(item, quantity, price, buyer, date):
    dict_to_json = {"item": str(item), "quantity": int(quantity), "price": float(price), "buyer": str(buyer), "date": date}
    with open(file_json) as f_n:
        objs = json.load(f_n)
    f_n.close()
    objs['orders'].append(dict_to_json)
    with open(file_json, 'w') as f_n:
        json.dump(objs, f_n, sort_keys = True, indent = 4)
    f_n.close()
today = datetime.datetime.today()
date = today.strftime("%Y-%m-%d-%H.%M.%S")
write_order_to_json('chocolate', 777, 666, 'kostya', date)