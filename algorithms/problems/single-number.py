# Problem: Single Number
# Approach: HashMap - O(n²)
# Date: 10-03-2026

nums = [2,2,1]


def singleNumber(nums):
    for i in nums:
        if nums.count(i) == 1:
            print(i)
        
singleNumber(nums)

# Problem: Single Number
# Approach: HashMap - O(n)
# Date: 05-05-2026

list = [2,2,1]

def single_number(list):
    set = {}
    for i in list:
        if i in set:
            set[i]-=1
        else:
            set[i] = 1
    return max(set, key=set.get)

print(single_number(list))