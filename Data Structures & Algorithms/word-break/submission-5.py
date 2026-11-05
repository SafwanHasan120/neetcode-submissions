class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        memo = {}
        def bt(rem):
            if(len(rem) == 0):
                return True

            if rem in memo:
                return memo[rem]

            for end in range(1, len(rem) + 1):
                if(rem[:end] in words):
                    if(bt(rem[end:])):
                        memo[rem] = True
                        return True
            memo[rem] = False
            return False
        return bt(s)