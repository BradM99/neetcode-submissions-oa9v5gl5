class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in numDict:
                return [numDict[difference], i]
            else:
                numDict[nums[i]] = i
        
        return False