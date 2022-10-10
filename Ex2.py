def factorSearch(num):
    for i in range(2, num+1):
        if num % i == 0:
            mult.append(i)
            break


num = int(input('Введите число для нахождения простых множителей: '))
mult = []
factorSearch(num)
num = int(num/mult[len(mult)-1])
while num >= mult[len(mult)-1]:
    factorSearch(num)
    num = int(num/mult[len(mult)-1])
print(mult)
