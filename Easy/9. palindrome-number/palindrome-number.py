"""Solution with a challenge of not converting the integer to a string"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        copy_num = x
        new_num = 0
        while copy_num > 0:
            digit = copy_num % 10
            new_num = new_num * 10 + digit
            copy_num //= 10
        print(x, new_num)
        return x == new_num


"""Solution with a shortest code"""
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


solution = Solution2()
print(solution.isPalindrome(10))
