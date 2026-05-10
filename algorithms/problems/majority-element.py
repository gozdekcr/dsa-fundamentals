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