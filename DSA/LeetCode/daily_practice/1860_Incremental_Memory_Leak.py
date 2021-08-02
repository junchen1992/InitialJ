"""
@Probelm: 1860. Incremental Memory Leak
@Link: https://leetcode.com/problems/incremental-memory-leak/

@Author Jun
@Date August 2st, 2021
"""
class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        crash_time = 0 
        while True:
            if max(memory1, memory2) >= crash_time + 1:
                crash_time += 1
                if memory1 >= memory2:
                    memory1 -= crash_time
                else:
                    memory2 -= crash_time
                
                continue
            
            return [crash_time + 1, memory1, memory2]
