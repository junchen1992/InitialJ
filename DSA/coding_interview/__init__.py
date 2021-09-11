from typing import *


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        record = [[0] * m for _ in range(n)]

        return self.findPath(maze, start[1], start[0], destination[1], destination[0], record)

    def findPath(self, maze, beginX, beginY, endY, endX, record):
        if beginX == endX and beginY == endY:
            return True

        if maze[beginY][beginX] == 1 or record[beginX][beginX]:
            return False

        left, right = beginX, beginX
        up, down = beginY, beginY

        while left





if __name__ == '__main__':
    params = ([5, 7, 7, 8, 8, 10], 8)
    print(Solution().search(*params))
