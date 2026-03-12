class Solution:
    def findMedian(self, arr):
        #code here.
        
        n= len(arr)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if arr[i] > arr[j]:
        #             arr[i], arr[j] = arr[j], arr[i]
        
        arr.sort()
                    
        if n%2==1:
            return arr[n//2]
            
        else:
            return ( arr[n//2] + arr[n//2 -1])/2
