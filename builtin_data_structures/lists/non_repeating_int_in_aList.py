def find_first_unique(nums):
    dicti = {}
    lst = []
    for i in nums:
        if i not in dicti:
            dicti[i] = 1
        else:
            dicti[i] += 1
    #print(dicti)
    for i in dicti:
        if dicti[i]== 1:
            lst.append(i)
    return(lst[0])

print(find_first_unique([2, 2, 6]))
print(find_first_unique([-9,1,8,-9,20,1,8]))