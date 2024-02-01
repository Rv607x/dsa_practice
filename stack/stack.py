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
        return self.items.pop()
    

# Test functionality