import unittest

from linkedlist import *


class LinkedListTest(unittest.TestCase):
    def setUp(self):
        self.linkedList = LinkedList()

    def test_initialised_empty(self):
        self.assertEqual(self.linkedList.is_empty(), True)

    def test_insert_elem(self):
        self.linkedList.insert_to_tail(5)
        return_list = [x for x in self.linkedList.__iter__()]
        self.assertEquals(return_list, [5])

    def test_multiple_insert(self):
        test_items = [5, 10, 15]
        for i in test_items:
            self.linkedList.insert_to_tail(i)
        return_list = [x for x in self.linkedList.__iter__()]
        self.assertEquals(return_list, test_items)

    def test_get_from_empty_list(self):
        self.assertEquals(self.linkedList.get_item(1), None)

    def test_get_item_not_in_list(self):
        test_items = [5, 10, 15]
        for i in test_items:
            self.linkedList.insert_to_tail(i)
        self.assertEquals(self.linkedList.get_item(20), None)

    def test_get_item_in_list(self):
        test_list = [5, 10, 15]
        for i in test_list:
            self.linkedList.insert_to_tail(i)
        self.assertEquals(self.linkedList.get_item(15), 15)

    def test_insert_to_position(self):
        test_list = [5, 15, 10]
        self.linkedList.insert_to_pos(15, 15)
        self.linkedList.insert_to_pos(10, 10)
        self.linkedList.insert_to_pos(5)
        return_list = [x for x in self.linkedList.__iter__()]
        self.assertEquals(return_list, test_list, None)

    def test_deletion(self):
        test_items = [5, 10, 15, 20, 25, 30]
        for i in test_items:
            self.linkedList.insert_to_tail(i)
        self.linkedList.delete_from_pos()
        self.linkedList.delete_from_pos()
        return_list = [x for x in self.linkedList.__iter__()]
        self.assertEquals(return_list, test_items[2:])
        self.linkedList.delete_from_pos(2)
        return_list = [x for x in self.linkedList.__iter__()]
        self.assertEquals(return_list, [15, 20, 30])
