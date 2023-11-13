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
        result = self.tail
        self.length -= 1
        node = self.head
        current = None
        while node.next is not None:
            current = node
            node = node.next
        if current is None:
            raise ValueError("Error")
        current.next = None
        self.tail = current
        return result

    def join(self, other):
        temp = other.tail
        self.tail.next = other.head
        self.tail = temp
        other.clear()

    def clear(self):
        current = self.head
        while current:
            next_node = current.next
            del current
            current = next_node

        self.head = None
        self.tail = None
        self.length = 0
