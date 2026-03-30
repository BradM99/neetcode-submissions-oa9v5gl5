class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0
        # Iterate the right pointer
        for right in range(len(nums)):
            # If the gap between left and right pointer is too big for k
            if right - left > k:
                # Remove the left number from the set
                window.remove(nums[left])
                # Move left forward
                left += 1
            # The set is only of size k at most
            if nums[right] in window:
                return True
            window.add(nums[right])

        return False