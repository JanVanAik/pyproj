borderNumber = int(input('Введите N: '))
res = []
degree = 0
while 2**degree < borderNumber:
    res.append(2**degree)
    degree +=1
print(res)