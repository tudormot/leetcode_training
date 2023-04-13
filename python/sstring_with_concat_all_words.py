"""

You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

    For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.

Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.



Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Since words.length == 2 and words[i].length == 3, the concatenated substring has to be of length 6.
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
The output order does not matter. Returning [9,0] is fine too.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation: Since words.length == 4 and words[i].length == 4, the concatenated substring has to be of length 16.
There is no substring of length 16 is s that is equal to the concatenation of any permutation of words.
We return an empty array.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation: Since words.length == 3 and words[i].length == 3, the concatenated substring has to be of length 9.
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"] which is a permutation of words.
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"] which is a permutation of words.
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"] which is a permutation of words.



Constraints:

    1 <= s.length <= 104
    1 <= words.length <= 5000
    1 <= words[i].length <= 30
    s and words[i] consist of lowercase English letters.


"""
from typing import List


class Solution:
    def get_required_words_map(self, words):
        req = {}
        for w in words:
            if w in req:
                req[w] +=1
            else:
                req[w] = 1
        return req
    def can_still_find_valid_sequences(self, s,words,curr_req,i):

        req_words = sum(curr_req.values())
        # print("letters still available: ", len(s) - i, s[i:])
        return len(s)-i >= req_words * len(words[0])

    def findSubstring(self, input_string: str, words: List[str]) -> List[int]:
        if input_string is None or input_string == "" or words is None or len(words) == 0:
            return [] #Unexpected input
        full_req = self.get_required_words_map(words)

        nw = len(words)
        wl = len(words[0])
        all_concatenation_start_indices = set()
        for j in range(wl):
            concatenations = []
            sequence_start = 0
            i = 0
            s = input_string[j:]
            curr_req = full_req.copy()
            curr_words = []
            curr_words_positions = {}
            print("$$$$BIG BOY ITERATION START$$$$")
            while self.can_still_find_valid_sequences(s,words,curr_req,i):
                candidate = s[i:i+wl]
                print("####START NEW IT#####")
                print("curr_req, i:", curr_req, i)
                print("curr_words: ", curr_words)
                print("candidate: ",candidate)
                gibberish_found_case = False
                same_word_too_close_case = False
                word_not_needed_found_case = False
                accepted_word_case = False
                if candidate in words:
                    if candidate in curr_req and curr_req[candidate]>0:
                        accepted_word_case = True
                    else:
                        if candidate in full_req:
                            same_word_too_close_case = True
                        else:
                            word_not_needed_found_case = True
                else:
                    gibberish_found_case = True

                if accepted_word_case:
                    print("in accepted word case")
                    curr_req[candidate] -= 1
                    if curr_req[candidate] == 0:
                        curr_req.pop(candidate)

                    curr_words.append(candidate)

                    if candidate in curr_words_positions:
                        curr_words_positions[candidate].append(i)
                    else:
                        curr_words_positions[candidate] = [i]

                    if len(curr_req) == 0:
                        print("found a solution at index: ", sequence_start)
                        concatenations.append(sequence_start)

                    i += wl
                    if len(curr_words) == nw:
                        sequence_start += wl
                        old_word = curr_words.pop(0)
                        if old_word in curr_req:
                            curr_req[old_word] += 1
                        else:
                            curr_req[old_word] = 1

                        curr_words_positions[old_word].pop(0)

                if gibberish_found_case:
                    curr_req = full_req.copy()
                    i += wl
                    sequence_start = i
                    curr_words = []
                    curr_words_positions = {}

                if word_not_needed_found_case:
                    curr_req = full_req.copy()
                    i += wl
                    sequence_start = i
                    curr_words = []
                    curr_words_positions = {}

                if same_word_too_close_case:
                    print("in words too close case. curr_words in seq:", curr_words)
                    curr_words.append(candidate)
                    curr_words_positions[candidate].append(i)
                    i += wl
                    curr_req[candidate] = -1

                    popped_word = None
                    while popped_word != candidate:
                        popped_word = curr_words.pop(0)
                        print("popping this word: ", popped_word)
                        sequence_start += wl
                        curr_words_positions[popped_word].pop(0)
                        if popped_word in curr_req:
                            curr_req[popped_word]+=1
                            if curr_req[popped_word]==0:
                                curr_req.pop(popped_word)
                        else:
                            curr_req[popped_word]=1
            concatenations = (x + j for x in concatenations)
            all_concatenation_start_indices.update(concatenations)
        return all_concatenation_start_indices


if __name__ == "__main__":
    s = "mississippi"
    words = ["is","si"]
    print(Solution().findSubstring(s,words))
    # Output: [0, 9]



