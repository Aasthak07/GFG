#User function Template for python3

class Solution:
    def findMean(self, arr):
        # code here 
        
        n= len(arr)
        sum= 0
        
        for i in range(n):
            sum+=arr[i]
            i+=1
            
        mean = sum//n
        return mean
            