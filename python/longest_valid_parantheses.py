
def peek_stack(stack):
    if stack:
        return stack[-1]    # this will get the last element of stack
    else:
        return None


class Solution:
    def __init__(self):
        # self.longest_valid = 0
        pass

    def longestValidParentheses(self, s: str) -> int:
        return self.longestValidParenthesesNew(s, 0)


    def longestValidParenthesesNew(self, s: str, longest_valid_old: int) -> \
            int:
        longest_valid_curr = 0
        stack = [-1]
        for i,c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                start_index = peek_stack(stack)
                if start_index is None:
                    temp = max(longest_valid_curr, longest_valid_old)
                    if len(s[i+1:])>temp:
                        return self.longestValidParenthesesNew(s[i+1:],temp)
                    else:
                        return temp
                else:
                    if i - start_index > longest_valid_curr:
                        longest_valid_curr = i- start_index
        return max(longest_valid_curr,longest_valid_old)



    def longestValidParenthesesExtra(self, s: str, prev_s_valid: int,
                                   total_valid) -> int:
        if not s:
            return total_valid
        # curr_s_valid = prev_s_valid

        #get rid of wrong brackets at beginning of string:
        last_invalid_i = -1
        for i,c in enumerate(s):
            if c =='(':
                break
            else:
                last_invalid_i = i
                prev_s_valid = 0

        s= s[last_invalid_i+1:]
        if not s or len(s) + prev_s_valid <= total_valid:
            return total_valid

        curr_valid = 0
        stack = []
        for i, c in enumerate(s):
            if c =="(":
                stack.append(i)
            else:
                bracket_start_i = stack.pop()
                if i - bracket_start_i + 1 > curr_valid:
                    curr_valid = i - bracket_start_i + 1
                if len(stack) == 0:
                    if total_valid < curr_valid + prev_s_valid:
                        total_valid = curr_valid + prev_s_valid
                    print("debug, calling with: " , s[i+1:],curr_valid +
                                                        prev_s_valid,total_valid)
                    return self.longestValidParenthesesExtra(s[i+1:],curr_valid +
                                                        prev_s_valid,total_valid
                                                        )
                else:
                    if total_valid< curr_valid:
                        total_valid = curr_valid
        return total_valid


    def longestValidParenthesesOld(self, s: str) -> int:
        if not s:
            return self.longest_valid

        acc = 0 #accumulator
        valid_regions = [] # [(start_i, end_i)]
        open_paranth_to_index = {} # int to int map
        illegal_state_reached = False
        i = 0
        for i, c in enumerate(s):
            if c == ')' and acc - 1 < 0:
                illegal_state_reached = True
                break

            if c == '(':
                acc += 1
                if acc not in open_paranth_to_index:
                    open_paranth_to_index[acc] = i
            else:
                if acc in open_paranth_to_index:
                    valid_region_length = i - open_paranth_to_index[acc] + 1
                    if valid_region_length > self.longest_valid:
                        self.longest_valid = valid_region_length
                    open_paranth_to_index.pop(acc)
                acc -= 1


        if illegal_state_reached and len(s) - i -1 > self.longest_valid:
            # decide if it is worth continuing the algorithm, or we have no
            # way to find a lengthier valid string anyways
            return self.longestValidParentheses(s[i+1:])
        else:
            return self.longest_valid

if __name__ =="__main__":
    input = "(()()"
    res = Solution().longestValidParentheses(input)
    print("Result: ",res)
    # assert res  == 24




