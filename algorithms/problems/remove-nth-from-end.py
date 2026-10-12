# Problem: Remove Nth From End
# Approach:
# Date: 07-10-2026

def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        dummy = ListNode(0, head)
        curr = dummy

        for _ in range(length - n):
            curr = curr.next

        curr.next = curr.next.next

        return dummy.next


        leftPointer = head
        rightPointer= head

        while n > 0 and rightPointer:
            rightPointer = rightPointer.next
            n -= 1
        while rightPointer and rightPointer.next:
            leftPointer = leftPointer.next
            rightPointer = rightPointer.next

        if leftPointer == head and rightPointer:
            return head.next
            
        leftPointer.next = leftPointer.next.next
        return head   