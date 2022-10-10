import random
num = int(input('Введите степень многочлена(1...5): '))
if 1 <= num <= 5:
    string = f'{random.randint(1,100)}'
    for i in range(1, num+1):
        string += f' + {random.randint(1,100)}*x^{i}'
    # string = string.replace('^1', '')                    хотел сделать красивую печать степенями в файл, но потом понял,
    # string = string.replace('^2', '\u00B2')              что в 5-ом задании я их не достану в том же виде(
    # string = string.replace('^3', '\u00B3')
    # string = string.replace('^4', '\u2074')
    # string = string.replace('^5', '\u2075')
    # print(string)
    # with open('text1.txt', 'w', encoding='utf-8') as f:
    #     f.write(string)
    #     f.write('\n')
    with open('text1.txt', 'w') as f:
        f.write(string)
else:
    print('Неверно указана степень!')
