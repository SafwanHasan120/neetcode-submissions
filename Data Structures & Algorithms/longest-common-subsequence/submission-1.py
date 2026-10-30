class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        longer = ""
        shorter = ""
        if(text1 == text2):
            return len(text1)
        if(len(text1) > len(text2)):
            longer = text1
            shorter = text2
        else:
            longer = text2
            shorter = text1

        dp = [[0] * (len(shorter) + 1) for _ in range(len(longer) + 1)]
        for i in range(len(longer) - 1, -1, -1):
            for j in range(len(shorter) - 1, -1, -1):
                if(longer[i] == shorter[j]):
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return dp[0][0]
