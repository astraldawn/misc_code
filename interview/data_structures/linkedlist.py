class LinkedListNode(object):
    def __init__(self, item):
        self.value = item
        self.next = None


class LinkedList:
    def __init__(self, item=None):
        self.size = 0
        if item is not None:
            self.head = LinkedListNode(item)
            self.tail = self.head
        else:
            self.head = None
            self.tail = None

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size is 0

    def insert_to_tail(self, item):
        self.size += 1
        if not self.head:
            self.head = LinkedListNode(item)
            self.tail = self.head
        elif self.tail:
            self.tail.next = LinkedListNode(item)
            self.tail = self.tail.next
        else:
            self.tail = LinkedListNode(item)

    def insert_to_pos(self, item, pos=0):
        if pos >= self.size - 1:
            # Insert to the end instead
            self.insert_to_tail(item)
            return

        new_node = LinkedListNode(item)
        self.size += 1
        # Insert to head
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev = self.get_node_at(pos)
            new_node.next = prev.next
            prev.next = new_node

    def delete_from_pos(self, pos=0):
        if pos >= self.size - 1:
            return

        self.size -= 1
        # Delete from head
        if pos == 0:
            self.head = self.head.next
        else:
            cur = self.get_node_at(pos)
            prev = self.get_node_at(pos - 1)
            prev.next = cur.next

    def get_node_at(self, pos):
        cur = self.head
        for i in range(0, pos):
            cur = cur.next
        return cur

    def get_item(self, query):
        if self.is_empty():
            return None
        cur = self.head
        while cur is not None:
            if cur.value == query:
                return query
            cur = cur.next
        return None

    def __iter__(self):
        cursor = self.head
        while cursor:
            yield cursor.value
            cursor = cursor.next
