"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

    Read in and ignore any leading whitespace.
    Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
    Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
    Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
    If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
    Return the integer as the final result.

Note:

    Only the space character ' ' is considered a whitespace character.
    Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.



Example 1:

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.

Example 2:

Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.

Example 3:

Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.



"""
from typing import Tuple


class Solution:
    def myAtoi(self, s: str) -> int:
        if s is None or s == "":
            return 0
        in_lead_spaces_valid_state = True
        invalid_char_found = False
        sign_char_found = False
        sign_of_number = False # false for negative, true for positive
        valid_number_start_index = -1
        for i,c in enumerate(s):
            if in_lead_spaces_valid_state and c == ' ':
                continue
            else:
                in_lead_spaces_valid_state = False
                if ord(c) >= 48 and ord(c) <= 57:
                    valid_number_start_index = i
                    if not sign_char_found:
                        sign_of_number = True
                    break
                elif c == "+":
                    sign_of_number = True
                    valid_number_start_index = i+1
                    break
                elif c=="-":
                    sign_of_number = False
                    valid_number_start_index = i +1
                else:
                    return 0

        for i, c in enumerate(s[valid_number_start_index:]):
            if c == '0':
                continue
            else:
                valid_number_start_index = i
                break
        r = 0
        for i, c in enumerate(s[valid_number_start_index:]):
            ascii_code = ord(c)
            if ascii_code >= 48 and ascii_code <= 57:
                r = r * 10 + ascii_code - 48
            else:
                break
        if sign_of_number is False:
            r = r* -1
        const = pow(2,31)
        return max(min(r,const-1),-const)






if __name__ == "__main__":
    # b = bytes(s, 'utf-8')
    print(Solution().myAtoi("-+abc%"))