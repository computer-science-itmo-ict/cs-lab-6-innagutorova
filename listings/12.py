fin = open('input.txt')
temp = fin.readline().split(',')
num = []
for i in range(len(temp)):
    num.append(int(temp[i]))
fout = open('output.txt', 'w')

def randomized_quick_sort3(nums, start, end):
    if start < end - 1:
        k = randint(start, end - 1)
        nums[k], nums[start] = nums[start], nums[k]
        m1, m2 = partition3(nums, start, end, nums[start])
        randomized_quick_sort3(nums, start, m1)
        randomized_quick_sort3(nums, m2 + 1, end)

def partition3(nums, start, end, x):
    j = start
    k = 0
    for i in range(start + 1, end):
        if nums[i] <= x:
            j = j + 1
            if nums[i] == x:
                k += 1
            nums[j], nums[i] = nums[i], nums[j]
    nums[j], nums[start] = nums[start], nums[j]
    return j - k + 1, j

randomized_quick_sort3(num, 0, len(num))
hirsh = 0
for h in range(num[-1]):
    m1, m2 = partition3(num, 0, len(num), h)
    if len(num) - m1 >= h:
        hirsh = h
    else:
        break
fout.write(str(hirsh))
fin.close()
fout.close()