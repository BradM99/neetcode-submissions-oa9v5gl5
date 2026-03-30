class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        # Assume nums array [1, 2, 3, 4]
        # Len = 4
        # ans[i] = nums[i % len(nums)]
        # 0 % 4 = 0
        # 1 % 4 = 1
        # .. 
        # 4 % 4 = 0 <----- Wraps back around to put nums[0], in ans[4]
        for i in range(len(nums) * 2):
            ans.append(nums[i % len(nums)]) 
        return ans