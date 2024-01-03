class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        needle_length = len(needle)
        for i in range(len(haystack) - needle_length + 1):
            if haystack[i:i + needle_length] == needle:
                return i
        return -1


"""
Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""

solution = Solution()
print(solution.strStr("abc", "c"))