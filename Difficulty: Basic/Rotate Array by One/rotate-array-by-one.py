#User function Template for python3

class Solution:
    def rotate(self, arr):
        n= len(arr)
        
        last_val= arr[n-1]
        
        for i in range(n-1, 0, -1):
            arr[i]= arr[i-1]
            
        arr[0] = last_val   
    
