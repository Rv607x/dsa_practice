from stack import Stack

def reverse_string(Stack, input_str):
    for i in range(len(input_str)):
        Stack.push(input_str[i])
    rev_str = ""
    while not Stack.is_empty():
        rev_str += Stack.pop()
    return rev_str

stack = Stack()
input_str = "!evitacudE ot emocleW"
print(reverse_string(stack, input_str))