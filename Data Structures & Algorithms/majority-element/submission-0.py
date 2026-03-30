class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        highest, count = 0, 0

        # [1, 2, 2, 2, 5, 4, 2]

        for num in nums:
            # 1, 2, 2, 2, 5, 4
            if count == 0: # 0, 1, 0, 1, 2, 1, 0
                highest = num #[1] [2]
            count += (1 if num == highest else -1)
        
        return highest