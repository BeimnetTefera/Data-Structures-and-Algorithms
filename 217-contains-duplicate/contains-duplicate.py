class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        store = {}
        for num in nums:
            if num not in store:
                store[num] = 1
            else:
                store[num] += 1

        for freq in store.values():
            if freq > 1:
                return True

        return False