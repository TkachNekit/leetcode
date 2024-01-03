class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        mutual_prefix = ""
        word = min(strs, key=len)
        for i in range(len(word)):
            letter = word[i]
            if all(list(map(lambda x: x[i] == letter, strs))):
                mutual_prefix += letter
            else:
                break
        return mutual_prefix


"""
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
"""

solution = Solution()
print(solution.longestCommonPrefix(["cir","car"]))