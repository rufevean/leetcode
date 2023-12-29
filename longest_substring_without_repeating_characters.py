def lswuc(s : str) -> str:
    longest = 0
    left = 0
    new_set = set()
    if len(s)==0:
        return 0 
    for right in range(len(s)):
        while s[right] in new_set:
            new_set.remove(s[left])
            left = left + 1
        new_set.add(s[right])
        longest = max(longest,right-left + 1)

    return longest 
