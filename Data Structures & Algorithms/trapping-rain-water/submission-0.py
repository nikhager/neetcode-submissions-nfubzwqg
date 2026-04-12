class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = len(height) - 1
        left_height = height[left]
        right_height = height[right]

        while left < right:
            if left_height < right_height:
                left += 1
                left_height = max(left_height, height[left])
                area += left_height - height[left]
            else:
                right -= 1
                right_height = max(right_height, height[right])
                area += right_height - height[right]
                
        return area