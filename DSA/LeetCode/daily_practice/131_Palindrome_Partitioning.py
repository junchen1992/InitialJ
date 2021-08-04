class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """Back-tracking."""
        result = []
        self.bt(s, 0, result, [])
        
        return result
        
    def bt(self, s, start_index, result, cur_parts):
        n = len(s)
        
        if start_index == n:
            result.append([sub_str for sub_str in cur_parts])
            return
        
        for end_index in range(start_index, n):
            sub_str = s[start_index: end_index + 1]
            if self.is_palindrome_str(sub_str):
                cur_parts.append(sub_str)
                self.bt(s, end_index + 1, result, cur_parts)
                cur_parts.pop()
    
    def is_palindrome_str(self, s):
        return s == s[-1::-1]
