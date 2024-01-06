def first_last_occurance(nums,target):
    def binary_search(nums,target):
        low = 0
        high = len(nums)-1
        first_occurance = -1 
        
        while low <= high:
            mid = (low+high)//2 
            if target == nums[mid]:
                first_occurance = mid
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return first_occurance
    def binary_search_reverse(arr, target):
        low, high = 0, len(arr) - 1
        last_occurance = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                last_occurance = mid
                low = mid + 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1 
        return last_occurance
    first_element = binary_search(nums,target)
    second_element = binary_search_reverse(nums,target)
    return [first_element,second_element]
