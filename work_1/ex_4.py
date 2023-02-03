text_profit = 'Финансовый результат - прибыль. Ее величина: '
text_profit_of_revenue = 'Рентабельность выручки = '
text_workers_count = 'Введите численность сотрудников фирмы: '
text_profit_per_worker = 'Прибыль фирмы в расчете на одного сотрудника = '
text_loss = 'Финансовый результат - убыток. Его величина:'

revenue = float(input('Введите выручку фирмы: '))
costs = float(input('Введите издержки фирмы: '))

fin_result = revenue - costs
if fin_result > 0:
    print(text_profit,fin_result)
    print(text_profit_of_revenue,fin_result/revenue)
    workers_count = int(input(text_workers_count))
    print(text_profit_per_worker,fin_result/workers_count)
else: print(text_loss,abs(fin_result))

