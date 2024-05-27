#Given two integer lists, nums1 and nums2, of size m and n, respectively, 
#sorted in nondecreasing order. Merge nums1 and nums2 into a single list sorted in nondecreasing order.

def merge_lists(nums1: list, nums2: list):
    sorted_lst = nums1 + nums2
    sorted_lst.sort()
    return sorted_lst

print(merge_lists([0,1,4,9], [-111,-20,-5,5,11,20]))

def merge_lists2(nums1: list, nums2: list):
    sorted_lst = []
    for i in nums1[:]:
        for j in nums2[:]:
            if i > j:
                sorted_lst.append(j)
                nums2.remove(j)
            elif j > i:
                sorted_lst.append(i)
                nums1.remove(i)
            else:
                if len(nums1) == 0 and len(nums2) > 0:
                    sorted_lst += nums2
                elif len(nums2) and len(nums1)== 0:
                    sorted_lst += nums1
    return sorted_lst


print(merge_lists2([0,1,4,9], [-111,-20,-5,5,11,20]))