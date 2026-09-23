# Problem: Implement Stack using Queues
# Approach: 
# Date: 23-09-2026

from collections import deque


class myStack:
    def __init__(self):
        self.myQueue = deque()

    def push(self, x: int) -> None:
        self.myQueue.append(x) 
        
    def pop(self):
        for i in range(len(self.myQueue)-1):
            self.myQueue.append(self.myQueue.popleft)
        return self.myQueue.popleft()
    
    def top(self):
        return self.myQueue[-1]
    
    def empty(self):
        return len(self.myQueue) == 0