array = list(map(int, input('Введите числа через пробел: ').split()))
newArray = []
newArray.append(array[0])
for i in array:
    count = 0
    for j in range(len(newArray)):
        if i != newArray[j-1]:
            count += 1
        if count == len(newArray):
            newArray.append(i)

print(array)
print(newArray)
