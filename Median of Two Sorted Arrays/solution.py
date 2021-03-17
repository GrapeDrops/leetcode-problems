import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        middle_count = math.ceil(total_len / 2) - 1
        list1_idx, list2_idx = 0, 0
        
        def headValuesHelper(idx_1, idx_2):
            val1 = float('inf') if idx_1 >= len(nums1) else nums1[idx_1]
            val2 = float('inf') if idx_2 >= len(nums2) else nums2[idx_2]
            return val1, val2
        
        for _ in range(middle_count):
            val1, val2 = headValuesHelper(list1_idx, list2_idx)
            if val1 < val2:
                list1_idx += 1
            else:
                list2_idx += 1
        else:
            val1, val2 = headValuesHelper(list1_idx, list2_idx)
            if total_len % 2:
                return min(val1, val2)
            if val1 < val2:
                first_val = nums1[list1_idx]
                list1_idx += 1
            else:
                first_val = nums2[list2_idx]
                list2_idx += 1
            val1, val2 = headValuesHelper(list1_idx, list2_idx) 
            return (first_val + min(val1, val2)) / 2
        
