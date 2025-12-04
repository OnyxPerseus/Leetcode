from collections import defaultdict


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head: Node):
    oldNodeDict = defaultdict(lambda: Node(0))
    oldNodeDict[None] = None
    cur = head
    while cur:
        oldNodeDict[cur].val = cur.val
        oldNodeDict[cur].next = oldNodeDict[cur.next]
        oldNodeDict[cur].random = oldNodeDict[cur.random]
        cur = cur.next
    return oldNodeDict[head]