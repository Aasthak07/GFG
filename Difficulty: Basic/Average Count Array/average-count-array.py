#User function Template for python3

class Solution:
    def countArray (self, arr, x) : 
        #Complete the function
        
      
        freq = {}
        
        # store frequency of elements
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        result = []
        
        for num in arr:
            avg = (num + x) // 2
            result.append(freq.get(avg, 0))
        
        return result
        
       
