class Solution:
    def countArrangement(self, N: int) -> int:
        self.count = 0
        nums = set(range(1, N + 1))
        cur_arr = [0] * N
        self.back_tracking(nums, cur_arr, 0)
        
        return self.count
        
    def back_tracking(self, nums, cur_arr, start_index):
        n = len(cur_arr)
        
        if start_index == n:
            if not nums:
                self.count += 1
            else:
                return
        
        else:
            next_index = start_index + 1
            for num in nums:
                if num % next_index == 0 or next_index % num == 0:
                    cur_arr[start_index] = num
                    self.back_tracking(nums - {num}, cur_arr, next_index)
                    cur_arr[start_index] = 0
