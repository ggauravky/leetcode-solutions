#  61. Rotate List (leetcode #61)
# 61. Rotate List

# Given the head of a linked list, rotate the list to the right by k places.


# Example 1:

# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:

# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
 


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None or k==0:
            return head
        
        l=0
        last = head
        while last.next != None:
            last=last.next
            l+=1
        l+=1
        
        k=k%l
        if k==0:
            return head
        
        current=head
        for _ in range(l-k-1):
            current=current.next
            
        last.next=head
        head=current.next
        current.next=None
        
        return head