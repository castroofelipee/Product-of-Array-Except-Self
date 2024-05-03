class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left_product = [1] * n
        right_product = [1] * n
        
        
        for i in range(1, n):
            left_product[i] = left_product[i - 1] * nums[i - 1]
        
        
        for i in range(n - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]
        
        
        result = [left_product[i] * right_product[i] for i in range(n)]
        
        return result


# Author: Felipe Castro on May 3, 2024

# I started by defining a class Solution with a method productExceptSelf that takes in a list of integers nums as input and returns a list of integers as output.
# Inside the method, i initialize the length of the input array nums as n, and we create a result array initialized with ones, which will eventually store the product of all elements except self.