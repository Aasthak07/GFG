class Solution:
    def frequencyCount(self, arr):
        n = len(arr)
        
        freq = {}

        # count frequency
        for num in arr:
            freq[num] = freq.get(num,0)+1

        res = []

        # build result for numbers 1..n
        for i in range(1,n+1):
            res.append(freq.get(i,0))

        return res