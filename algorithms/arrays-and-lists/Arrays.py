#Array, List

import array as arr
array1 = arr.array("i", [1,2,3,4])
array1.append(15)
print(array1)

myList= [1,2,3,4,5]
otherList= [6,7,8,9]

myList.extend(otherList)
print(myList)

result = [0] * 8
print(result)

import sys
n = 30
myDynamicArray = []
for i in range(n):

    myLength = len(myDynamicArray)
    myByte = sys.getsizeof(myDynamicArray)
    print(f"Lenght: {myLength} Byte: {myByte}")
    myDynamicArray.append(n)
