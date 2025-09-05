class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Merge two sorted linked lists into a single sorted linked list.
    """
    dummy = ListNode(-1)  # nodo inicial ficticio
    current = dummy

    # Mientras ambas listas tengan nodos
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Conectar la lista restante (si hay)
    current.next = l1 if l1 else l2

    return dummy.next


def print_list(node: ListNode):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


if __name__ == "__main__":
    # Lista 1: 1 -> 2 -> 4
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    # Lista 2: 1 -> 3 -> 4
    l2 = ListNode(1, ListNode(3, ListNode(4)))

    merged = merge_two_lists(l1, l2)
    print_list(merged)  # 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None
