# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        shift = 0
        result = ListNode(0)
        origin_result = result

        while l1 or l2:
            v1_value = l1.val if l1 else 0
            v2_value = l2.val if l2 else 0

            result.val += v1_value + v2_value
            if result.val >= 10:
                result.val = result.val - 10
                shift = 1

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if not l1 and not l2 and not shift:
                break

            result.next = ListNode(shift)
            result = result.next
            shift = 0

        return origin_result
