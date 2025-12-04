from IRedBlackTree import IRedBlackTree, INode
from typing import Optional, cast, Any


class Node(INode):
    def __init__(self, parent, leftChild, rightChild, value: Any, nil) -> None:
        self.color: str = "RED"
        self.parent: INode = parent
        self.leftChild: INode = leftChild
        self.rightChild: INode = rightChild
        self.value: Any = value
        self.nil = nil
    
    # Returns the parents parent
    def grandparent(self) -> INode:
        if self.parent is None or self.parent is self.nil:
            return self.nil
        return self.parent.parent
    
    # Finds and returns the parents other child
    def sibling(self) -> INode:
        if self.parent is self.nil:
            return self.nil
        if self == self.parent.leftChild:
            return self.parent.rightChild
        else:
            return self.parent.leftChild





class RedBlackTree(IRedBlackTree):
    def __init__(self, value: Optional[Any]) -> None:

        # Creation of the nil node
        self.nil: INode = cast(INode, Node(None, None, None, 0, None))
        self.nil.leftChild = self.nil
        self.nil.rightChild = self.nil
        self.nil.parent = self.nil
        self.nil.color = "BLACK"
        self.nil.nil = self.nil
        self.root: INode = self.nil
        if value != None:
            self.root = Node(self.nil, self.nil, self.nil, value, self.nil)
            self.root.color = "BLACK"


    def insert(self, value: Any) -> None:
        newNode = Node(self.nil, self.nil, self.nil, value, self.nil)
        if self.root == self.nil:
            self.root = newNode
        else:
            node = self.root
            parent = self.root
            while node != self.nil:
                parent = node
                if value < node.value:
                    node = node.leftChild
                else:
                    node = node.rightChild
            newNode.parent = parent
            if newNode.value < parent.value:
                parent.leftChild = newNode
            else:
                parent.rightChild = newNode

        # Insertion fixups
        while newNode.parent.color == "RED":
            if newNode.parent == newNode.grandparent().leftChild:
                nodeX = newNode.grandparent().rightChild
                if nodeX.color == "RED":
                    newNode.parent.color = "BLACK"
                    nodeX.color = "BLACK"
                    newNode.grandparent().color = "RED"
                    newNode = newNode.grandparent()
                else: 
                    if newNode == newNode.parent.rightChild:
                        newNode = newNode.parent
                        self.left_rotate(newNode)
                    newNode.parent.color = "BLACK"
                    newNode.grandparent().color = "RED"
                    self.right_rotate(newNode.grandparent())
            else:
                nodeX = newNode.grandparent().leftChild
                if nodeX.color == "RED":
                    newNode.parent.color = "BLACK"
                    nodeX.color = "BLACK"
                    newNode.grandparent().color = "RED"
                    newNode = newNode.grandparent()
                else: 
                    if newNode == newNode.parent.leftChild:
                        newNode = newNode.parent
                        self.right_rotate(newNode)
                    newNode.parent.color = "BLACK"
                    newNode.grandparent().color = "RED"
                    self.left_rotate(newNode.grandparent())
            if newNode == self.root:
                break
        self.root.color = "BLACK"

        

    def search(self, value: Any) -> INode:
        node = self.root
        while node != self.nil and value != node.value:
            if value < node.value:
                node = node.leftChild
            else:
                node = node.rightChild
        return node

    def remove(self, node: INode) -> None:
        replacingNode = None
        og_color = node.color
        if node.leftChild == self.nil and node.rightChild != self.nil:
            replacingNode = node.rightChild
            self.transplant(node, replacingNode)
        elif node.rightChild == self.nil and node.leftChild != self.nil:
            replacingNode = node.leftChild
            self.transplant(node, replacingNode)
        else:
            replacingChild = self.find_min(node.rightChild)
            og_color = replacingChild.color
            replacingNode = replacingChild.rightChild
            if replacingChild.parent == node:
                replacingNode.parent = replacingChild
            else:
                self.transplant(replacingChild, replacingChild.rightChild)
                replacingChild.rightChild = node.rightChild
                replacingChild.rightChild.parent = replacingChild
            self.transplant(node, replacingChild)
            replacingChild.leftChild = node.leftChild
            if node.rightChild != self.nil:
                node.rightChild.parent = replacingChild
        
        # Removal fixups
        if og_color == "BLACK":
            while replacingNode != self.root and replacingNode.color == "BLACK":
                if replacingNode == replacingNode.parent.leftChild:
                    nodeX = replacingNode.parent.rightChild
                    if nodeX.color == "RED":
                        nodeX.color = "BLACK"
                        replacingNode.parent.color = "RED"
                        self.left_rotate(replacingNode.parent)
                        nodeX = replacingNode.parent.rightChild
                    if nodeX.leftChild.color == "BLACK" and nodeX.rightChild.color == "BLACK":
                        nodeX.color = "RED"
                        replacingNode = replacingNode.parent
                    else:
                        if nodeX.rightChild.color == "BLACK":
                            nodeX.leftChild.color = "BLACK"
                            nodeX.color = "RED"
                            self.right_rotate(nodeX)
                            nodeX = replacingNode.parent.rightChild
                        nodeX.color = replacingNode.parent.color
                        replacingNode.parent.color = "BLACK"
                        nodeX.rightChild.color = "BLACK"
                        self.left_rotate(replacingNode.parent)
                        replacingNode = self.root
                else:
                    nodeX = replacingNode.parent.leftChild
                    if nodeX.color == "RED":
                        nodeX.color = "BLACK"
                        replacingNode.parent.color = "RED"
                        self.right_rotate(replacingNode.parent)
                        nodeX = replacingNode.parent.leftChild
                    if nodeX.leftChild.color == "BLACK" and nodeX.rightChild.color == "BLACK":
                        nodeX.color = "RED"
                        replacingNode = replacingNode.parent
                    else:
                        if nodeX.rightChild.color == "BLACK":
                            nodeX.leftChild.color = "BLACK"
                            nodeX.color = "RED"
                            self.left_rotate(nodeX)
                            nodeX = replacingNode.parent.leftChild
                        nodeX.color = replacingNode.parent.color
                        replacingNode.parent.color = "BLACK"
                        nodeX.leftChild.color = "BLACK"
                        self.right_rotate(replacingNode.parent)
                        replacingNode = self.root

            replacingNode.color = "BLACK"



    def transplant(self, node: INode, replacingNode: INode) -> None:
        if node == self.root:
                self.root = replacingNode
        elif node.parent.leftChild == node:
            node.parent.leftChild = replacingNode
        else:
            node.parent.rightChild = replacingNode
        replacingNode.parent = node.parent

    def find_min(self, node: INode) -> INode:
        while node.leftChild != self.nil:
            node = node.leftChild
        return node

    def left_rotate(self, node: INode) -> None:
        nodeX = node.rightChild
        node.rightChild = nodeX.leftChild
        if nodeX.leftChild != self.nil:
            nodeX.leftChild.parent = node
        nodeX.parent = node.parent
        if node.parent == self.nil:
            self.root = nodeX
        elif node == node.parent.leftChild:
            node.parent.leftChild = nodeX
        else:
            node.parent.rightChild = nodeX
        nodeX.leftChild = node
        node.parent = nodeX

    def right_rotate(self, node: INode) -> None:
        nodeX = node.leftChild
        node.leftChild = nodeX.rightChild
        if nodeX.rightChild != self.nil:
            nodeX.rightChild.parent = node
        nodeX.parent = node.parent
        if node.parent == self.nil:
            self.root = nodeX
        elif node == node.parent.rightChild:
            node.parent.rightChild = nodeX
        else:
            node.parent.leftChild = nodeX
        nodeX.rightChild = node
        node.parent = nodeX

    def print_tree(self, node=None, prefix="", is_left=True):
        if node is None:
            node = self.root
        if node == self.nil:
            return

        if node.rightChild != self.nil:
            self.print_tree(node.rightChild, prefix + ("      " if is_left else "│     "), False)

        print(prefix + ("└── " if is_left else "┌── ") + f"{node.value}({'B' if node.color=='BLACK' else 'R'})")

        if node.leftChild != self.nil:
            self.print_tree(node.leftChild, prefix + ("      " if is_left else "│     "), True)