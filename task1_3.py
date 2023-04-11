num = input('Введите номер билета: ')
left = int(num[:3])
right = int(num[3:])
print((left // 100 + left % 100 // 10 + left % 10) == (right // 100 + right % 100 // 10 + right % 10))
