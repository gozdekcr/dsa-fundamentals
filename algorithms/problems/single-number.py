# Problem: Single Number
# Approach: Linear Search - O(n²)
# Date: 10-03-2026

nums = [2,2,1]


def singleNumber(nums):
    for i in nums:
        if nums.count(i) == 1:
            print(i)
        
singleNumber(nums)