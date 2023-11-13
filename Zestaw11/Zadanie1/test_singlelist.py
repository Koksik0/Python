import unittest
from singlelist import SingleList
from node import Node


class TestSingleList(unittest.TestCase):
    def setUp(self):
        self.list = SingleList(Node(1))

    def test_insert_head(self):
        self.list.insert_head(Node(0))
        self.assertEqual(self.list.head.data, 0)

    def test_insert_tail(self):
        self.list.insert_tail(Node(2))
        self.assertEqual(self.list.tail.data, 2)

    def test_remove_tail(self):
        self.list.insert_head(Node(0))
        self.list.insert_tail(Node(2))
        self.assertEqual(self.list.remove_tail(), Node(2))

    def test_join(self):
        self.list2 = SingleList(Node(10))
        self.list2.insert_tail(Node(11))
        self.list2.insert_tail(Node(12))
        self.list2.insert_tail(Node(13))
        self.list.insert_head(Node(0))
        self.list.insert_tail(Node(2))
        self.list.join(self.list2)
        self.assertEqual(self.list.head, Node(0))
        self.assertEqual(self.list.tail, Node(13))

    def test_clear(self):
        self.list.insert_head(Node(0))
        self.list.insert_tail(Node(2))
        self.list.clear()
        self.assertEqual(self.list.head, None)
        self.assertEqual(self.list.tail, None)
        self.assertEqual(self.list.length, 0)


if __name__ == '__main__':
    unittest.main()
