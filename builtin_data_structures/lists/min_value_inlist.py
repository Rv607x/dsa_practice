def find_minimum(lst):
    min_val = lst[0]
    for i in lst[1:]:
        if i < min_val:
            min_val = i
    return min_val

print(find_minimum([-5, 99, 0, -999, 67, -99999]))
