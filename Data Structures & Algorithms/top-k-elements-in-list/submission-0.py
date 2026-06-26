class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        sorted_by_value = dict(sorted(seen.items(), key=lambda item: item[1]))
        return list(sorted_by_value.keys())[-k:]

