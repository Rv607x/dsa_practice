# Given a list of integers, lst, remove all the even integers from the list.

def remove_even(lst: list):
    new_lst= []
    for i in lst:
        if i % 2 != 0:
            new_lst.append(i)
    return new_lst

print(remove_even([0, 6, 9, 76, -4, 7]))
