from typing import Protocol, Any


class INode(Protocol):
    color: str
    value: Any
    parent: "INode"
    leftChild: "INode"
    rightChild: "INode"
    nil: "INode"

    def grandparent(self) -> "INode":
        """
        Gets and returns the grandparent node
        O(1) time complexity 
        O(1) space complexity
        """
        ...

    def sibling(self) -> "INode":
        """
        Gets and returns the sibling node
        O(1) time complexity 
        O(1) space complexity
        """
        ...

class IRedBlackTree(Protocol):
    root: INode
    nil: INode

    def insert(self, value: Any) -> None:
        """
        Insert a value into the tree
        O(log n) time complexity 
        O(1) space complexity
        """
        ...

    def search(self, value: Any) -> INode:
        """
        Check if a value exists in the tree
        O(log n) time complexity 
        O(1) space complexity
        """
        ...

    def remove(self, node: INode) -> None:
        """
        Remove a node from the tree
        O(log n) time complexity 
        O(1) space complexity
        """
        ...

    def find_min(self, node: INode) -> INode:
        """
        Find the smallest descendant of a node
        O(log n) time complexity 
        O(1) space complexity
        """
        ...

    def transplant(self, node: INode, replacingNode: INode):
        """
        Replace a node with another node
        O(1) time complexity 
        O(1) space complexity
        """
        ...

    def left_rotate(self, node: INode) -> None:
        """
        Perform a left rotation on the tree
        O(1) time complexity 
        O(1) space complexity
        """
        ...

    def right_rotate(self, node: INode) -> None:
        """
        Perform a right rotation on the tree
        O(1) time complexity 
        O(1) space complexity
        """
        ...

    def print_tree(self, node: INode, indent = "", last=True) -> None:
        """
        Prints the tree out to the console
        O(n) time complexity 
        O(log n) space complexity
        """