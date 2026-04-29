class Solution:
    def maximumScore(self, grid):
        n = len(grid)
        col_sums = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                col_sums[j][i+1] = col_sums[j][i] + grid[i][j]

        dp = [[-float('inf')] * 3 for _ in range(n + 1)]
        for h in range(n + 1):
            dp[h][0] = 0

        for j in range(n):
            new_dp = [[-float('inf')] * 3 for _ in range(n + 1)]
            
            curr_max_0_or_2 = -float('inf')
            for h in range(n + 1):
                curr_max_0_or_2 = max(curr_max_0_or_2, dp[h][0], dp[h][2])
                new_dp[0][0] = max(new_dp[0][0], curr_max_0_or_2)

            for h in range(n + 1):
                for prev_h in range(n + 1):
                    s0 = col_sums[j-1][h] - col_sums[j-1][prev_h] if j > 0 and h > prev_h else 0
                    new_dp[h][0] = max(new_dp[h][0], dp[prev_h][0] + s0, dp[prev_h][2] + s0)

                    s1 = col_sums[j][prev_h] - col_sums[j][h] if j > 0 and prev_h > h else 0
                    new_dp[h][1] = max(new_dp[h][1], dp[prev_h][0] + s1, dp[prev_h][1] + s1)

                    new_dp[h][2] = max(new_dp[h][2], dp[prev_h][1], dp[prev_h][2])
            
            dp = new_dp

        return max(max(row) for row in dp)