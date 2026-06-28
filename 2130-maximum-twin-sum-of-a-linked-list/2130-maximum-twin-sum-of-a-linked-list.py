class Solution:
    def pairSum(self, head):
        slow = fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next

            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        ans = 0
        left, right = prev, slow

        while left:
            ans = max(ans, left.val + right.val)
            left = left.next
            right = right.next

        return ans