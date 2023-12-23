
def container(array:list):
    i = 0
    j = len(array)-1
    area = 0 
    while i < j:
        if array[i] < array[j]:
            area = max(area,(j-i) * array[i])
            i = i+1
        
        else:
            area = max(area,(j-i)*array[j])
            j = j - 1
    return area

result = container(array)
print(result)

