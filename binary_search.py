
def binary_search(arr : list[int],key : int) -> int:
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2

        if key == arr[mid]:
            return mid
        elif key > arr[mid]:
            low = mid + 1
        else:
            high = mid -1 

    return -1 
    
