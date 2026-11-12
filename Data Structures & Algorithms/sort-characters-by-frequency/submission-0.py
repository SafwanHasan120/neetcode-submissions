class Solution:
    def frequencySort(self, s: str) -> str:
        freqs = {}
        for char in s:
            freqs[char] = freqs.get(char, 0) + 1
        
        maxFreq = max(freqs.values())
        buckets = [[] for _ in range(maxFreq+1)]
        for char, freq in freqs.items():
            buckets[freq].append(char)
        res = []
        for freq in range(len(buckets)-1, -1, -1):
            for char in buckets[freq]:
                for i in range(freq):
                    res.append(char)
        return "".join(res)