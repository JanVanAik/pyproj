def letter_sort(array):

    if len(array) == 0:
        return array
    return f'{array[0] + str(array.count(array[0]))}' + letter_sort(array[1:].replace(array[0], ''))

print(letter_sort('aggaryaaaahhhygjjj'))
# output: a6g3r1y2h3j3
print(letter_sort(''))
# output: empty
try:
    print(letter_sort())
except TypeError:
    print('Вы забыли ввести строку')
#  output: 'Вы забыли ввести строку'

