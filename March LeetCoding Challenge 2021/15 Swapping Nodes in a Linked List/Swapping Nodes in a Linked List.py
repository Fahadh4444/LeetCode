# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        temp = head
        change = head
        toChange = head
        n = 0
        while(temp):
            n = n+1
            temp = temp.next
        for i in range(k-1):
            change = change.next
        for i in range(n-k):
            toChange = toChange.next
        a, b = change.val, toChange.val
        change.val, toChange.val = b, a
        return head
