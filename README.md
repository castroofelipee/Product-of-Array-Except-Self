# Product of Array Except Self
- Given an integer array nums, return an array answer such that answer is equal to the product of all the elements of nums except nums.

## Calculating Left Products:
- Traverse through the input `array` nums from index 1 to n-1 and calculate the product of all elements to the left of each element.

- This is done by updating the result array at each index i with the product of all elements from index `0 to i-1` in the nums array.

- At the end of this loop, the result array contains the product of all elements to the left of each element in the nums array.

```python
def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left_product = [1] * n
        right_product = [1] * n
```

- By Felipe Castro 
