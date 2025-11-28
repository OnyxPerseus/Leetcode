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
    #find mid position list
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # reverse 2nd part of list
    second = slow.next
    prev = slow.next = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp
    first,second = head,prev
    while second:
        tmp1,tmp2 = first.next,second.next
        second.next = tmp1
        first.next = second
        first = tmp1
        second = tmp2

if __name__ == "__main__":
    arr = [1,2,3,4]
    head =  ListNode()
    initList(arr,head)
    solve(head)
    printList(head)