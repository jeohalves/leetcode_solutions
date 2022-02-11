# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and not list2:
            return 
        elif not list1:
            return list2
        elif not list2:
            return list1
        
        
        if list1.val <= list2.val: 
            first = list1
            prev = list1
            cur = list1.next
            other = list2
        else:
            first = list2
            prev = list2
            cur = list2.next
            other = list1
            
        
        while True:
            if other is None:
                cur = cur.next
                continue
            
            if cur is None:
                prev.next = other
                break
            
            if cur.val <= other.val:
                prev = cur
                cur = cur.next
            else:
                prev.next = other
                prev = other 
                
                other = cur                
                cur = prev.next           
            
        
        return first

