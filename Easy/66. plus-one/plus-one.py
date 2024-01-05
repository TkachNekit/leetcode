class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        reversed_digits = digits[::-1]
        add_to_next_digit = True
        for i in range(len(digits)):
            if not add_to_next_digit:
                break
            if reversed_digits[i] == 9:
                reversed_digits[i] = 0
            else:
                reversed_digits[i] += 1
                add_to_next_digit = False
        if reversed_digits[-1] == 0:
            reversed_digits.append(1)
        return reversed_digits[::-1]




"""
Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""

solution = Solution()
digits = []
print(solution.plusOne(digits))