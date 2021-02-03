# LeetCode February Coding Challenge 2021 # 3: Trim a Binary Search Tree

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

 

# Example 1:


# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Example 2:


# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:


# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
 

# Constraints:

# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.
 

# Follow up: Can you solve it using O(1) (i.e. constant) memory?


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if(head == None or head.next == None):
            return False
        p1 = head.next
        p2  = head.next.next

        while(p1 != None and p2 != None and p1.next != None and p2.next != None and p2.next.next != None and p1 != p2):
            p1 = p1.next
            p2 = p2.next.next
        if(p1 == p2):
            return True
        else:
            return False

s = Solution()

# head = ListNode(3)
# head.next = ListNode(2)
# head.next.next = ListNode(0)
# head.next.next.next = ListNode(-4)
# head.next.next.next.next = head.next
head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = head

print(s.hasCycle(head))
