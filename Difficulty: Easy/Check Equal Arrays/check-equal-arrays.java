import java.util.*;

class Solution {
    public static boolean checkEqual(int[] a, int[] b) {
        if (a.length != b.length) return false;

        Map<Integer, Integer> freq = new HashMap<>();

        // Count frequencies of elements in a[]
        for (int num : a) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        // Subtract frequencies using b[]
        for (int num : b) {
            if (!freq.containsKey(num) || freq.get(num) == 0) {
                return false;
            }
            freq.put(num, freq.get(num) - 1);
        }

        return true;
    }
}
