import math
# num = float(input('Введите необходимую точность(0.1-0.0000000001): '))
# if 0.0000000001 <= num <= 0.9999999999:
#     count = 0
#     while num < 1:
#         num *= 10
#         count += 1
#     print(round(math.pi, count))
# else:
#     print('Неверная точность!')


num = int(input('Введите число знаков после запятой(1...10): '))
if 1 <= num <= 10:
    print(round(math.pi, num))
else:
    print('Неверное число знаков!')
