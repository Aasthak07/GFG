class Solution:
    def minAnd2ndMin(self, arr):
        # code here
        n= len(arr)
        smallest = second_smallest= float('inf')
        
        
        
        for i in range(n):
            if arr[i]< smallest:
                second_smallest= smallest
                smallest = arr[i]
                
            elif arr[i] > smallest and arr[i] < second_smallest:
                second_smallest = arr[i]
                
        if second_smallest == float('inf'):
            return [-1]        
        return [smallest, second_smallest]
