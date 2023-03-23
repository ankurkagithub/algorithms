class Node:
    '''
    Node is an object to store data and pointer information for each linked list
    element.
    '''
    def __init__(self, data = None):
        self.data = data
        self.next = None
    # implementing a built in __repr function to show store data in node,
    # instead of some random object data
    def __repr__(self):
        return f"Node: {self.data}"


class LinkedList():
    '''
    This class creates Linklist object which than can be manipulated as per
    task requirements.
    '''
    # Creating a constructor to
    def __init__(self, head = None):
        self.head = head

    def is_empty(self):
        '''
        Checks if the linked list is empty or not. Returns True or False.
        Complexities-  Time: O(1), Space: O(1)
        '''
        return self.head is None

    def size(self):
        current = self.head
        size = 0
        while current:
            current = current.next
            size += 1
        return size

    def insert(self, new_data, index = 0):
        '''
        This function inserts the data at specified index.
        Default value for index is 0 unless specified otherwise.
        Complexities-
        Time: If inserting at the start with index 0: O(1) otherwise O(n)
        Space: O(1)
        '''
        node = Node(new_data)
        current = self.head
        position = 0
        if index == 0:
            node.next = current
            self.head = node
            return
        while position < index:
            previous = current
            current = current.next
            position += 1
        previous.next = node
        node.next = current
        return

    def insert_at_end(self, data):
        '''
        Traverse through the list and locate the last element.
        It adds the new data node to the last elment using it pointer.
        Complexities-
        Time: O(n)
        Space: O(1)
        '''
        node = Node(data)
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def insert_list(self,values):
        '''
        This function calls insert_at_end function. Traverse through the list
        and locate the last element. It adds the new data node to the last
        elment using it pointer.
        Complexities-
        Time: O(n)
        Space: O(1)
        '''
        for value in values:
            self.insert_at_end(value)

    def remove(self, data):
        '''
        Traverse through the linked list and locate the data value.
        If found the value is removed.
        Complexities-
        Time: O(n)
        Space: O(1)
        '''
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

if __name__ == "__main__":
    l = LinkedList()
    l.insert(4,0)
    data = [3,4,5,6,'ankur',9]
    l.insert_list(data)
    print(l)
