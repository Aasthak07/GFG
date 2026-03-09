class Solution:
    def frequencyCount(self, arr):
        n = len(arr)
        freq = [0]*n
        
        for num in arr:
            if num <= n:
                freq[num-1] += 1
        
        return freq