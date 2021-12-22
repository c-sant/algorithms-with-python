from ._base_classes import ADT

class Queue(ADT):
    """
    A linear collection of elements that follows the FIFO (First In, First Out)
    order of operations.
    """

    def __init__(self):
        self._q = []
        super().__init__(self._q)

    @property
    def front(self):
        """
        Element that currently is at the front of the queue.
        """
        if self.empty():
            return None
        
        return self._q[0]

    @property
    def rear(self):
        """
        Element that currently is at the rear of the queue.
        """
        if self.empty():
            return None
        
        return self._q[-1]

    def enqueue(self, element):
        """
        Adds element to the rear of the queue.
        """
        self._q.append(element)

    def dequeue(self):
        """
        Removes and returns the element at the front of the queue.

        Raises IndexError if queue is empty.
        """
        if self.empty():
            raise IndexError('dequeue from empty queue')

        return self._q.pop(0)

    def peek(self):
        """
        Returns the element at the front of the queue.

        Raises IndexError if queue is empty.
        """
        if self.empty():
            raise IndexError('peek from empty queue')
        
        return self._q[0]
