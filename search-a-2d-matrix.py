def list_find(matrix: list[list[int]],target :int) -> bool :
    n = 0 
    while target > matrix[n][-1]:
        if target <= matrix[-1][-1]:
            n = n +1
        else:
            break 
    def binary_search(nums,target):
        low,high = 0,len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid -1
        return False 
    result = binary_search(matrix[n],target)
    return result

