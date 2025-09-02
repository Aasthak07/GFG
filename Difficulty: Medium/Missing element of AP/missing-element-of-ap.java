// User function Template for Java
class Solution {
    public int findMissing(int[] arr) {
        int n = arr.length;
        
        // Handle edge case: array with only 2 elements
        if (n == 2) {
            // Next element in AP would be arr[1] + (arr[1] - arr[0])
            return 2 * arr[1] - arr[0];
        }
        
        // Find the actual common difference
        // Check first few differences to determine the correct common difference
        int diff1 = arr[1] - arr[0];
        int diff2 = arr[2] - arr[1];
        int commonDiff;
        
        // The correct common difference is the one that appears in most pairs
        if (diff1 == diff2) {
            commonDiff = diff1;
        } else {
            // Check with the last difference to determine which is correct
            int diffLast = arr[n-1] - arr[n-2];
            if (diff1 == diffLast) {
                commonDiff = diff1;
            } else {
                commonDiff = diff2;
            }
        }
        
        // Check if the sequence is already complete
        boolean isComplete = true;
        for (int i = 1; i < n; i++) {
            if (arr[i] - arr[i-1] != commonDiff) {
                isComplete = false;
                break;
            }
        }
        
        // If sequence is complete, return next element
        if (isComplete) {
            return arr[n-1] + commonDiff;
        }
        
        // Binary search to find the missing element
        int left = 0, right = n - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            // Calculate what the value should be at position mid
            // In complete AP: arr[i] = arr[0] + i * commonDiff
            int expectedValue = arr[0] + mid * commonDiff;
            
            if (arr[mid] == expectedValue) {
                // Missing element is in the right half
                left = mid + 1;
            } else {
                // Missing element is in the left half
                right = mid - 1;
            }
        }
        
        // The missing element should be at position 'left'
        return arr[0] + left * commonDiff;
    }
}

// Test class to verify the solution
class TestSolution {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Test cases from the problem
        int[] test1 = {2, 4, 8, 10, 12, 14};
        System.out.println("Test 1: " + java.util.Arrays.toString(test1));
        System.out.println("Expected: 6, Got: " + solution.findMissing(test1));
        System.out.println();
        
        int[] test2 = {1, 6, 11, 16, 21, 31};
        System.out.println("Test 2: " + java.util.Arrays.toString(test2));
        System.out.println("Expected: 26, Got: " + solution.findMissing(test2));
        System.out.println();
        
        int[] test3 = {4, 7, 10, 13, 16};
        System.out.println("Test 3: " + java.util.Arrays.toString(test3));
        System.out.println("Expected: 19, Got: " + solution.findMissing(test3));
        System.out.println();
        
        // Additional test cases
        int[] test4 = {10, 8, 6, 2, 0}; // Descending, missing 4
        System.out.println("Test 4 (Descending): " + java.util.Arrays.toString(test4));
        System.out.println("Expected: 4, Got: " + solution.findMissing(test4));
        System.out.println();
        
        int[] test5 = {1, 3}; // Only two elements
        System.out.println("Test 5 (Two elements): " + java.util.Arrays.toString(test5));
        System.out.println("Expected: 5, Got: " + solution.findMissing(test5));
        System.out.println();
        
        int[] test6 = {-2, 0, 2, 4, 8}; // Missing 6
        System.out.println("Test 6: " + java.util.Arrays.toString(test6));
        System.out.println("Expected: 6, Got: " + solution.findMissing(test6));
    }
}