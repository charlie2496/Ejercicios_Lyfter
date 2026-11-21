class Node:
    data: str
    next: "Node"
    prev: "Node"

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Deque:
    head: Node
    tail: Node

    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def print_structure(self):
        if self.head is None:
            print("Deque is empty")
            return
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def push_left(self, new_node):
        new_node.prev = None
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def push_right(self, new_node):
        new_node.next = None
        new_node.prev = self.tail
        if self.tail is not None:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def pop_left(self):
        if self.head is None:
            return None
        
        removed_node = self.head
        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        removed_node.next = None
        return removed_node


    def pop_right(self):
        if self.tail is None:
            return None

        removed_node = self.tail
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None

        removed_node.prev = None
        return removed_node
    
if __name__ == "__main__":
        
    first_node = Node("Hola")
    my_deque = Deque(first_node)
    # my_deque.print_structure()

    second_node = Node("word")
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

