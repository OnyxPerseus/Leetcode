class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        return self.devide(lists,0,len(lists) - 1)
        
    def devide(self,lists,l,r):
        if l > r:
            return None
        if l == r:
            return lists[l]
        mid = (l+r)//2
        left = self.devide(lists,l,mid)
        right = self.devide(lists,mid+1,r)
        return self.merge(left,right)

    def merge(self,l1,l2):
        dummy = h = ListNode()
        while l1 or l2:
            if not l2 or (l1 and l1.val < l2.val):
                h.next = l1
                l1 = l1.next
            else:
                h.next = l2
                l2 = l2.next
            h = h.next
        return dummy.next

                    