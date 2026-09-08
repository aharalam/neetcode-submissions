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
            y = heapq.heappop(maxHeap)
            x = heapq.heappop(maxHeap)

            print("after popping:", maxHeap)

            # If y != x, push the remaining weight back into the
            # heap in negated form:
            if y < x: # use < because y and x are negative
                y = y - x
                heapq.heappush(maxHeap, y)
                print("after pushing the remaining weight back into the heap in negated form:", maxHeap)
            elif y == x:
                print("y == x")
                pass
            else:
                print("else statement reached")
                pass
            
        
        print(maxHeap)
        
        print("len of maxHeap:", len(maxHeap))
        if len(maxHeap) >= 1:
            print("inside of len(maxHeap)")
            return -1 * maxHeap[len(maxHeap) - 1]
        
        return 0