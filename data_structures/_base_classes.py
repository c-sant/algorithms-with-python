from abc import ABC

class ADT(ABC):
    """
    Abstract Data Class used as base class for array-based Data Strucutres.
    """

    def __init__(self, array: list):
        self._array = array

    def __contains__(self, element):
        return element in self._array

    def __eq__(self, other):
        if type(self) != type(other):
            return False

        return self._array == other._array

    def __len__(self):
        return len(self._array)

    def __str__(self):
        return str(self._array)

    def empty(self) -> bool:
        """
        Returns True if the collection is empty; otherwise, returns False.
        """
        return len(self) == 0

    def clear(self):
        """
        Removes all items from the collection.
        """
        self._array.clear()

class LADT(ABC):
    """
    Linked Abstract Data Class used as base class for node-based Data 
    Strucutres.
    """

    def __contains__(self, element):
        return element in self.tolist()

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        
        return self.tolist() == other.tolist()

    def __len__(self):
        return self._size

    def __str__(self):
        return str(self.tolist())

    def empty(self):
        """
        Returns True if the collection is empty; otherwise, returns False.
        """
        return len(self) == 0

    def clear(self):
        """
        Removes all items from the collection.
        """
        self._first = self._bottom = None
        self._size = 0

    def tolist(self):
        """
        Returns the collection in the form of a Python list.
        """
        l = []
        
        current_node = self._first

        while current_node:
            l.append(current_node.data)
            current_node = current_node.right
        
        return l