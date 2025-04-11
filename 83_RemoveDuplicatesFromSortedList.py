# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head:ListNode):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    current = head

    while current and current.next != None:

        if current.val == current.next.val:
            #remove next from list
            current.next = current.next.next
        else:
            current = current.next

    return head

def printList(head:ListNode):
    current = head
    while current.next != None:
        print(current.val)
        current = current.next
    
    print(current.val)
    print()


head = ListNode(1,ListNode(1,ListNode(1)))

# printList(head)
printList(deleteDuplicates(head))