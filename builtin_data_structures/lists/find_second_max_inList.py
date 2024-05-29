def find_second_maximum(nums):
    if nums[1] > nums[0]:
        max_num = nums[1]
        second_max = nums[0]
    else:
        max_num = nums[0]
        second_max = nums[1]
    for i in nums[2:]:
        if i > max_num:
            second_max = max_num
            max_num = i
        if i > second_max and i < max_num:
            second_max = i
    return second_max

print(find_second_maximum([4, 2, 1, 5, 0]))