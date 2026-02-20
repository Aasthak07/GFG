#User function Template for python3
# non-repeating element.
from collections import defaultdict
class Solution:
    def firstNonRepeating(self, arr):
        
        n=len(arr)
        # Complete the function
        mp=defaultdict(lambda:0)
        
            # Insert all array elements in hash table
        for i in range(n):
            mp[arr[i]]+=1
        
        
        # Traverse array again and return
    # first element with count 1.
        for i in range(n):
            if mp[arr[i]] == 1:
                return arr[i]
        return 0    
        
