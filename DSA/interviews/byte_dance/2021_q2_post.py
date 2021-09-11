"""给定一个字符串s，找到第一个最长不重复子串."""

def solve(s: str):
    # Edge cases
    if not s:
        return 0

    if len(s) < 2:
        return len(s)

    # Two Pointers
    n = len(s)
    ans = s[0]
    window = {s[0]}
    p1, p2 = 0, 0
    while p2 < n - 1:
        new_p2 = p2
        while new_p2 + 1 < n and s[new_p2] not in window:
            new_p2 += 1
            window.add(s[new_p2]) 
        
    

if __name__ == '__main__':
    assert solve('ecbecba') == 'ecba'
