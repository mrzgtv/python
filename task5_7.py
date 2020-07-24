import json

profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('text_7.txt', 'r', encoding="utf-8") as file:
    for line in file:
        comp_name, comp_type, earning, costs = line.split()
        profit[comp_name] = float(earning) - float(costs)
        if profit.setdefault(comp_name) >= 0:
            prof = prof + profit.setdefault(comp_name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.1f}')
    else:
        print(f'Прибыль - отсутсвует. Все в убытках')
    print(f'Прибыль каждой компании - {profit}')

with open('text_77.json', 'w', encoding="utf-8", ) as write_js:

    json.dump(profit, write_js, ensure_ascii=False)

