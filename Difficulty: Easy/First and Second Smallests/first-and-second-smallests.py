# class Solution:
#     def minAnd2ndMin(self, arr):
#         if len(arr) < 2:
#             return -1
        
#         arr = sorted(set(arr))
        
#         if len(arr) < 2:
#             return -1
        
#         return arr[0], arr[1]
class Solution:
    def minAnd2ndMin(self, arr):
        if len(arr) < 2:
            return [-1]
        
        smallest = float('inf')
        second_smallest = float('inf')
        
        for num in arr:
            if num < smallest:
                second_smallest = smallest
                smallest = num
            elif smallest < num < second_smallest:
                second_smallest = num
        
        if second_smallest == float('inf'):
            return [-1]
        
        return [smallest, second_smallest]
