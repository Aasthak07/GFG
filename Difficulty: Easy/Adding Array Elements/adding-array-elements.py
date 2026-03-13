import heapq

class Solution:
    def minOperations(self, arr, n, k):
        heapq.heapify(arr)   # convert list to min heap
        operations = 0
        
        while len(arr) > 1 and arr[0] < k:
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)
            
            heapq.heappush(arr, first + second)
            operations += 1
        
        if arr and arr[0] >= k:
            return operations
        return -1
