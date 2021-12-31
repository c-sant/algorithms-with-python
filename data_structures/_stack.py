from typing import Any, Iterable, Union
from ._base_classes import ADT, LADT
from ._node import Node

class Stack(ADT):
    """
    A linear collection of elements that follows the LIFO (Last In, First Out)
    order of operations.

    It may have a capacity which cannot be surpassed, but setting it to 
    ``None`` will make the stack limitless.
    """

    def __init__(self, iterable: Iterable = [], capacity: int = None):
        if capacity < len(iterable):
            raise ValueError('push into full stack')
        
        self._capacity = capacity
        self._s = list(reversed(iterable))
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
    nodes. The first element is at the top of the stack, while the last is
    considered to be in the bottom.

    It may have a capacity which cannot be surpassed, but setting it to
    ``None`` will make the stack limitless.

    Regarding the node logic, given a node x, it's left node is above x, while
    the right node is below.
    """

    def __init__(self, iterable: Iterable = [], capacity: int = None) -> None:
        self._capacity = capacity
        self._size = 0
        self._first = self._last = None

        for element in iterable:
            self.push(element)

    @property
    def capacity(self) -> Union[int, None]:
        """
        Maximum amount of elements the stack can have.
        """
        return self._capacity

    @property
    def top(self) -> Any:
        """
        Element that currently is at the top of the stack.
        """
        return self._first.data

    def full(self) -> bool:
        """
        Returns True if number of elements in the stack are the same value as
        it's capacity; otherwise, returns False.
        """
        if self._capacity == None:
            return False
        
        return self._capacity == len(self)

    def push(self, element: Any) -> None:
        """
        Inserts element at the top of the stack.

        Raises IndexError if stack is already full.
        """
        if self.full():
            raise IndexError('push into full stack')
        
        new_top = Node(element)

        if self.empty():
            self._first = self._last = new_top
        
        else:
            self._first.left = new_top
            new_top.right = self._first
            self._first = new_top

        self._size += 1

    def pop(self) -> Any:
        """
        Removes and returns the element at the top of the stack.

        Raises IndexError if stack is empty.
        """
        if self.empty():
            raise IndexError('pop from empty stack')
        
        data = self._first.data

        if len(self) == 1:
            self._first = self._last = None
        else:
            new_top = self._first.right
            new_top.left = self._first.right = None
            self._first = new_top

        self._size -= 1

        return data

    def peek(self) -> Any:
        """
        Returns the element at the top of the stack.

        Raises IndexError if stack is empty.
        """
        if self.empty():
            raise IndexError('peek from empty stack')

        return self._first.data
        
