class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10 :
            return []
        res = set()
        compare = set()
        for i in range(len(s) - 9):
            if(s[i:i+10] in compare):
                res.add(s[i:i+10])
            else:
                compare.add(s[i:i+10])
        return list(res)