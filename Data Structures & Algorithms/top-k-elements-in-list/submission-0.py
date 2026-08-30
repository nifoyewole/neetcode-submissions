class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        ans = []
        for num in nums:
                if num not in counts:
                    counts[num] = 0
                counts[num] += 1
        new = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        for x in new:
                ans.append(x[0])
                if len(ans) == k:
                    break
        return ans