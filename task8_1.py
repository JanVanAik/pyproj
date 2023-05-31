# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
#
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной


import re

def fixNum(number):
    number = number.replace(' ', '')
    return f'{number[0]}({number[1:4]}){number[4:]}'

def validateNum(number):
    return re.match(r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$',
                   number.replace('-', '').replace(' ', ''))

def phoneNumberWork(number):
    if validateNum(number):
        return fixNum(number)
    else:
        return False

def importInfo(info):
    sortedText = info.split(',')
    if len(sortedText) < 3:
        return 'You entered incorrect parameters'
    phoneNum = phoneNumberWork(sortedText[2])
    if not phoneNum:
        return 'Phone number is invalid'
    try:
        comments = sortedText[3]
    except IndexError:
        comments = ' '
    with open('phoneBook.txt', 'a', encoding='utf-8') as file:
        file.write(f'{sortedText[0].replace(" ", "")}---{sortedText[1]}---{phoneNum}---{comments}\n')
        return 'User is added'


def exportInfo(fileName):
    with open('phoneBook.txt', 'r', encoding='utf-8') as file:
        with open(f'{fileName}.txt', 'w', encoding='utf-8') as expFile:
            for line in file:
                expFile.write(line)
    return 'Export File is ready'



def searchInfo(info):
    with open('phoneBook.txt', 'r', encoding='utf-8') as file:
        res = 'We have found following users: \n'
        for line in file:
            if info in line:
                line = line.split('---')
                res += f'\nName: {line[0]}\nSecond Name: {line[1]}\nPhone number: {line[2]}\nComments: {line[3]}\n'
        return res



if __name__ == '__main__':
    userChoice = input('Write "import", "export", or "search":\n')
    if userChoice == 'import':
        print(importInfo(input(f'Enter following parameters, split with commas.\n1)Name\n'
                         f'2)Second name\n3)Phone number \n4)Comments\n')))
    elif userChoice == 'export':
        print(exportInfo(input('If you want to export information, '
                                          'enter file name, where you want to export: ')))
    elif userChoice == 'search':
        print(searchInfo(input('Enter search parameter: ')))


