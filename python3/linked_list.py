""" A linked list implementation with insert, delete, and search functions.
"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def search(node, key):
    while node and node.data != key:
        node = node.next

    return node


def insert(node, new_node):
    new_node.next = node.next
    node.next = new_node


def delete(node):
    node.next = node.next.next
