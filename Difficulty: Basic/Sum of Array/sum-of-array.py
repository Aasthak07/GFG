#User function Template for python3
class Solution:
	def arraySum(self, arr):
   		# code here
   		
   		sum = 0
   		n= len(arr)
   		
   		for i in range(n):
   		    sum+= arr[i]
   		    i+=1
   		return sum    
