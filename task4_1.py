firstSetLen, secondSetLen = [int(n) for n in list
(input('Введите размеры двух множеств через запятую: ').replace(' ', '').split(','))]

firstSet = set([int(input('Введите следующий элемент первого множества: ')) for n in range(firstSetLen)])
secondSet = set([int(input('Введите следующий элемент второго множества: ')) for n in range(secondSetLen)])
print(f'Множество {firstSet} имеет с множеством {secondSet} следующиеобщие значения: '
      f'{sorted(list(firstSet.intersection(secondSet)))}')