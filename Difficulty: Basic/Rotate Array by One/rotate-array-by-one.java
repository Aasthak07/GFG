class Solution {
    public void rotate(int[] arr) {
        int n = arr.length;
        if (n == 0) return; // handle empty array
        
        int last = arr[n - 1]; // save the last element
        
        // shift all elements one position to the right
        for (int i = n - 1; i > 0; i--) {
            arr[i] = arr[i - 1];
        }
        
        arr[0] = last; // place last element at the front
    }
}
