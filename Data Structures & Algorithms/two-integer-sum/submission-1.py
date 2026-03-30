class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numstore = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numstore:
                return [numstore[diff], i]
            else:
                numstore[nums[i]] = i
