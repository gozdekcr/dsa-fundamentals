# Valid Anagram
# Approach: HashMap frequency count
# Date: 07.05.26

s = "anagram"
t = "nagaram"

def isAnagram(w1, w2):
    char = {}
    for i in w1:
        if i in char:
            char[i] += 1
        else:
            char[i] = 1
    for g in w2:
        if g not in char:
            return False
        else:
            char[g] -= 1
    for k in char:
        if char[k] != 0:
            return False
    
    return True

print(isAnagram(s,t))