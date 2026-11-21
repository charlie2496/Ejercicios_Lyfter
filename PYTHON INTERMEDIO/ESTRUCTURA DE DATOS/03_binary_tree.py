
class Node:
    data: str
    left: "Node"
    right: "Node"

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    root: Node

    def __init__(self, root=None):
        self.root = root

    def print_structure(self, current_node=None, depth=0, side="root"):
        if depth == 0 and current_node is None:
            current_node = self.root

        if current_node is None:
            return

        print("    " * depth + side + ": " + current_node.data)

        self.print_structure(current_node.left, depth + 1, "left")
        self.print_structure(current_node.right, depth + 1, "right")


first_node = Node("A")
second_node = Node("B")
third_node = Node("C")
fourth_node = Node("D")
fifth_node = Node("E")

first_node.left = second_node
first_node.right = third_node

second_node.left = fourth_node
second_node.right = fifth_node

my_tree = BinaryTree(first_node)

my_tree.print_structure()
