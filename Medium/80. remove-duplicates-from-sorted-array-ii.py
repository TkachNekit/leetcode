class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        p1, p2 = 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                p1 += 1
            else:
                p1 = 1

            if p1 <= 2:
                nums[p2] = nums[i]
                p2 += 1
        return p2


"""
Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

sol = Solution()
nums = [1,1,1,2,2,3]
print(sol.removeDuplicates(nums))