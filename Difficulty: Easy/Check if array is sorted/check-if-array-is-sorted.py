class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        arr1= sorted(arr)
        if arr==arr1:
            return True
        else:
            return False