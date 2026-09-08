class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # left child: 2 * i only if index 0 is not a value, but in this case it would be
        # (2 * i) + 1

        # right child: (2 * i) + 2

        # parent child: (i - 1) / 2


        maxHeap = []

        for num in stones:
            heapq.heappush(maxHeap, -num)

        print("initial:", maxHeap)

        while len(maxHeap) > 1:
            # Pop the two largest stones:
            # "pick up the two stones and smash them together"
            y = heapq.heappop(maxHeap)
            x = heapq.heappop(maxHeap)

            y = y - x # this is the smash
            # If y != x, push the remaining weight back into the
            # heap in negated form:
            if y < 0: # use < because y and x are negative => "if y > x: smash the two stones together!"" ==> "if y has a weight. In other words, if y has a weight after the smashing of the two stones..."
                heapq.heappush(maxHeap, y) # push y to the heap
        if len(maxHeap) >= 1:
            return -1 * maxHeap[len(maxHeap) - 1]
        
        return 0