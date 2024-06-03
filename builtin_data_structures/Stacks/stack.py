"""A typical Stack must contain the following functions:

push(element) - Push to stack
pop() - remove element at top of stack
peek() - view element at top of stack
is_empty() - checks to see if it has elements
size() - size/length of stack

"""

class MyStack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0

    def is_empty(self):
        return self.stack_size == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]
    
    def size(self):
        return self.stack_size

    def push(self, value):
        self.stack_size += 1
        self.stack_list.append(value)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop(-1)

# test code

stack_obj = MyStack()
print(stack_obj)
print(stack_obj.is_empty())
print(stack_obj.peek())
print(stack_obj.size())
for i in range(6):
    stack_obj.push(i)
print(stack_obj.peek())
print(stack_obj.is_empty())
print(stack_obj.size())
print(stack_obj.pop())
print(stack_obj.peek())
