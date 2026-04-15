class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.length = len(nums)

    def sumRange(self, left: int, right: int) -> int:
        total = 0
        while left < right + 1:
            total += self.arr[left]
            left += 1
        return total


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)