import math

numbers = [int(n) for n in list
(input('Введите два загаданных числа, через запятую: ').replace(' ', '').split(','))]
prod = numbers[1]*numbers[0]
summa = numbers[1] + numbers[0]
print(numbers)
# Решение через дискриминант, перебором пользоваться не стал - неоправданная трата памяти
# D = b**2 - 4ac
# x1 = (-b-sqrt(D))/2a = (-b-sqrt(b**2-4ac))/2a = (summa-sqrt(summa**2-4prod))/2
# x1 = (-b+sqrt(D))/2a = (-b+sqrt(b**2-4ac))/2a = (summa+sqrt(summa**2-4prod))/2

print(f'Первое число равно  {int((summa - math.sqrt(summa**2 - 4 * prod)) / 2)}, '
      f'второе число равно  {int((summa + math.sqrt(summa**2 - 4 * prod)) / 2)}')


