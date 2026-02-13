# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = ListNode(0)
        current = dummy

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


# ---------- Helper functions for testing ----------

# Convert list → linked list
def build_list(nums):
    dummy = ListNode()
    cur = dummy
    for n in nums:
        cur.next = ListNode(n)
        cur = cur.next
    return dummy.next


# Print linked list
def print_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "")
        node = node.next
    print()


# ---------- Test ----------
l1 = build_list([1, 2, 3])
l2 = build_list([4, 5, 6])

sol = Solution()
result = sol.addTwoNumbers(l1, l2)

print_list(result)
