season_list = [
    'зима', 'весна', 'лето', 'осень'
]
season_map = [
    1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 1
]
season_dict = {
  'зима': [12, 1, 2],
  'весна': [3, 4, 5],
  'лето': [6, 7, 8],
  'осень': [9, 10, 11]
}
month = int(input('Введите номер месяца: '))
print(season_list[season_map[month-1]-1])
for season in season_dict:
    if month in season_dict[season]:
        month = season
print(month)


