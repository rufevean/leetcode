def fnc(s : str) -> int:
        new_hash = {}
        for ele in s:
            if ele not in new_hash:
                new_hash[ele] = 1
            else:
                new_hash[ele] += 1
        for index,ele in enumerate(s):
            if new_hash[ele] == 1:
                return index
        return -1
