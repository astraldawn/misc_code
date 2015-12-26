# Chapter 2 - Linked lists
# Additional questions
#   - Trees and graphs 4.4
#   - Object-oriented design 8.10
#   - Scalability 10.7
#   - Moderate 17.13


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def get_next(self):
        return self.next

    def append(self, value):
        end = Node(value)
        n = self
        while n.next is not None:
            n = n.next
        n.next = end

    # Return the node at the given index
    def get_node(self, index):
        n = self
        for i in range(0, index):
            if n is None:
                return n
            n = n.next
        return n


def print_list(head):
    cur = head
    output = []
    cnt = 0
    while cur is not None and cnt < 100:
        output.append(cur.value)
        cur = cur.get_next()
        cnt += 1
    print output


def create_list():
    items = [7, 20, 9, 8, 4, 1, 15, 12]
    head = Node(6)
    for item in items:
        head.append(item)
    return head


# 2.1 Write code to remove duplicates from an unsorted linked list
# Follow-up: How to solve the problem if a temporary buffer is not allowed

# This solution assumes the existence of a buffer
# O(N) space, O(N) time
def one(head):
    seen = {}
    cur = head
    prev = None
    while cur is not None:
        if cur.value in seen:
            prev.next = cur.next
        else:
            seen[cur.value] = 1
            prev = cur
        cur = cur.next
    return head


# This solution makes use of a runner
# O(1) space, O(N^2) time
def one_followup(head):
    cur = head
    while cur is not None:
        runner = cur
        while runner.next is not None:
            if runner.next.value == cur.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        cur = cur.next
    return head


def test_one():
    head = Node(3)
    head.append(2)
    head.append(3)
    head.append(2)
    head.append(1)
    head.append(2)
    # head = one(head)
    head = one_followup(head)
    print_list(head)


# 2.2 Implement an algorithm to find the k-th to last element of a singly
# linked list
#
# The solution is trivial if the length of list is known.
#
# In the solutions, the 0-th to last element is the last element in the LL
#
# This is the recursive solution. It works by passing a counter back upward.
# However, the recursive calls require O(N) space
def two_recursive(head, k):
    if head is None:
        return -1
    i = two_recursive(head.next, k) + 1
    if i == k:
        print head.value
    return i


# This solution is a nice iterative answer
def two_iterative(head, k):
    p1 = head
    p2 = head

    # Move p1 k spaces ahead of p2
    for i in range(0, k):
        if p1 is None:
            return -1
        p1 = p1.next

    if p1 is None:
        return -1

    # Then run through the list per normal
    while p1.next is not None:
        p1 = p1.next
        p2 = p2.next

    return p2.value


def test_two():
    head = Node(0)
    for i in range(1, 10):
        head.append(i)
    print_list(head)
    two_recursive(head, 8)


# 2.3 Implement an algorithm to delete a node in the middle of a singly
# linked list, given only access to that node
# Eg. given node c from a -> b -> c -> d -> e
# Res: nothing is returned by the new linked list looks like a -> b -> d -> e
#
# This is one the few questions where edge cases are important. If the node
# isn't initialised or the node is at the end of the list
def three(node):
    # Failure conditions
    if node is None or node.next is None:
        return -1

    # Replace the current node with the next node
    next_node = node.next
    node.value = next_node.value
    node.next = next_node.next


def test_three():
    head = create_list()
    cur_node = head.get_node(2)
    three(cur_node)
    print_list(head)


# 2.4 Write code to partition a linked list around a value x, such that all
# nodes less than x come before all nodes greater than or equal to x
#
# Split into two linked lists
def four(head, x):
    list_l = None
    list_geq = None
    cur = head
    seen = False
    while cur is not None:
        if cur.value < x:
            if list_l is None:
                list_l = Node(cur.value)
            else:
                list_l.append(cur.value)
        else:
            if cur.value == x and not seen:
                seen = True
            else:
                if list_geq is None:
                    list_geq = Node(cur.value)
                else:
                    list_geq.append(cur.value)
        cur = cur.next

    list_l.append(x)

    # Merge the two lists
    cur = list_l
    while list_l is not None and list_l.next is not None:
        list_l = list_l.next

    list_l.next = list_geq
    return cur


def test_four():
    head = create_list()
    head.append(8)
    head.append(8)
    res = four(head, 8)
    print_list(head)
    print_list(res)


# 2.5 You have two numbers represented by a linked list, where each node
# contains a single digit. The digits are stored in reverse order, such that
# the 1's digit is at the head of the list. Write a function that adds the
# two numbers together and returns the sum as a linked list
#
# Example
# IN: (7 -> 1 -> 6) + (5 -> 9 -> 2). 617 + 295
# OUT: 2 -> 1 -> 9. 912
#
# Follow up: Supposed the digits are stored in forward order.
# IN: 6 -> 1 -> 7 + 2 -> 9 -> 5
# OUT: 9 -> 1 -> 2

# 2.6 Given a circular linked list, implement an algorithm which returns the
# node at the beginning of the loop.
#
# A circular linked is a linked list in which a node's next pointer points to
# an earlier node, so as to make a loop in the linked list
#
# Example
# IN: A -> B -> C -> D -> E -> C
# OUT: C

# Use two pointers, one that is fast and one that is slow.
# Fast pointer moves at twice the speed of the slow pointer
def six(head):
    slow = head
    fast = head

    # Find the meeting point. This will be at LOOP_SIZE - k steps into the
    # linked list
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # Error checking
    if fast is None or fast.next is None:
        return None

    # Reset the slow pointer and keep the fast pointer where it is. Each of
    # them are k steps from the loop start. If the move at the same pace,
    # they must meet at the loop start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return fast


def test_six():
    head = Node('A')
    n1 = Node('B')
    n2 = Node('C')
    n3 = Node('D')
    n4 = Node('E')
    head.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2
    print six(head).value


# 2.7 Implement a function to check if a linked list is a palindrome
#
# Again using the fast / slow runner concept. Use a fast runner to reach the
# end of the LL. Then the slow runner will be halfway through the LL. Store
# the stuff that has already been seen into the stack. Alternatives include
# reversing the linked list and checking if the 2 lists are identical
def seven(head):
    slow = head
    fast = head
    stack = []

    while fast is not None and fast.next is not None:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    # Odd number of elements, skip the middle
    if fast is not None:
        slow = slow.next

    while slow is not None:
        if slow.value != stack.pop():
            return False
        slow = slow.next

    return True


def test_seven():
    head = Node(1)
    head.append(2)
    head.append(3)
    head.append(3)
    head.append(2)
    head.append(1)
    print seven(head)  # Expect true
    head.append(1)
    print seven(head)  # Expect false
