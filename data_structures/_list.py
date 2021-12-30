from typing import Any
from ._node import Node
from ._base_classes import LADT

class LinkedList(LADT):
    """
    A double-ended list of elements that uses node logic to store it's items.

    Regarding the node logic, given a node x, it's left node is before x in the
    list, while the right node is after it.
    """

    def __init__(self):
        self._size = 0
        self._first = self._last = None

    def __setitem__(self, index, element):
        if index >= len(self):
            raise IndexError('list assignment index out of range')
        
        current_node = self._first

        for i in range(index):
            current_node = current_node.right
        
        current_node.data = element

    def append(self, element: Any) -> None:
        """
        Appends element to the end of the list.
        """
        new_last = Node(element)
        
        if self.empty():
            self._first = self._last = new_last
        else:
            new_last.left = self._last
            self._last.right = new_last
            self._last = new_last

        self._size += 1

    def insert(self, index: int, element: Any) -> None:
        """
        Inserts element before index.
        """
        if index >= len(self):
            self.append(element)
        else:
            new_node = Node(element)
            node_after = self._traverse(index)
            node_before = node_after.left

            node_after.left = new_node
            new_node.right = node_after
            if node_before:
                node_before.right = new_node
                new_node.left = node_before
            else:
                self._first = new_node
        
        self._size += 1

    def pop(self, index: int = -1) -> Any:
        """
        Removes and returns item at index (default last).

        Raises IndexError if list is empty or index is out of range.
        """
        if index >= len(self):
            raise IndexError('pop from empty list')
        else:
            removed_node = self._traverse(index)
            data = removed_node.data

            before_removed = removed_node.left
            after_removed = removed_node.right

            if before_removed:
                before_removed.right = after_removed
            if after_removed:
                after_removed.left = before_removed
            if removed_node is self._first:
                self._first = after_removed
            if removed_node is self._last:
                self._last = before_removed

        self._size -= 1

        return data

    def index(self, element: Any) -> int:
        """
        Returns first index of element.

        Raises ValueError if the element is not present.
        """
        if element not in self:
            raise ValueError(f"'{element}' is not in list")
        
        for i, current_element in enumerate(self):
            if current_element == element:
                return i

    def count(self, element: Any) -> int:
        """
        Returns number of occurences of element.
        """
        if self.empty():
            return 0
        
        total = 0

        for i in self:
            if i == element:
                total += 1
        
        return total