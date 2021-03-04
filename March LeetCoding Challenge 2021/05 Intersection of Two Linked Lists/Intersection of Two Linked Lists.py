# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Explnation for solution
# If the length of linked lists had been the same, finding the intersection node would be as easy as iterating over both linked list simultaneously and returning if same node is found.
# In the given question, however, we need to first align the lists. The head of list with greater length need to be iterated forward diff times(difference of lengths) and the final answer won't be affected by this since length of list after intersection must be same(meaning intersection surely wouldn't exist in the first diff nodes) . This way, we can parallelly compare nodes of both list and return if two nodes match.


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB
        n1 = 0
        n2 = 0
        while(a):
            n1 = n1 + 1
            a = a.next
        while(b):
            n2 = n2 + 1
            b = b.next
        a = headA
        b = headB
        while(a and (n1 > n2)):
            a = a.next
            n1 = n1 - 1
        while(b and (n2 > n1)):
            b = b.next
            n2 = n2 - 1
        while(a and b):
            if(a == b):
                return a
            a = a.next
            b = b.next
        if(a):
            return b
        return a

        # Time limit exceeded
        # headOne = headA
        # while(headOne):
        #     headTwo = headB
        #     while(headTwo):
        #         if(headOne == headTwo):
        #             return headOne
        #         headTwo = headTwo.next
        #     headOne = headOne.next
        # return headOne
