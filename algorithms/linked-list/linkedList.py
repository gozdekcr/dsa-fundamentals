#Node -> Linked list

#singly linked list

class Node():
    def __init__(self,value):
        self.value = value
        self.nextNode = None

firstNode = Node(10)
secondNode = Node(20)
thirdNode = Node(30)

firstNode.nextNode = secondNode
secondNode.nextNode = thirdNode

print(firstNode.nextNode.value)     #secondNode's value
print(firstNode.nextNode.nextNode.value)   #thirdNode's value


#doubly linked list

class doublyNode():
    def __init__(self,value):
        self.value = value
        self.nextNode = None
        self.prevNode = None
        
firstNode = doublyNode(5)
secondNode = doublyNode(10)
thirdNode = doublyNode(15)

firstNode.nextNode = secondNode
secondNode.prevNode = firstNode
secondNode.nextNode = thirdNode
thirdNode.prevNode = secondNode

print(firstNode.nextNode.nextNode.value) #thirdNode's value
print(thirdNode.prevNode.prevNode.value) #firstNode's value
