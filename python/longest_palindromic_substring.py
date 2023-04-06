"""
Given a string s, return the longest
palindromic
substring
in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"



Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.

"""
class EvenPalindromeWatcher:
    def __init__(self, index_of_expected_letter, s):
        # assumption: rest of code uses this class nicely and doesn't
        # provide invalid indices
        self.palindrome_middle_index = index_of_expected_letter
        self.s = s
        self.index_of_expected_letter = index_of_expected_letter
        self.palindrome_length = 0
        self.is_palindrome_terminated = False

    def update_palindrome(self, i):
        if not self.is_palindrome_terminated and self.s[i] == self.s[ \
                self.index_of_expected_letter]:
            # print("debug, we got here for pal with middle: ", self.s[self.palindrome_middle_index], "and with testing "
            #                                                                                     "char: "
            #                                                                                 "", self.s[i])
            self.index_of_expected_letter -= 1
            self.palindrome_length += 2
        else:
            self.is_palindrome_terminated = True

        self.is_palindrome_terminated = self.is_palindrome_terminated or \
                                        self.index_of_expected_letter == -1
        return self.is_palindrome_terminated

    def return_palindrome_substring(self):
        pal_half_length = self.palindrome_length //2
        # print("debug, in even palindrome halflength = ", pal_half_length, "mid letter=", self.s[self.palindrome_middle_index])

        substring = self.s[
                    self.palindrome_middle_index - pal_half_length +1 :
                    self.palindrome_middle_index + pal_half_length + 1]

        return substring

class OddPalindromeWatcher:
    def __init__(self, index_of_expected_letter, s):
        # assumption: rest of code uses this class nicely and doesn't
        # provide invalid indices
        self.palindrome_middle_index = index_of_expected_letter
        self.s = s
        # self.is_first_update = True
        self.index_of_expected_letter = index_of_expected_letter -1
        self.palindrome_length = 1
        self.is_palindrome_terminated = self.index_of_expected_letter < 0

    def update_palindrome(self, i):
        if not self.is_palindrome_terminated and self.s[i] == self.s[\
                self.index_of_expected_letter]:
            # print("DDBUG, we got here for pal with middle: ", self.s[self.palindrome_middle_index], "and with testing "
            #                                                                                         "char: "
            #                                                                                         "", self.s[i])
            self.index_of_expected_letter -=1
            self.palindrome_length += 2
        else:
            self.is_palindrome_terminated = True

        self.is_palindrome_terminated = self.is_palindrome_terminated or \
                                   self.index_of_expected_letter == -1
        # print("for mid letter:",self.s[self.palindrome_middle_index],"PALIN terminated: ", self.is_palindrome_terminated)
        return self.is_palindrome_terminated


    def return_palindrome_substring(self):
        #compute palindrome start index:
        # if self.is_odd_palindrome:
        pal_half_length = (self.palindrome_length -1 )//2
        # print("debug, halflength = ", pal_half_length)
        substring = self.s[
                    self.palindrome_middle_index-pal_half_length:self
                    .palindrome_middle_index + pal_half_length + 1]
        # else:
        #     pal_half_length = self.palindrome_length //2        # self.is_first_update = True

        #     substring = self.s[
        #                 self.palindrome_middle_index - pal_half_length +1 :
        #                 self.palindrome_middle_index + pal_half_length + 1]

        return substring






class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_subpalindrome = s[0]
        if len(s) == 1:
            return max_subpalindrome
        max_subpalindrome_length  = 1
        max_subpalindrome_watcher = None
        active_subpalindromes = [] #list containing objects, with following
        # fields: subpalindrome_size
        for i in range(len(s)):
            # print("analysing letter:" , s[i])
            new_active_subpalindromes = []
            for w in active_subpalindromes:
                # print("we here")
                is_termination_encountered = w.update_palindrome(i)
                # print("is_termination_encountered: ", is_termination_encountered)
                if is_termination_encountered:
                    if w.palindrome_length > max_subpalindrome_length:
                        # print("changing max watcher")
                        max_subpalindrome_watcher = w
                        max_subpalindrome_length = w.palindrome_length
                else:
                    # print("appending something, w= ", w)
                    new_active_subpalindromes.append(w)
            active_subpalindromes = new_active_subpalindromes
            active_subpalindromes.extend([OddPalindromeWatcher(i,s),EvenPalindromeWatcher(i,s)])

        # print("active subpali:", active_subpalindromes)
        # print("max_pali_length: ", max_subpalindrome_length)
        # for w in active_subpalindromes:
            # print("legth of this pali: ", w.palindrome_length)
        if active_subpalindromes[\
                0].palindrome_length > \
                max_subpalindrome_length:
            max_subpalindrome_watcher = active_subpalindromes[0]
            max_subpalindrome_length = max_subpalindrome_watcher.palindrome_length
        if max_subpalindrome_length == 1:
            return s[0]        # self.is_first_update = True        # self.is_first_update = True
        else:
            return max_subpalindrome_watcher.return_palindrome_substring()

if __name__ == "__main__":
    # s = "cc"
    s = "abb"

    # s = "abcba"

    print(Solution().longestPalindrome(s))



