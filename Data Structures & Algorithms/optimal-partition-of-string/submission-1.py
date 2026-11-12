class Solution:
    def partitionString(self, s: str) -> int:
        res = 0
        seen = set()
        seen.add(s[0])
        for char in s:
            if char in seen:
                res += 1
                seen.clear()
                seen.add(char)
            else:
                seen.add(char)
        return res
        #caacdaaaacccabb
        #ca, acd, a, a, a, ac, c, cb, b
        #a: 7, b: 2, c: 5, d: 1
