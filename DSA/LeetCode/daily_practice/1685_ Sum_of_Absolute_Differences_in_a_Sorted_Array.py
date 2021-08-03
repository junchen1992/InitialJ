"""
@Probelm: 1685. Sum of Absolute Differences in a Sorted Array
@Link: https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

@Author Jun
@Date August 3rd, 2021
"""
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        """Math."""
        n = len(nums)
        result = [0] * n
        
        # Compute result[0]
        result[0] = sum(map(lambda x: abs(nums[0] - x), nums))
        
        # Compute remaining entries
        for idx in range(1, n):
            result[idx] = result[idx - 1] + (2 * idx - n) * (nums[idx] - nums[idx - 1])
            
        return result
