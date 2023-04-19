import random

# Если список вводит пользователь
# userNum, targetNumber = (int(input('Введите количество чисел в списке: ')), int(input('Введите искомое число: ')))
# randomList = [int(input('Введите следующее число массива: ')) for i in range( userNum)]

userNum, targetNumber = (int(input('Введите количество чисел в списке: ')), int(input('Введите искомое число: ')))
randomList = [random.randint(1, userNum) for i in range(userNum + 1)]
result = randomList[0]
for i in randomList:
    if abs(i - targetNumber) < abs(result - targetNumber):
        result = i
print(f'В списке {randomList} из {userNum} чисел, первое найденное ближайшее к {targetNumber}  число - это {result}')
