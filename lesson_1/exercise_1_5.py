plus = float(input("Введите сумму выручки фирмы: "))
minus = float(input("Введите сумму издержек фирмы: "))
if plus > minus:
    print("Прибыль - выручка больше издержек")
else:
    print("Убыток - издержки больше выручки")
profit = plus - minus
print(f"Рентабельность: {profit / plus * 100}%")
workers = int(input("Введите численность сотрудников Вашей фирмы: "))
print(f"Прибыль фирмы в расчете на одного сотрудника: {profit/workers}")
