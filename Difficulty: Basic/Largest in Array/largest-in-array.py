class Solution:
    def largest(self, arr):
        # code here
        # arr.sort()
        # return arr[-1]
        n= len(arr)
        max= arr[0]
        for i in range(n):
            if arr[i]>max:
                max=arr[i]
        return max        
        
        
