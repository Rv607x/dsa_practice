def right_rotate(nums, k):
    if len(nums) == k:
        return nums
    if k > len(nums):
        new_k = k % len(nums)
        return nums[-new_k:] + nums[:-new_k]
    if len(nums) > k:
        return nums[-k:] + nums[:-k]

print(right_rotate([1,2,3,4,5,6,7], 1))
