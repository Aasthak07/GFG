# User function Template for python3

class Solution:
    def rotate(self, arr):
        n = len(arr)
        if n == 0:
            return arr
        
        # Save the last element
        last = arr[-1]
        
        # Shift elements to the right
        for i in range(n-1, 0, -1):
            arr[i] = arr[i-1]
        
        # Place last element at first position
        arr[0] = last
        
        return arr
        
#         1. range(start, stop, step)

# start = n-1 → loop starts from the last index of the array.

# stop = 0 → the loop stops just before 0 (Python ranges are exclusive of the stop value).

# step = -1 → the loop goes backward (decreasing by 1 each time).

# 2. Example with n = 5

# Suppose the array is [1, 2, 3, 4, 5], so n = 5.

# range(n-1, 0, -1) → range(4, 0, -1)
# This generates:

# i = 4, 3, 2, 1

# 3. What happens inside the loop?

# We shift each element to the right by one position:

# arr[i] = arr[i-1]


# When i = 4: arr[4] = arr[3] → last element becomes 4

# When i = 3: arr[3] = arr[2] → position 3 becomes 3

# When i = 2: arr[2] = arr[1] → position 2 becomes 2

# When i = 1: arr[1] = arr[0] → position 1 becomes 1

# Now the array looks like: [1, 1, 2, 3, 4]

# Finally, after the loop, we set:

# arr[0] = last   # last = 5


# Result: [5, 1, 2, 3, 4]
