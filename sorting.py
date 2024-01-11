
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array
def select_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1,len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i],array[min_index] = array[min_index],array[i]
    return array

def insert_sort(array):
    for i in range(1,len(array)):
        pre_index = i-1
        current = array[i]
        while pre_index >= 0 and array[pre_index] > current:
            array[pre_index+1] = array[pre_index]
            pre_index -= 1
        array[pre_index+1] = current
    return array

def merge_sort(array):
    if len(array) <= 1:
        return array
    num = len(array)//2
    left = merge_sort(array[:num])
    right = merge_sort(array[num:])
    return merge(left,right)

def merge(left,right):
    l,r = 0,0
    result = []
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l+=1
        else:
            result.append(right[r])
            r+=1
    result += left[l:]
    result += right[r:]
    return result

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i<=pivot]
        greater = [i for i in array[1:] if i>pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

def redix_sort(array):
    max_num = max(array)
    it = 0
    while 10**it <= max_num:
        buckets = [[] for _ in range(10)]
        for num in array:
            buckets[num//(10**it)%10].append(num)
        array.clear()
        for bucket in buckets:
            array.extend(bucket)
        it += 1
    return array
