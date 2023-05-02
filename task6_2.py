# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

amount = int(input('Введите количество элементов прогрессии: '))
progression = [int(input('Введите  следующий элемент прогрессии: ')) for n in range(amount)]
userRange = tuple(input('Введите левую и правую границы заданного диапазона: ').replace(',', '').split())
sortedProgression = sorted(progression)

for val in sortedProgression:
    if val >= int(userRange[0]):
        leftBorder = sortedProgression.index(val)
        break

for val in sortedProgression:
    if val == int(userRange[1]):
        leftBorder = sortedProgression.index(val)
        break
    if val > int(userRange[1]):
        rightBorder = sortedProgression.index(val)-1
        break

print(f'Числа в вашем диапазоне находятся от индекса {leftBorder} до {rightBorder}')
