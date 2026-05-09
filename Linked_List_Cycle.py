# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


# Function to detect cycle in linked list
def hasCycle(head):
    slow = head
    fast = head

    # Move slow by 1 step and fast by 2 steps
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # If both pointers meet, cycle exists
        if slow == fast:
            return True

    return False


# Creating linked list: 3 -> 2 -> 0 -> -4
head = ListNode(3)
second = ListNode(2)
third = ListNode(0)
fourth = ListNode(-4)

head.next = second
second.next = third
third.next = fourth

# Creating cycle: -4 -> 2
fourth.next = second

# Check cycle
if hasCycle(head):
    print("true")
else:
    print("false")