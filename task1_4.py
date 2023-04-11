# Для успеха число долек должно быть кратно размеру одной из сторон

nums = [int(n) for n in list
(input('Введите размеры сторон и количество долек через запятую: ').replace(' ', '').split(','))]
if nums[0] * nums[1] < nums[2]:
    print('Да там делить то нечего, так ешь')
elif nums[2] % nums[0] == 0 or nums[2] % nums[1] == 0:
    print('Разделить можно')
else:
    print('Your chocolate is in another castle')
