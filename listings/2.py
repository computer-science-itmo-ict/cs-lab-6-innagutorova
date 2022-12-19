
def scarecrow_sort(num, k):
    for i in range(0, len(num) - k):
        if num[i] > num[i + k]:
            num[i], num[i + k] = num[i + k], num[i]

fin = open('input.txt')
n, k = fin.readline().split()
temp = fin.readline().split()
num = []
for i in range(len(temp)):
    num.append(int(temp[i]))
n = int(n)
k = int(k)
fout = open('output.txt', 'w')

scarecrow_sort(num, k)
res = 'ДА'
for i in range(0, len(num) - 1):
    if num[i] > num[i + 1]:
        res = 'НЕТ'
        break

fout.write(res)
fin.close()
fout.close()