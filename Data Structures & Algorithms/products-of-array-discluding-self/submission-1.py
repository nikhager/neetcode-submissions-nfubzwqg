class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Given an integer array nums, return an array output 
        # where output[i] is the product of all the elements of nums except nums[i].

        # Initialize the result array with all values set to 1.
        size = len(nums)
        output = [1] * size
        # Create a variable prefix = 1.
        prefix = 1
        # First pass (left to right):
        # For each index i:
        for i in range(size):
            # Set output[i] = prefix (product of all elements to the left).
            output[i] = prefix
            # Update prefix *= nums[i].
            prefix *= nums[i]
        # Create a variable postfix = 1.
        postfix = 1
        # Second pass (right to left):
        # For each index i:
        for i in range(size - 1, -1, -1):
            # Multiply output[i] by postfix (product of all elements to the right).
            output[i] *= postfix
            # Update postfix *= nums[i].
            postfix *= nums[i]
        # Return the result array.
        return output

        # Each product is guaranteed to fit in a 32-bit integer.
        
        # Follow-up: Could you solve it in O(n) time without using the division operation?