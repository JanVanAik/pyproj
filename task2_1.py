import random
amount = int(input('Введите количество монеток: '))
list = []
for i in range(amount):
    list.append(random.choice(['tales', 'heads']))
headsOrTalesCounter = [0, 0]
for i in range(amount):
    if list[i] == "heads":
        headsOrTalesCounter[0] += 1
    else:
        headsOrTalesCounter[1] += 1
print(list)
print(min(headsOrTalesCounter))




