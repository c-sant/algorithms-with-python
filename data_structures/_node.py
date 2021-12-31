class Node:
    """
    Data container that links itself to other data containers.
    """

    def __init__(self, data, parent = None, left = None, right = None):
        self.parent = parent
        self.left = left
        self.right = right
        self.data = data