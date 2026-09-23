"""
Deque()

addLeft()
addRight()

removeLeft()
removeRight()

isEmpty()
size()

"""

class Deque():
    def __init__(self):
        self.elements = []
        
    def isEmpty(self):
        self.elements == []
        
    def size(self):
        return len(self.elements)    
    
    def addLeft(self,element):
        self.elements.insert(0,element)
    
    def addRight(self,element):
        self.elements.append(element)
        
    def removeLeft(self):
        return self.elements.pop(0)
        
    def removeRight(self):
        return self.elements.pop()
    
    
myDeque = Deque()

print(myDeque.isEmpty)

myDeque.addRight(10)
myDeque.addRight(20)
myDeque.addRight(30)
myDeque.addLeft(40)
myDeque.addLeft(50)

