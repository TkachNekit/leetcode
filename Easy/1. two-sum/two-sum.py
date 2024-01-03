"""Solution with hash tables, provides O(2n)"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = dict()
        for i in range(len(nums)):
            dic[target - nums[i]] = i
        for i in range(len(nums)):
            number = nums[i]
            if number in dic and dic[number] != i:
                return sorted([i, dic[number]])
        return []


"""Solution with brute force, O(n^2)"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
