def rearrange(lst):
    neg = []
    pos = []
    for i in lst:
        if i < 0:
            neg.append(i)
        else:
            pos.append(i)
    return neg + pos

print(rearrange([1,-2,3,-4,5]))