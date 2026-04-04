class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest = 1
        ipotential = 1
        dpotential = 1

        for i in range(len(nums) - 1):

            if nums[i + 1] > nums[i]:
                if ipotential > 1:
                    ipotential += 1
                else:
                    dpotential = 1
                    ipotential += 1

            elif nums[i + 1] < nums[i]:
                if dpotential > 1:
                    dpotential += 1
                else:
                    ipotential = 1
                    dpotential += 1
            else:
                dpotential = 1
                ipotential = 1

            longest = max(longest, dpotential, ipotential)

        return longest
