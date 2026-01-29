class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = []
        store  = { }
        for num in nums:
            if num not in store:
                store[num] = 1
            else:
                store[num] += 1

        for num, freq in store.items():
            if freq > (size / 3):
                ans.append(num)

        return ans