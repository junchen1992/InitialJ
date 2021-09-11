"""给定一个字符串s，找到第一个最长不重复子串."""

#coding=utf-8
import sys 
# #str = input()
# #print(str)
# print('Hello,World!')
def solve(s: str):
    if not s or len(s) < 2:
        return s

    # Two indicies in the string s
    p1, p2 = 0, 0  # Inclusive indicies
    ans = s[0]
    chars = {s[0]} # Store current window's chars
    n = len(s)
    while p1 < n - 1 and p2 < n - 1:
        if p2 == n - 1:
            if p2 - p1 + 1 > len(ans):
                ans = s[p1: p2 + 1]
            break

        next_char = s[p2 + 1]
        if next_char not in chars:
            chars.add(next_char)
#             p2 += 1
        else:
            while p1 <= n - 1 and s[p1] != next_char:
                chars.discard(s[p1])
                p1 += 1
            # p1 now will be updated to just after the one equals next_char
            p1 += 1
        p2 += 1

        if len(chars) > len(ans):
            ans = s[p1: p2 + 1]
#         print(p1, p2, ans, chars)

    return ans

print(solve('ecbecba'))
