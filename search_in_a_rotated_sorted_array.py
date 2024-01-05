
def rotating_array(nums : list[int],target :int)-> int:
    def find_pivot(nums ):
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 1
        low = 0
        high = len(nums)-1
        while low <= high:
            if nums[low] > nums[high]:
                low = low + 1
            else:
                return low 
        return 0
    def binary_search(nums,target):
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high)//2 
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid -1 
        return -1
    pivot = find_pivot(nums)
    print(pivot)
    new_nums = nums[pivot:]+nums[:pivot]
    search = binary_search(new_nums,target)
    if search != -1:
        if search + pivot >= len(nums) : 
            return search + pivot - len(nums)
        return search + pivot
    else:
        return -1 
