# Problem: Majority Element
# Approach: HashMap - O(n)
# Date: 10-05-2026

nums = [2,2,1,1,1,2,2]
def majorityElement(nums):
    count = {}
    for i in nums:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return max(count , key=count.get)

print(majorityElement(nums))

# Boyer Moore
# Space O(1) time O(n)
# Date: 27-08-2026

def boyerMoore():
    count= 0
    result = 0
    
    for num in nums:
        if count == 0:
            result = num
        if num == result:
            count +=1
        else:
            count -=1
    return result

print(boyerMoore())