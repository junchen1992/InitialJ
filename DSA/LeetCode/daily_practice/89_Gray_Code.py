class Solution:
    def grayCode(self, n: int) -> List[int]:
        size = 2 ** n
        bin_code = ['0'] * n
        gray_code = [0] * size
        
        idx = 0
        for _ in range((size >> 1) - 1):
            gray_code[idx + 1] = self.step1(bin_code)
            gray_code[idx + 2] = self.step2(bin_code)
            idx += 2
        gray_code[idx + 1] = self.step1(bin_code)
        
        return gray_code
    
    def step1(self, bin_code):
        bin_code[-1] = str(1 - int(bin_code[-1]))
        
        return int(''.join(bin_code), base=2)
    
    def step2(self, bin_code):
        n = len(bin_code)
        for idx in range(-1, -n - 1, -1):
            if bin_code[idx] == '1':
                bin_code[idx - 1] = str(1 - int(bin_code[idx - 1]))
                return int(''.join(bin_code), base=2)
