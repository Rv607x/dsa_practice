def reverse_string(input_str: str):
    empty_lst = []
    new_str = ""
    if len(input_str) == 0:
        return input_str
    else:
        for i in input_str:
            empty_lst.append(i)
    while len(empty_lst) > 0:      
        new_str += empty_lst.pop()
    return new_str

input_str = "!evitacudE ot emocleW"
print(reverse_string(input_str))
print(reverse_string(""))

