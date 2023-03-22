class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node: {self.data}"


class LinkedList():
    def __init__(self, head = None):
        self.head = head

    def is_empty(self):
        return self.head is None

    def add(self, data):
        current = Node(data)
        current.next = self.head
        self.head = current

    def size(self):
        current = self.head
        size = 0
        while current:
            current = current.next
            size += 1
        return size

    def insert(self, new_data, index):
        node = Node(new_data)
        current = self.head
        position = 0
        while position < index:
            previous = current
            current = current.next
            position += 1
        previous.next = node
        node.next = current

    def remove(self, data):
        current = self.head
        found = False
        while not found and current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    previous.next = current.next
                found = True
            else:
                previous = current
                current = current.next

    def __repr__(self):
        current = self.head
        output = []
        while current:
            if current is self.head:
                output.append(f"Head: {current.data}")
            elif current.next is None:
                output.append(f"Tail: {current.data}")
            else:
                output.append(f"{current.data}")
            current = current.next

        return "->".join(output)
