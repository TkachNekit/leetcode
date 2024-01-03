class Solution:
    def isValid(self, s: str) -> bool:
        open_bracket_set = list()
        bracket_dic = {
            "(": 0,
            ")": 0,
            "[": 0,
            "]": 0,
            "{": 0,
            "}": 0
        }
        "(([]){})"
        for i in range(len(s)):
            bracket_dic[s[i]] += 1
            current_bracket = s[i]
            if current_bracket == "(" or current_bracket == "[" or current_bracket == "{":
                open_bracket_set.append(current_bracket)
            elif current_bracket == ")" or current_bracket == "]" or current_bracket == "}":
                if len(open_bracket_set) == 0:
                    return False
                last_open_bracket = open_bracket_set.pop()
                if current_bracket == ")":
                    if last_open_bracket != "(":
                        return False
                if current_bracket == "]":
                    if last_open_bracket != "[":
                        return False
                if current_bracket == "}":
                    if last_open_bracket != "{":
                        return False
        if (bracket_dic["("] != bracket_dic[")"]) or \
                (bracket_dic["["] != bracket_dic["]"]) or \
                (bracket_dic["{"] != bracket_dic["}"]):
            return False
        return True


"""
Example 1:

Input: s = "()"
Output: true


Example 2:

Input: s = "()[]{}"
Output: true


Example 3:

Input: s = "(]"
Output: false
"""

solution = Solution()
print(solution.isValid("(([]){})"))
