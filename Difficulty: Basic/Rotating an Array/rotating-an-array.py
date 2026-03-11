class Solution:
    def leftRotate(self, arr, d):
        n = len(arr)
        d = d % n
        
        def reverse(l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        
        reverse(0, d-1)
        reverse(d, n-1)
        reverse(0, n-1)
        
        return arr