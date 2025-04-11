# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd( head, n):

    """
    :type head: Optional[ListNode]
    :type n: int
    :rtype: Optional[ListNode]
    """
    previous = ListNode()
    current = head
    depth = 0

    while current and current.next != None:

        current = current.next
        depth+=1
    
    if depth == 0:
        return ListNode()

    depth = (depth - n) + 1
    current = head

    for i in range(depth):
        previous = current
        current = current.next

    if current.next != None:
        previous.next = current.next
    else:
        previous.next = None
    
    return head




def printList(head:ListNode):
    current = head
    while current.next != None:
        print(current.val)
        current = current.next
    
    print(current.val)
    print()

        
# head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
head = ListNode(1)
head = removeNthFromEnd(head,1)
printList(head)