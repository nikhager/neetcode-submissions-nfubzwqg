class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        size = len(temperatures)
        left = 0
        right = 1

        while left < size:
            if right > size - 1:
                result.append(0)
                left += 1
                right = left + 1
            elif temperatures[right] > temperatures[left]:
                result.append(right - left)
                left += 1
                right = left + 1
            else:
                right += 1
            
        return result