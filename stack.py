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

#######################################################
# In python we use collection.deque for stack
from collections import deque
# stack = deque()
# stack.append("deque - first")
# stack.append("deque - second")
# stack.append("12345")

# print(stack)




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


def is_balanced(data):
    '''
    stack data structure is used to identify if brackets are closed when coding
    '''
    stack = Stack()
    for char in data:
        stack.push(char)
    count_square = 0
    count_curley = 0
    count_parent = 0
    for i in range(stack.size()):
        value = stack.pop()
        if value == "}":
            count_curley += 1
        if value == ")":
            count_parent += 1
        if value == "]":
            count_square += 1
        if value == "{":
            count_curley -= 1
        if value == ")":
            count_parent -= 1
        if value == "]":
            count_square -= 1
    print(count_square)
    print(count_curley)
    print(count_parent)
    return not count_curley and not count_parent and not count_square



data = input("Enter data with parenteses: ")

print(is_balanced(data))
