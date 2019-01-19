""" A minimal singly linked list implementation with insert, delete, and search
    functions.
"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


def search(node, key):
    while node and node.data != key:
        node = node.next

    return node


def insert(node, new_node):
    new_node.next = node.next
    node.next = new_node


def delete(node):
    node.data = node.next.data
    node.next = node.next.next


def delete_kth_last(L, k):
    dummy_head = Node(0, L)
    first = dummy_head.next

    for _ in range(k):
        first = first.next

    second = dummy_head

    while first:
        first, second = first.next, second.next

    second.next = second.next.next

    return dummy_head.next
