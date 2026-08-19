class MyLinkedList:
    """
    Doubly Linked List with deque-style operations
    """
    class _Node:
        def __init__(self, element):

             # initializer:
            self.element = element
            self.prev = None
            self.next = None

    def __init__(self):
        """
        Constructs an empty list.
        """
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        """
        Returns True if this list contains no elements.
        """
        return self._size == 0

    def _node_at(self, index):
        p = self._head
        for _ in range(index):
            p = p.next
        return p

    def get(self, index):
        """
        Returns the element at the specified position.
        """
        if index < 0 or index >= self._size:
            raise IndexError(f"Index: {index}, list size: {self._size}")
        return self._node_at(index).element

    def set(self, index, element):
        """
        Replaces the element at the specified position, returning the old value.
        """
        if index < 0 or index >= self._size:
            raise IndexError(f"Index: {index}, list size: {self._size}")
        p = self._node_at(index)
        old_element = p.element
        p.element = element
        return old_element

    def __getitem__(self, index):
        return self.get(index)

    def __setitem__(self, index, element):
        self.set(index, element)

    def append(self, element):
        """
        Adds element to the right side of the list.
        """
        n = MyLinkedList._Node(element)
        if self._tail is None:
            self._head = self._tail = n
        else:
            n.prev = self._tail
            self._tail.next = n
            self._tail = n
        self._size += 1

    def appendleft(self, element):
        """
        Adds element to the left side of the list.
        """
        n = MyLinkedList._Node(element)
        if self._head is None:
            self._head = self._tail = n
        else:
            n.next = self._head
            self._head.prev = n
            self._head = n
        self._size += 1

    def pop(self):
        """
        Removes and returns an element from the right side of the list.
        """
        if self._tail is None:
            raise IndexError("Pop from an empty list")
        n = self._tail
        self._tail = n.prev
        if self._tail is None:
            self._head = None
        else:
            self._tail.next = None
        self._size -= 1
        return n.element

    def popleft(self):
        """
        Removes and returns an element from the left side of the list.
        """
        if self._head is None:
            raise IndexError("Pop from an empty list")
        n = self._head
        self._head = n.next
        if self._head is None:
            self._tail = None
        else:
            self._head.prev = None
        self._size -= 1
        return n.element


    def rotate(self, n=1):
        """
        Rotates the elements n steps to the right (or left is n is negative).
        """
        if self._size < 2 or n == 0:
            return
        n %= self._size
        if n == 0:
            return
        # Move the last n elements to the front.
        # Find the new tail: the node at position (size - n - 1)
        new_tail = self._node_at(self._size - n - 1)
        new_head = new_tail.next

        #Break the chain between new_tail and new_head
        new_tail.next = new_head.prev = None

        #Attach the old head after the old tail
        self._tail.next = self._head
        self._head.prev = new_tail

        #Update the head and tail pointers
        self._head = new_head
        self._tail = new_tail

    def clear(self, size):
        self._head = self._tail = None
        size._size = 0

    def __iter__(self):
        current = self._head
        while current is not None:
            yield current.element
            current = current.next

    def __repr__(self):
        return f"MyLinkedList({', '.join(repr(x) for x in self)})"

if __name__ == "__main__":
    my_list = MyLinkedList()
    for i in range(5):
        my_list.append(i)
    print(my_list)
    my_list[2] = 99
    print(my_list)
    print(my_list[2])
    print(my_list.popleft())
    print(my_list.pop())
    my_list.appendleft(67)
    my_list.append(12345)
    print(my_list)


