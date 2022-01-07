from abc import ABC
from typing import Any
from ._node import Node


class ADT(ABC):
    """
    Abstract Data Class used as base class for array-based Data Strucutres.
    """

    def __init__(self, array: list) -> None:
        self._array = array

    def __contains__(self, element: Any) -> bool:
        return element in self._array

    def __eq__(self, other) -> bool:
        if type(self) != type(other):
            return False

        return self._array == other._array

    def __len__(self) -> int:
        return len(self._array)

    def __str__(self) -> str:
        return str(self._array)

    def empty(self) -> bool:
        """
        Returns True if the collection is empty; otherwise, returns False.
        """
        return len(self) == 0

    def clear(self) -> None:
        """
        Removes all items from the collection.
        """
        self._array.clear()

    def tolist(self) -> list:
        return self._array.copy()


class LADT(ABC):
    """
    Linked Abstract Data Class used as base class for node-based Data 
    Strucutres.
    """

    def __contains__(self, element: Any) -> bool:
        return element in self.tolist()

    def __eq__(self, other) -> bool:
        if type(self) != type(other):
            return False

        return self.tolist() == other.tolist()

    def __iter__(self):
        current_node = self._first

        while current_node:
            yield current_node.data

            current_node = current_node.right

    def _traverse(self, index: int) -> Node:
        if index < 0:
            index = len(self) - index

        if index >= len(self):
            raise IndexError('index out of range')

        if index < len(self) // 2:
            current_node = self._first

            for i in range(index):
                current_node = current_node.right

            return current_node
        else:
            current_node = self._last

            for i in range(len(self) - index - 1):
                current_node = current_node.left

            return current_node

    def __getitem__(self, index: int) -> Any:
        if index >= len(self):
            raise IndexError('index out of range')

        return list(self)[index]

    def __len__(self) -> int:
        return self._size

    def __str__(self) -> str:
        return str(self.tolist())

    def empty(self) -> bool:
        """
        Returns True if the collection is empty; otherwise, returns False.
        """
        return len(self) == 0

    def clear(self) -> None:
        """
        Removes all items from the collection.
        """
        self._first = self._bottom = None
        self._size = 0

    def tolist(self) -> list:
        """
        Returns the collection in the form of a Python list.
        """
        return list(self)
