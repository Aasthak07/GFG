class Solution:
    def maxCircularSum(self, arr):
        total = sum(arr)

        currMax = maxSum = arr[0]
        currMin = minSum = arr[0]

        for num in arr[1:]:
            currMax = max(num, currMax + num)
            maxSum = max(maxSum, currMax)

            currMin = min(num, currMin + num)
            minSum = min(minSum, currMin)

        # if all elements are negative
        if maxSum < 0:
            return maxSum

        return max(maxSum, total - minSum)