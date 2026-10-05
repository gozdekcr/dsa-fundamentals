# Problem: Baseball Game
# Approach:
# Date: 23-09-2026

myInput = ["5", "2", "C", "D", "+"]

def solution():
    
    myStack = []
    
    for op in myInput:
        if op == "C":
            myStack.pop()
        elif op=="+":
            myStack.append(myStack[-1] + myStack[-2])
        elif op == "D":
            myStack.append(2* myStack[-1])
        else:
            myStack.append(int(op))
    return sum(myStack)

print(solution())
