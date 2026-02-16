
def findMedianSortedArrays(nums1, nums2):
    num_add = nums1 + nums2
    num_add.sort()
    n = len(num_add)

    # Odd length
    if n % 2 != 0:
        idx = n // 2
        return float(num_add[idx])

        # Even length
    else:
        idx1 = (n // 2) - 1
        idx2 = n // 2
        return (num_add[idx1] + num_add[idx2]) / 2.0

result = findMedianSortedArrays([1,2],[3,4])
print("Result:",result)