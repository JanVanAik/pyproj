import random

# Если массив генерируем мы

userNum = int(input('Введите число N: '))
targetNumber = int(input('Введите искомое число: '))
userList = [random.randint(1, userNum) for i in range(userNum + 1)]
count = 0
for i in userList:
    if i == targetNumber:
        count += 1

print(f'В заданном массиве вида "1..N"  {userList} искомое число {targetNumber} встречается {count} раз ')


# Если массив вводит пользователь

userNum = int(input('Введите число N: '))
targetNumber = int(input('Введите искомое число: '))