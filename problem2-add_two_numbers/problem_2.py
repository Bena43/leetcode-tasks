# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        degree = 0
        result = 0
        while l1 or l2:
            if not l1:
                result += l2.val*(10**degree)
                l2 = l2.next
            elif not l2:
                result += l1.val*(10**degree)
                l1 = l1.next
            else:
                result += (l1.val + l2.val)*(10**degree)
                l1 = l1.next
                l2 = l2.next
            degree += 1
        
        result_list_current = result_list_origin = ListNode(val=0)
        original_result = result
        while result > 0:
            result_list_current.next = ListNode(val = result % 10)
            result_list_current = result_list_current.next
            result //= 10
            
        if original_result > 0:
            result_list_origin = result_list_origin.next
        
        return result_list_origin