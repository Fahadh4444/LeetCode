# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# ////////////////////////////////////////////////////My Code//////////////////////////////////////////////////////
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         temp = head
#         n = 0
#         while(temp):
#             n = n + 1
#             temp = temp.next
#         temp = head
#         m = int(n/2)
#         arr = [0]*m
#         for i in range(0,m):
#             arr[i] = temp.val
#             temp = temp.next
#         if(n%2 != 0):
#             temp = temp.next
#         m = m - 1
#         while(m >= 0):
#             if(arr[m] != temp.val):
#                 return False
#             m = m - 1
#             temp = temp.next
#         return True


# ///////////////////////////////////////////////////////Best Solution///////////////////////////////////////////////
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        o = []
        while head:
            o.append(head.val)
            head = head.next
        return o == o[::-1]


# //////////////////////////////////////////////Second Best Solution//////////////////////////////////////////////////
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         if not head:
#             return True
#         vals = []
#         while head:
#             vals.append(head.val)
#             head = head.next
#         revers = []
#         for i in reversed(range(len(vals))):
#             revers.append(vals[i])
#         return revers == val
