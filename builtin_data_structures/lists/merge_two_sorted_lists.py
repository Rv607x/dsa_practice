#Given two integer lists, nums1 and nums2, of size m and n, respectively, 
#sorted in nondecreasing order. Merge nums1 and nums2 into a single list sorted in nondecreasing order.

def merge_lists(nums1: list, nums2: list):
    sorted_lst = nums1 + nums2
    sorted_lst.sort()
    return sorted_lst

print(merge_lists([0,1,4,9], [-111,-20,-5,5,11,20]))

def merge_lists2(nums1: list, nums2: list):
    sorted_lst = []
    p1 = nums1[0]
    return sorted_lst


print(merge_lists2([0,1,4,9], [-111,-20,-5,5,11,20]))