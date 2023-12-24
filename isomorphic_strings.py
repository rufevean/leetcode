def isomorphic(s : str,t : str) -> bool:
    if len(s) != len(t) :
        return False
    newhash = {}
    newhash2 = {}
    for i in range(len(s)):
        if s[i] in newhash:
            if t[i] != newhash[s[i]]:
                return False
        if t[i] in newhash2:
            if s[i] != newhash2[t[i]]:
                return False
        
        newhash[s[i]] = t[i]
        newhash2[t[i]] = s[i]
    
    return True
        
