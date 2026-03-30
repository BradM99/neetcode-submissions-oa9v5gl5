class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Add stones to a max heap
        stones = [-s for s in stones]
        # No max heap in Python so need to do min heap and reverse to look like max
        heapq.heapify(stones)
        

        # Loop while there are more than 1 stone
        while len(stones) > 1:
            # Pop highest and 2nd highest stone
            biggestStone = heapq.heappop(stones)
            secondBiggest = heapq.heappop(stones)
            
            # IF second largest breaks, take its size away from largest
            if secondBiggest > biggestStone:
                #Put largest back into heap
                heapq.heappush(stones, biggestStone - secondBiggest)

        # IF both stones break on the last iteration, we should add a zero
        # This will be ignored if its not necessary anyway as we are returning stones[0]
        stones.append(0)
        return -stones[0]