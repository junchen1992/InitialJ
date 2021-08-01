"""
@Probelm: 1663. Smallest String With A Given Numeric Value
@Link: https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

@Author Jun
@Date August 1st, 2021
"""
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        remaining_sum = k - n
        z_cnt = remaining_sum // 25
        remaining_sum -= z_cnt * 25
        
        if remaining_sum:
            min_str = 'a' * (n - z_cnt - 1) + chr(remaining_sum + 97) + 'z' * z_cnt
        else:
            min_str = 'a' * (n - z_cnt) + 'z' * z_cnt
        
        return min_str
