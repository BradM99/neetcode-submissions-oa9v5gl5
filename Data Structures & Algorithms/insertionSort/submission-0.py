# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # Amount of times to loop (length of list)
        pairCount = len(pairs)
        # Empty array to put sorted lists into at each pass
        pairsSorted = []
        # For each element in the array
        for i in range(pairCount):
            # We want the previous element as well to compare
            j = i - 1
            # If there is no previous element skip
            # If the previous element is bigger than the one were looping over, we need to swap them
            while j >= 0 and pairs[j].key > pairs[j+1].key:
                pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
                # We need to then sort the parts before this, so we take 1 away from J to move down
                j-= 1
            # Pairs[:] is a copy of the current pairs list
            pairsSorted.append(pairs[:])
        
        return pairsSorted