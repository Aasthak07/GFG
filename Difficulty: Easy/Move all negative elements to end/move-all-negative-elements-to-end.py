class Solution:
    def segregateElements(self, arr):
        n = len(arr)
        negatives = []  # store negatives temporarily
        pos_index = 0
        
        # Move positives to the front and collect negatives
        for i in range(n):
            if arr[i] >= 0:
                arr[pos_index] = arr[i]
                pos_index += 1
            else:
                negatives.append(arr[i])
        
        # Append negatives after positives
        for neg in negatives:
            arr[pos_index] = neg
            pos_index += 1
