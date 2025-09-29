sum = int(input("Введите сумму "))

money = [100, 50, 10, 5, 2, 1]

for denga in money:
    print(f"Нужно {sum//denga} бумажек по {denga}")
    sum %= denga

