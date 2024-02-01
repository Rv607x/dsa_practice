""""
Stack data Structure implementation in python
"""

class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """ Push is a stack operation to add elements to a stack
        When an element is pushed to a stack, it's added to the top 
        of the stack
        """
        self.items.append(item)

    def pop(self):
        """
        Remove the top element of the stack
        """
        return self.items.pop()

    def is_empty(self):
        """
        check if the stack is empty
        """
        return self.items == []

    def peek(self):
        """
        Used to view the top element of the stack 
        """
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items
    
    
# Test functionality
mystack = Stack()
mystack.push("A")
mystack.push("cow")
print(mystack.get_stack())
mystack.push("C")
print(mystack.get_stack())
mystack.pop()
print(mystack.get_stack())
print(mystack.peek())

newStack = Stack()
print(newStack.is_empty())