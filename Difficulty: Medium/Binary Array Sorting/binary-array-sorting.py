class Solution:
    def binSort(self, arr):
        count0 = arr.count(0)  # number of 0s
        n = len(arr)
        
        for i in range(n):
            if i < count0:
                arr[i] = 0
            else:
                arr[i] = 1
