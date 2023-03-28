# This data structure is used for "undo" and back button to visit last page.
# traverse the links/data on the last element
# LIFO: Last in first out


# We can use array instead of stack, we have to use dynamic array which can use
# ammortised memory.
s = []
s.append("one")
s.append("ka")
s.append("two")

print(s.pop())
print(s.pop())
print(s.pop())

# or we can use linked list but we have to traverse to the end


# In python we use collection.deque for stack
from collections import deque
stack = deque()
stack.append("deque - first")
stack.append("deque - second")
stack.append("12345")

print(stack)




class Stack():
    def __init__(self):
        self.container = deque()

    def push(self,data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)
    # This has push to add new data or pop to access
    # last element.
    # pusshing and popping is O(1)
    # seraching an element is O(n)

stack = Stack()
stack.push("A")
stack.push("B")
stack.push("C")
stack.push("D")

print("Peek: ", stack.peek())
print("Is_empty: ", stack.is_empty())
print("Size: ", stack.size())
print("Pop: ",stack.pop() )
print("Size: ", stack.size())
")
