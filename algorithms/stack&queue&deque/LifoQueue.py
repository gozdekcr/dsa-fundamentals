#Last in first out

from queue import LifoQueue

lifoQueue = LifoQueue()

lifoQueue.put(1)
lifoQueue.put(10)
lifoQueue.put(20)

print(lifoQueue.get())

print(lifoQueue.get())

from queue import Queue

myQueue = Queue()

myQueue.put(1)
myQueue.put(10)
myQueue.put(20)

print(myQueue.get())
print(myQueue.get())

from collections import deque

myDeque = deque()

myDeque.append(10)
myDeque.append(20)
myDeque.append(30)

print(myDeque)

myDeque.appendleft(40)

print(myDeque)

myDeque.popleft()

print(myDeque)
