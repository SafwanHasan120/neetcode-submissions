class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for char in s:
            letters[char] = letters.get(char, 0) + 1
        for char in t:
            if(letters.get(char, 0) != 0):
                letters[char] -= 1
            else:
                return False
        return all(value == 0 for value in letters.values())