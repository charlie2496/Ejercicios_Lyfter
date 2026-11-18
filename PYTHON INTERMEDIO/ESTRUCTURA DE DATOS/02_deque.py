class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class deque:
    head: Node

    def __init__(self, head=None):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def push_left(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def push_right(self, new_node):
        current_node = self.head

        if current_node is None:
            self.head = new_node
            return

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node
        new_node.next = None

    def pop_left(self):
        if self.head:
            self.head = self.head.next

    def pop_right(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        current_node = self.head

        while current_node.next.next is not None:
            current_node = current_node.next

        current_node.next = None

first_node = Node("Hola")
my_deque = deque(first_node)
# my_deque.print_structure()

second_node = Node("Mundo")
my_deque.push_left(second_node)

third_node = Node("third")
my_deque.push_right(third_node)

forth = Node("forth")
my_deque.push_right(forth)

my_deque.print_structure()

print("POP")

my_deque.pop_left()
my_deque.print_structure()

print("POP")

my_deque.pop_right()
my_deque.print_structure()

print("POP")

my_deque.pop_right()
my_deque.print_structure()

print("POP")

my_deque.pop_right()
my_deque.print_structure()