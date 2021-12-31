from ._base_classes import ADT, LADT
from ._node import Node
from typing import Any, Iterable

class Queue(ADT):
    """
    A linear collection of elements that follows the FIFO (First In, First Out)
    order of operations.
    """

    def __init__(self, iterable: Iterable = []) -> None:
        self._q = iterable
        super().__init__(self._q)

    @property
    def front(self) -> Any:
        """
        Element that currently is at the front of the queue.
        """
        if self.empty():
            return None
        
        return self._q[0]

    @property
    def rear(self) -> Any:
        """
        Element that currently is at the rear of the queue.
        """
        if self.empty():
            return None
        
        return self._q[-1]

    def enqueue(self, element: Any) -> None:
        """
        Adds element to the rear of the queue.
        """
        self._q.append(element)

    def dequeue(self) -> Any:
        """
        Removes and returns the element at the front of the queue.

        Raises IndexError if queue is empty.
        """
        if self.empty():
            raise IndexError('dequeue from empty queue')

        return self._q.pop(0)

    def peek(self) -> Any:
        """
        Returns the element at the front of the queue.

        Raises IndexError if queue is empty.
        """
        if self.empty():
            raise IndexError('peek from empty queue')
        
        return self._q[0]



class LinkedQueue(LADT):
    """
    A linear collection of elements that follows the FIFO (First In, First Out)
    order of operations. The linked queue doesn't rely on arrays, but rather on
    nodes. The first element is at the front of the queue, while the last is at
    the rear.

    Regarding the node logic, given a node x, it's left node is before x in the
    queue, while the right node is after it.
    """

    def __init__(self, iterable: Iterable = []) -> None:
        self._size = 0
        self._first = self._last = None

        for element in iterable:
            self.enqueue(element)

    @property
    def front(self) -> Any:
        """
        Element that currently is at the front of the queue.
        """
        return self._first.data

    @property
    def rear(self)-> Any:
        """
        Element that currently is at the rear of the queue.
        """
        return self._last.data

    def enqueue(self, element: Any) -> None:
        """
        Adds element to the rear of the queue.
        """

        new_rear = Node(element)

        if self.empty():
            self._first = self._last = new_rear
        else:
            self._last.right = new_rear
            new_rear.left = self._last
            self._last = new_rear

        self._size += 1

    def dequeue(self) -> Any:
        """
        Removes and returns the element at the front of the queue.

        Raises IndexError if queue is empty.
        """
        if self.empty():
            raise IndexError('dequeue from empty queue')

        data = self._first.data

        if len(self) == 1:
            self._first = self._last = None
        else:
            new_first = self._first.right
            new_first.left = self._first.right = None
            self._first = new_first

        self._size -= 1

        return data

    def peek(self) -> Any:
        """
        Returns the element at the front of the queue.

        Raises IndexError if queue is empty.
        """
        if self.empty():
            raise IndexError('peek from empty queue')

        return self._first.data