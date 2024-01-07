from node import Node


class SingleList:
    def __init__(self, first_element: Node):
        self.head = first_element
        self.tail = first_element
        self.length = 1

    def insert_head(self, new_node: Node):
        temp = self.head
        self.head = new_node
        self.head.next = temp

    def insert_tail(self, new_element: Node):
        if self.length == 1:
            self.head.next = new_element
            self.tail = new_element
            self.length += 1
        else:
            self.tail.next = new_element
            self.tail = new_element
            self.length += 1

    def print_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def remove_tail(self) -> Node:
        if self.head is None:
            raise ValueError("Error: The list is empty.")
        result = self.tail
        self.length -= 1

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            node = self.head
            current = None
            while node.next is not None:
                current = node
                node = node.next
            current.next = None
            self.tail = current
        return result

    def join(self, other):
        if not self.head and not other.head:
            pass
        elif not self.head:
            self.head = other.head
            self.tail = other.tail
        elif other.head:
            self.tail.next = other.head
            self.tail = other.tail
        other.clear()

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0