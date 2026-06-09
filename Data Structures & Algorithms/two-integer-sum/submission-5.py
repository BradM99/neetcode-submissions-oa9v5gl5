class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nummap:
                return [nummap[diff], i]
            nummap[nums[i]] = i 