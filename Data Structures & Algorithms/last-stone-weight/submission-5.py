import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]

        stones = [-n for n in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            diff = y-x
            if diff == 0:
                continue
            heapq.heappush(stones, -diff)
        
        if len(stones) == 0:
            return 0
        return -stones[-1]