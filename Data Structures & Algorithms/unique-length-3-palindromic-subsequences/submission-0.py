class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        for i in range(len(s)):
            freq[s[i]] -= 1
            if freq[s[i]] == 0:
                freq.pop(s[i])
            for j in range(26):
                c = chr(ord('a') + j)
                if c in left and c in freq.keys():
                    res.add((s[i], c))
            left.add(s[i])
        return len(res)
