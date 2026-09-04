class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        lettersT = {}
        for char in s:
            letters[char] = letters.get(char, 0) + 1
        for char in t:
            lettersT[char] = lettersT.get(char, 0) + 1
        return letters == lettersT