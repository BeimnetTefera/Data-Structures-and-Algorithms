class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        curr_sum = sum(nums)
        expected_sum = n * (n + 1) // 2
        missing_value = expected_sum - curr_sum

        return missing_value