class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for s in strs:
            # Create a 26-element character count array for each string
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # Convert array to a tuple so it can be used as a dict key
            groups[tuple(count)].append(s)
            
        return list(groups.values())
        