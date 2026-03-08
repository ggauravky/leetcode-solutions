# 19. Remove Nth Node From End of List

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        p1=head
        p2=head
        for i in range(n):
            p2=p2.next
        
        if p2==None:
            return head.next
        
        while p2.next!=None:
            p1=p1.next
            p2=p2.next
        
        p1.next=p1.next.next
        return head

# The idea is to use two pointers, p1 and p2. We move p2 n steps ahead of p1. Then we move both pointers one step at a time until p2 reaches the end of the list. At this point, p1 will be pointing to the node just before the node we want to remove. We can then skip the node to be removed by setting p1.next to p1.next.next. Finally, we return the head of the modified list.
# Time complexity: O(L), where L is the length of the linked list.
# Space complexity: O(1), since we are using only a constant amount of extra space