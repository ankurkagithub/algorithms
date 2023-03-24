class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return f"{self.data}"

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def insert(self, data, index):
        node = Node(data)
        current = self.head
        last_node = None
        position = 0

        if index == 0:
            node.next = self.head
            self.head = node
            node.previous = last_node
            return

        while position < index:
            position += 1
            last_node = current
            current = current.next
            current.previous = last_node

        node.next = current
        node.previous = last_node
        current.previous = node
        last_node.next = node
        return

    def __repr__(self):
        current = self.head
        output = []    print(dll)

        while current:    print(dll)

            if current is self.head:
                output.append(f"Head: {current} ")
            elif current.next is None:
                output.append(f" Tail: {current} ")
            else:
                output.append(f" {current} ")
            current = current.next
        return "<->".join(output)

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert(8,0)
    dll.insert(9,0)
    dll.insert(5,0)
    dll.insert(10,0)
    dll.insert("ankur",0)
    print(f"Before: {dll}")
    dll.insert(1000,2)
    print(f"After: {dll}")
