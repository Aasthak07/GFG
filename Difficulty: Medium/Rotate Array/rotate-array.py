class Solution:
    
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotateArr(self, nums, d):
        n = len(nums)

        if n == 0:
            return nums
        
        d = d % n   # important step
        
        # Step 1: reverse first d elements
        self.reverse(nums, 0, d - 1)

        # Step 2: reverse remaining n-d elements
        self.reverse(nums, d, n - 1)

        # Step 3: reverse entire array
        self.reverse(nums, 0, n - 1)

        return nums
