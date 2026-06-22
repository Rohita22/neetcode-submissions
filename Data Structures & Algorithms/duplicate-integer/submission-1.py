class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        k = []
        for num in nums:
            if num in k:
                return True
            else:
                k.append(num)
        return False