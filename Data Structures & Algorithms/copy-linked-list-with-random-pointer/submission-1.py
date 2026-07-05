"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        otc = collections.defaultdict(lambda: Node(0))
        otc[None] = None
        cur = head

        while cur:
            otc[cur].val = cur.val
            otc[cur].next = otc[cur.next]
            otc[cur].random = otc[cur.random]
            cur = cur.next
        return otc[head]