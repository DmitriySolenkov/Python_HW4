def polynomSum(array1, array2, index):
    buffer1 = array1[index].split('*')
    buffer2 = array2[index].split('*')
    sum = int(buffer1[0])+int(buffer2[0])
    sumX = str(sum)+buffer1[1]
    return sumX


f = open('text.txt')
polynom1 = f.read()
f.close
f = open('text1.txt')
polynom2 = f.read()
f.close
print(polynom1)
print(polynom2)
array1 = polynom1.split(' + ')
array2 = polynom2.split(' + ')
if len(array1) <= len(array2):
    length = len(array1)
else:
    length = len(array2)
polSum = [int(array1[0])+int(array2[0])]
for i in range(1, length):
    polSum.append(polynomSum(array1, array2, i))
for i in range(length, len(array1)):
    polSum.append(array1[i])
for i in range(length, len(array2)):
    polSum.append(array2[i])
print(" + ".join(map(str, polSum)))
