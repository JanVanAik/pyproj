sum = int(input('Введите количество журавликов: '))
if sum%6 == 0:
 # X+Y+Z = sum
 # X = Y
 # Z = 2*(X+Y) =>
 # sum = X+Y+2X + 2Y = 6X and
 # Z = 4x = 4/6 sum
    print(f'Дети сделали {int(sum/6)}, {int(sum/6)} и {int(sum*4/6)} журавликов')
else:
    print('Дети сделали некорректное количество журавликов, мы их обязательно покараем')