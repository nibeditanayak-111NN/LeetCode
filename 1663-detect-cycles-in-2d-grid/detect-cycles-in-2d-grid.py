class Solution:
    def containsCycle(self, grid):
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(x, y, px, py, char):
            visited[x][y] = True

            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == char:
                    if not visited[nx][ny]:
                        if dfs(nx, ny, x, y, char):
                            return True
                    elif nx != px or ny != py:
                        return True

            return False

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True

        return False


if __name__ == "__main__":
    obj = Solution()

    grid1 = [["a","a","a","a"],
             ["a","b","b","a"],
             ["a","b","b","a"],
             ["a","a","a","a"]]
    print(obj.containsCycle(grid1))

    grid2 = [["c","c","c","a"],
             ["c","d","c","c"],
             ["c","c","e","c"],
             ["f","c","c","c"]]
    print(obj.containsCycle(grid2))

    grid3 = [["a","b","b"],
             ["b","z","b"],
             ["b","b","a"]]
    print(obj.containsCycle(grid3))