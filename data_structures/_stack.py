from ._base_classes import ADT, LADT
from ._node import Node

class Stack(ADT):
    """
    A linear collection of elements that follows the LIFO (Last In, First Out)
    order of operations.

    It may have a capacity which cannot be surpassed, but setting it to 
    ``None`` will make the stack limitless.
    """

    def __init__(self, capacity: int = None):
        self._capacity = capacity
        self._s = []
        super().__init__(self._s)

    @property
    def capacity(self):
        """
        Maximum amount of elements the stack can have.
        """
        return self._capacity

    @property
    def top(self):
        """
        Element that currently is at the top of the stack.
        """
        if self.empty():
            return None

        return self._s[0]

    def full(self):
        """
        Returns True if number of elements in the stack are the same value as
        it's capacity; otherwise, returns False.
        """
        if self._capacity == None:
            return False

        return self._capacity == len(self)

    def push(self, element):
        """
        Inserts element at the top of the stack.

        Raises IndexError if stack is already full.
        """
        if self.full():
            raise IndexError('push into full stack')
        
        self._s.insert(0, element)

    def pop(self):
        """
        Removes and returns the element at the top of the stack.

        Raises IndexError if stack is empty.
        """
        if self.empty():
            raise IndexError('pop from empty stack')

        return self._s.pop(0)

    def peek(self):
        """
        Returns the element at the top of the stack.

        Raises IndexError if stack is empty.
        """
        if self.empty():
            raise IndexError('peek from empty stack')
        
        return self._s[0]



class LinkedStack(LADT):
    """
    A linear collection of elements that follows the LIFO (Last In, First Out)
    order of operations. The linked stack doesn't rely on arrays, but rather on
    nodes. 

    It may have a capacity which cannot be surpassed, but setting it to
    ``None`` will make the stack limitless.

    Regarding the nodes, given a node x, it's left node is above x, while the
    right node is below.
    """

    def __init__(self, capacity: int = None):
        self._capacity = capacity
        self._size = 0
        self._top = self._bottom = None
        super().__init__(self._top, self._bottom)

    @property
    def capacity(self):
        """
        Maximum amount of elements the stack can have.
        """
        return self._capacity


    @property
    def top(self):
        """
        Element that currently is at the top of the stack.
        """
        return self._top

    def full(self):
        """
        Returns True if number of elements in the stack are the same value as
        it's capacity; otherwise, returns False.
        """
        if self._capacity == None:
            return False
        
        return self._capacity == len(self)

    def push(self, element):
        """
        Inserts element at the top of the stack.

        Raises IndexError if stack is already full.
        """
        if self.full():
            raise IndexError('push into full stack')
        
        new_top = Node(element)

        if self.empty():
            self._top = self._bottom = new_top
        
        else:
            self._top.left = new_top
            new_top.right = self._top
            self._top = new_top

        self._size += 1

    def pop(self):
        """
        Removes and returns the element at the top of the stack.

        Raises IndexError if stack is empty.
        """
        if self.empty():
            raise IndexError('pop from empty stack')
        elif len(self) == 1:
            self._top = self._bottom = None
        else:
            new_top = self._top.right
            new_top.left = self._top.right = None


        self._size -= 1

    def peek(self):
        """
        Returns the element at the top of the stack.

        Raises IndexError if stack is empty.
        """
        if self.empty():
            raise IndexError

        return self._top
        
