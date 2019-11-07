"""
A class to store the representation of a Phylogenetic Tree.
"""
class Node:
    def __init__(self, left=None, right=None, other=None):
        self.left = left
        self.right = right
        self.other = other
        self.dleft = 0
        self.dright = 0
        self.dother = 0
        self.visited = False

class Leaf(Node):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
