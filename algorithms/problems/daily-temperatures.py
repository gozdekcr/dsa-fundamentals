# Problem: Daily Temperature
# Approach: 
# Date: 05-10-2026

temperatures = [73,74,75,71,69,72,76,73]

def solution():
    result = [0] * len(temperatures)  #daha baştan içinde sıfırlar olan result listi oluşturuyoruz
    myStack = [] #temp  ve index koymamız lazım
    
    for index, temperature in enumerate(temperatures):
        while myStack and temperature > myStack[-1][0]:
            stackTemp, stackIndex= myStack.pop()
            result[stackIndex] = index - stackIndex
        myStack.append([temperature,index])
    return result    
print(solution())
        
        
    
        
    