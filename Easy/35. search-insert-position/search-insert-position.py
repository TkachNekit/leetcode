class Solution:
    """Bad-looking binary search"""

    def searchInsert(self, nums: list[int], target: int) -> int:
        left_index = 0
        right_index = len(nums) - 1
        if nums[left_index] >= target:
            return 0
        if nums[right_index] == target:
            return right_index
        if nums[right_index] < target:
            return right_index + 1
        while True:
            new_middle_index = (left_index + right_index) // 2
            if new_middle_index == left_index:
                break
            if nums[new_middle_index] == target:
                return new_middle_index
            elif nums[new_middle_index] < target:
                left_index = new_middle_index
            elif nums[new_middle_index] > target:
                right_index = new_middle_index
        return left_index + 1

    """good-looking binary search"""

    def binary_search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return left


"""
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""
solution = Solution()

nums = [1, 3]
target = 3
print(solution.searchInsert(nums, target))
