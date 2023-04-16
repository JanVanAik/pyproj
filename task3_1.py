import random

# Если массив генерируем мы

userNum = int(input('Введите число N: '))
targetNumber = int(input('Введите искомое число: '))
randomList = [random.randint(1, userNum) for i in range(userNum + 1)]
count = 0
for i in randomList:
    if i == targetNumber:
        count += 1

print(f'В заданном массиве вида "1..N"  {randomList} искомое число {targetNumber} встречается {count} раз ')


# Если массив вводит пользователь

upperBoard = int(input('Введите число N: '))
selectedNumber = int(input('Введите искомое число: '))
userList = [int(input('Введите следующее число массива: ')) for i in range(upperBoard)]
counter = 0
for i in userList:
    if i == selectedNumber:
        counter += 1

print(f'В заданном массиве вида "1..N"  {userList} искомое число {selectedNumber} встречается {counter} раз ')