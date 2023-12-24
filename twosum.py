def twosum(nums : list,target : int):
    newhash = {}
    for key,value in enumerate(nums):
        if target-value in newhash:
            return (newhash[target-value],key)
        else:  
            newhash[value] = key
    
