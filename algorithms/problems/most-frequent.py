# Problem: Most Frequent Element
# Approach: HashMap - O(n)
# Date: 10-04-2026

nums=[3, 3, 1, 1, 1, 0, 0, 0, 0]

def most_frequent(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] +=1
        else:
            count[num] = 1
    return max(count, key=count.get)

print(most_frequent(nums))