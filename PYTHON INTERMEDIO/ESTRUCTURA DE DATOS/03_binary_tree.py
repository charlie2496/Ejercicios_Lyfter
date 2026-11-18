
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

    def print_structure(self, current_node):
        if current_node is None:
            return

        print(current_node.data)

        self.print_structure(current_node.left)
        self.print_structure(current_node.right)


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

my_tree.print_structure(my_tree.root)
