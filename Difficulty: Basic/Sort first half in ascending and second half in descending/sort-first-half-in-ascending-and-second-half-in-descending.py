class Solution:
    def customSort(self, arr):
        n = len(arr)
        if n <= 1:
            return arr
            
        arr1 = arr[:n//2]
        arr2 = arr[n//2:]
        arr1.sort()
        arr2.sort(reverse=True)
        return arr1+arr2