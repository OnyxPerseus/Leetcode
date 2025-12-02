class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def initList(arr,list):
    for i,x in enumerate(arr):
        list.val = x
        if i < len(arr) - 1:
            list.next = ListNode()
        list = list.next

def printList(list):
    while list and list.val is not None:
        print(list.val,end=',')
        list = list.next

def solve(head,n):
    slow = fast = head
    head = ListNode(next=head)
    for _ in range(n):
        fast = fast.next
    prev = head
    while fast:
        fast = fast.next
        prev = slow    
        slow = slow.next
    prev.next = slow.next
    return head.next

if __name__ == '__main__':
    arr = [1]
    n = 1
    head = ListNode()
    initList(arr,head)
    printList(solve(head,n))