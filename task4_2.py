amount = int(input('Введите количество грядок: '))
gardenList = [int(input('Введите  количество ягод на следующей грядке: ')) for n in range(amount)]
localMaxList = []
for i in range(len(gardenList)):
    if i == 0:
        localMaxList.append(gardenList[i] + gardenList[i+1] + gardenList[-1])
    elif i == len(gardenList) - 1:
        localMaxList.append(gardenList[i] + gardenList[i - 1] + gardenList[0])
    else:
        localMaxList.append(gardenList[i - 1] + gardenList[i] + gardenList[i + 1])
print(f'В наборе грядок {gardenList} наибольший локальный максимум будет равен {max(localMaxList)}, '
      f'для элемента под номером {localMaxList.index(max(localMaxList)) + 1}')