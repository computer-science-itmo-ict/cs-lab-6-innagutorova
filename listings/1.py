
fin = open('input.txt')
n = int(fin.readline())
num = fin.readline().split()
fout = open('output.txt', 'w')
def quick_sort(nums, start, end):
    if start < end - 1:
        m = partition(nums, start, end)
        quick_sort(nums, start, m)
        quick_sort(nums, m + 1, end)
def randomized_quick_sort(nums, start, end):
    if start < end - 1:
        k = randint(start, end - 1)
        nums[k], nums[start] = nums[start], nums[k]
        m = partition(nums, start, end)
        randomized_quick_sort(nums, start, m)
        randomized_quick_sort(nums, m + 1, end)
def partition(nums, start, end):
    x = nums[start]
    j = start
    for i in range(start + 1, end):
        if nums[i] <= x:
            j = j + 1
            nums[j], nums[i] = nums[i], nums[j]
    nums[j], nums[start] = nums[start], nums[j]
    return j
def quick_sort3(nums, start, end):
    if start < end - 1:
        m1, m2 = partition3(nums, start, end)
        quick_sort3(nums, start, m1)
        quick_sort3(nums, m2 + 1, end)
def randomized_quick_sort3(nums, start, end):
    if start < end - 1:
        k = randint(start, end - 1)
        nums[k], nums[start] = nums[start], nums[k]
        m1, m2 = partition3(nums, start, end)
        randomized_quick_sort3(nums, start, m1)
        randomized_quick_sort3(nums, m2 + 1, end)
def partition3(nums, start, end):
    x = nums[start]
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
quick_sort(num, 0, len(num))
fout.write(str(num).replace('[', '').replace(']', '').replace(',', '').replace("'", ''))
fin.close()
fout.close()