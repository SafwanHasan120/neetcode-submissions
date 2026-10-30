class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 0, 1, 1, 1, 1, 1
        # 1, 2, 3, 4, 5, 6
        # 1, 3, 6, 10, 15, 21
        
        if(n == 0):
            return m
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if(i == 0 or j == 0):
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]