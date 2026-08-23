class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i, n in enumerate(nums):
            values[n] = i
        for i, n in enumerate(nums):
            diff = target - n
            if diff in values and values[diff] != i:
                return [i,values[diff]] 
        return [] 
