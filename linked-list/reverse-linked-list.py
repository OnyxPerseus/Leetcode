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

def solve(head):
    last = None
    while head:
        last = ListNode(head.val,last)
        head = head.next
    return last


if __name__ == "__main__":
    data = [1,2,3,4,5]
    head = ListNode(next=ListNode())
    initList(data,head)
    printList(solve(head))