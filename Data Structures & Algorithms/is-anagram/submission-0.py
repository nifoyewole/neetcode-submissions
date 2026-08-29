class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}

        for i in s:
            counts[i] = counts.get(i, 0) + 1
        for i in t:
            counts[i] = counts.get(i, 0) - 1

        return all(v==0 for v in counts.values())