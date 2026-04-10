# Problem: Contains Duplicate
# Approach: HashMap - O(n)
# Date: 10-04-2026

nums=[2, 1, 1]

def containsDuplicate(nums):
  count={}
  for num in nums:
    if num in count:
      count[num] +=1
    else:
      count[num] = 1
  for num in count:
    value= count[num]
    if value>1:
      return True
    
  return False
    
print(containsDuplicate(nums))