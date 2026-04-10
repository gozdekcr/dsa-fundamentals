list = [2,2,1]


def singleNumber(nums):
    for i in nums:
        if nums.count(i) == 1:
            print(i)
        

singleNumber(list)