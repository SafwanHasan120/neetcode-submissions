class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s2) < len(s1)):
            return False
        n = len(s1)
        s = s2
        compare = {}
        for char in s1:
            compare[char] = compare.get(char, 0) + 1
        subDict = {}
        for char in s[0:n]:
            subDict[char] = subDict.get(char, 0) + 1
        if(subDict == compare):
            return True
        for i in range(1, len(s) - n + 1):
            if(subDict[s[i-1]] == 1):
                subDict.pop(s[i-1])
            else:
                subDict[s[i-1]] = subDict.get(s[i-1], 0) - 1
            subDict[s[i+n-1]] = subDict.get(s[i+n-1], 0) + 1
            if(subDict == compare):
                return True
            
        return False

        
