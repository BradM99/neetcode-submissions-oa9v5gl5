class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        # Add stones to a max heap
        stones = [-s for s in stones]
        # No max heap in Python so need to do min heap and reverse to look like max
        heapq.heapify(stones)
        

        # Loop while there are more than 1 stone
        while len(stones) > 1:
            # Pop highest and 2nd highest stone
            biggestStone = heapq.heappop(stones)
            secondBiggest = heapq.heappop(stones)
            #IF both stones are equal, both break
            # IF second largest breaks, take its size away from largest
            if secondBiggest > biggestStone:
                heapq.heappush(stones, biggestStone - secondBiggest)
                #Put largest back into heap

        stones.append(0)
        return -stones[0]