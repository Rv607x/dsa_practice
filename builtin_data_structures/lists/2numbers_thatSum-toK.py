# Given a list of integers, nums, and an integer target, k, find two numbers
# in the list that sum up to the target k.


def find_sum(nums, k):
    for i in nums:
        for j in nums[1:]:
            if i + j == k:
                return[i, j]

print(find_sum([2,4,6,8,10,19], 21))