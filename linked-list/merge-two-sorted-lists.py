class ListNode:
    def __init__(self, val=0, next=None):
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

def solve(list1,list2):
    l = ListNode()
    head = l
    while list1 or list2:
        if not list2 or (list1 and list1.val < list2.val):
            l.next = list1
            list1 = list1.next
        else:
            l.next = list2
            list2 = list2.next
        l = l.next
    return head.next

if __name__ == '__main__':
    arr1 = [1,2,4]
    arr2 = [1,3,4]
    list1 = ListNode()
    list2 = ListNode()
    initList(arr1,list1)
    initList(arr2,list2)
    printList(solve(list1,list2))
