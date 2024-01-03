"""First and slow asf program"""


class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }

        count = dict()
        for letter in values.keys():
            count[letter] = 0

        pass_letter = False
        for i in range(len(s)):
            symbol = s[i]
            if pass_letter:
                pass_letter = False
                continue
            if symbol == "I":
                if i == len(s) - 1:
                    count["I"] += 1
                else:
                    if s[i + 1] == "V":
                        count["IV"] += 1
                        pass_letter = True
                    elif s[i + 1] == "X":
                        count["IX"] += 1
                        pass_letter = True
                    else:
                        count["I"] += 1
            elif symbol == "X":
                if i == len(s) - 1:
                    count["X"] += 1
                else:
                    if s[i + 1] == "L":
                        pass_letter = True
                        count["XL"] += 1
                    elif s[i + 1] == "C":
                        pass_letter = True
                        count["XC"] += 1
                    else:
                        count["X"] += 1

            elif symbol == "C":
                if i == len(s) - 1:
                    count["C"] += 1
                else:
                    if s[i + 1] == "D":
                        pass_letter = True
                        count["CD"] += 1
                    elif s[i + 1] == "M":
                        pass_letter = True
                        count["CM"] += 1
                    else:
                        count["C"] += 1
            elif symbol == "V":
                count["V"] += 1
            elif symbol == "L":
                count["L"] += 1
            elif symbol == "D":
                count["D"] += 1
            elif symbol == "M":
                count["M"] += 1
        total = 0
        for sym, value in values.items():
            total += count[sym] * value
        return total


"""Better solution with less code? main difference """


class Solution2:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        for i in range(len(s)):
            if i < len(s) - 1 and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total


solution = Solution2()
"""Test cases"""

"""
Input: s = "III"
Output: 3
Explanation: III = 3
"""
s = "III"
print(solution.romanToInt(s))

"""
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
"""
s = "LVIII"
print(solution.romanToInt(s))

"""
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""
s = "MCMXCIV"
print(solution.romanToInt(s))
