def all_perms(nums : list ) -> list:
    perms = [] 
    if len(nums)== 0 : return [[]] # returning empty list when array is empty
    def swap(i,j,nums):
        nums[i],nums[j] = nums[j],nums[i]
    def helpers(nums,i):
        if i == len(nums) -1 :
            perms.append(nums[:])
            return 
        for j in range(i,len(nums)): 
            swap(i,j,nums)
            helpers(nums,i+1)
            swap(i,j,nums)
    helpers(nums,0)
    return perms

