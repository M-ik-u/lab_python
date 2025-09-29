time = int(input("Введите кол-во секунд: "))

min = time // 60
sec = time % 60

omin = ""
osec = ""

if min == 1:
    omin += str(min) + " минута "
elif 2 <= min <= 4:
    omin += str(min) + " минуты "
else:
    omin += str(min) + " минут "

if sec == 1:
    osec += str(sec) + " секунда "
elif 2 <= sec <= 4:
    osec += str(sec) + " секунды "
else:
    osec += str(sec) + " секунд "

print(f"{time} с = {omin}{osec}")