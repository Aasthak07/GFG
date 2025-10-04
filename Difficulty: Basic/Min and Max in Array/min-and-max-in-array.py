class Solution:
    def getMinMax(self, arr):
        if not arr:  # handle empty array
            return [None, None]
        
        # initialize min and max as the first element
        minimum = arr[0]
        maximum = arr[0]
        
        # iterate through the array
        for num in arr:
            if num < minimum:
                minimum = num
            elif num > maximum:
                maximum = num
        
        return [minimum, maximum]
