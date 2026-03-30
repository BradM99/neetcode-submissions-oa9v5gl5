class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        insert_pos = m + n - 1        # Position where the next largest element goes
        index1 = m - 1                # Last valid element in nums1
        index2 = n - 1                # Last element in nums2

        while index2 >= 0:
            if index1 >= 0 and nums1[index1] > nums2[index2]:
                nums1[insert_pos] = nums1[index1]
                index1 -= 1
            else:
                nums1[insert_pos] = nums2[index2]
                index2 -= 1
            insert_pos -= 1