class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequencies = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, count in count.items():
            frequencies[count].append(num)
        
        highestk = []
        for i in range(len(frequencies) -1, 0, -1):
            for num in frequencies[i]:
                highestk.append(num)
                if len(highestk) == k:
                    return highestk