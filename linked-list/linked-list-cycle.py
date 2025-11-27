class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head):
    fast = head
    while fast and fast.next:
        head = head.next
        fast = fast.next.next
        if head == fast:
            return True
    return False

if __name__ == "__main__":
    a = ListNode(3)
    b = ListNode(-2)
    c = ListNode(-6)
    a.next = b
    b.next = c
    c.next = b
    print(solve(a))