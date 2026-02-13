class Solution:
    def removeDuplicates(self, arr):
        # code here 
        n= len(arr)
        start=0
        if n == 0:
            return 0
        
        for i in range(1,n):
            # unique
            if arr[i]!=arr[start]:
                start+=1
                arr[start]=arr[i]
        return arr[:start+1]   
            
                