# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Init with dummy value which is lower than minimal value.
        return_list = temp_merged_list = ListNode(-101)
        while l1 or l2:
            if not l1:
                temp_merged_list.next = ListNode(l2.val)
                l2 = l2.next
            elif not l2:
                temp_merged_list.next = ListNode(l1.val)
                l1 = l1.next                  
            elif l1.val > l2.val:
                temp_merged_list.next = ListNode(l2.val)
                l2 = l2.next
            else:
                temp_merged_list.next = ListNode(l1.val)
                l1 = l1.next  
            # Continue to set next value.
            temp_merged_list = temp_merged_list.next
        # Omit first irrelevant item, return "return_list"
        return return_list.next
                
        