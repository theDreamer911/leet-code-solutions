class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return dummy.next


# # If we can use function
# a = [1, 3, 4]
# b = [1, 2, 4]

# a.extend(b)
# a.sort()
# print(a)

# # or

# c = a+b
# c.sort()
# print(c)
