class Node:
    """
    Data container that links itself to other data containers.
    """

    def __init__(self, data, left = None, right = None):
        self.left = left
        self.right = right