def recursiveExponentiation(x, y):
    if y == 1:
        return x
    return x * recursiveExponentiation(x, y-1)

print(recursiveExponentiation(2, 10))
# output 1024