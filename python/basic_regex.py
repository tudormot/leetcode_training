from functools import cache
EPS = "magic_epsilon_transition_token"


class RegexPrimitive:
    def __init__(self, awaited_letter, next_state):
        self.next_state: RegexPrimitive = next_state
        self.epsilon_visited = False  # lil optim
        pass

    def give_next_state(self, input):
        raise "Not implemented, subclass this class!"


class AwaitLetterOnce(RegexPrimitive):
    def __init__(self, awaited_letter, next_state):
        assert awaited_letter != EPS, "What are you trying to do here? " \
                                      "invalid input"
        self.awaited_letter = awaited_letter
        super().__init__(awaited_letter, next_state)

    def give_next_state(self, input) -> [RegexPrimitive]:
        if input == self.awaited_letter:
            return [self.next_state]
        else:
            return []


class AwaitAnyLetterOnce(RegexPrimitive):
    def __init__(self, awaited_letter, next_state):
        super().__init__(awaited_letter, next_state)

    def give_next_state(self, input) -> [RegexPrimitive]:
        if input != EPS:
            return [self.next_state]
        else:
            return []


class AwaitLetterArbitraryTimes(RegexPrimitive):
    def __init__(self, awaited_letter, next_state):
        assert awaited_letter != EPS, "What are you trying to do here? " \
                                      "invalid input"
        self.awaited_letter = awaited_letter
        super().__init__(awaited_letter, next_state)

    def give_next_state(self, input) -> [RegexPrimitive]:
        if input == EPS:
            return [self.next_state]
        elif input == self.awaited_letter or self.awaited_letter == '.':
            return [self, self.next_state]
        else:
            return []


class StringMatchedState(RegexPrimitive):
    def __init__(self, awaited_letter, next_state):
        assert not awaited_letter and not next_state, "Sanity check. " \
                                                      "initialize " \
                                                      "this with None " \
                                                      "please"
        self.awaited_letter = awaited_letter
        super().__init__(awaited_letter, next_state)

    def give_next_state(self, input) -> [RegexPrimitive]:
        return []



class RegexAutomata:
    def __init__(self, regex_pattern):
        self.active_states = []
        self._parse_input(regex_pattern)

    def _parse_input(self, p: str):
        i = len(p) - 1
        next_state = StringMatchedState(None, None)
        while i >= 0:
            if p[i] == '.':
                new_next_state = AwaitAnyLetterOnce(None, next_state)
                next_state = new_next_state
            elif p[i] == '*':
                i = i - 1
                new_next_state = AwaitLetterArbitraryTimes(p[i], next_state)
                next_state = new_next_state
            else:
                new_next_state = AwaitLetterOnce(p[i], next_state)
                next_state = new_next_state
            i = i - 1
        self.active_states = self._get_epsilon_closure_of_state_set([
            next_state])

    def _get_epsilon_closure_of_state_set(self, states: [RegexPrimitive]) \
            -> [RegexPrimitive]:
        epsilon_search_visited_states = []
        states_to_visit = []
        for s in states:
            states_to_visit += s.give_next_state(EPS)
            s.epsilon_visited = True
            epsilon_search_visited_states.append(s)
        while True:
            if len(states_to_visit) == 0:
                break
            s = states_to_visit.pop()
            if s.epsilon_visited:
                continue
            else:
                states_to_visit += s.give_next_state(EPS)
                s.epsilon_visited = True
                epsilon_search_visited_states.append(s)
        for s in epsilon_search_visited_states:
            s.epsilon_visited = False
        return epsilon_search_visited_states


    def verify_string(self, s):
        for c in s:
            # print("we here for c = ", c)
            if len(self.active_states) == 0:
                break
            new_active_states = []
            for state in self.active_states:
                new_active_states += state.give_next_state(c)
            self.active_states = self._get_epsilon_closure_of_state_set(new_active_states)
            # print("active states: ", self.active_states)

        return any(type(s) == StringMatchedState for s in self.active_states)


# class Solution(object):
#     def isMatch(self, text, pattern):
#         if not pattern:
#             return not text
#
#         first_match = bool(text) and pattern[0] in {text[0], '.'}
#
#         if len(pattern) >= 2 and pattern[1] == '*':
#             return (self.isMatch(text, pattern[2:]) or
#                     first_match and self.isMatch(text[1:], pattern))
#         else:
#             return first_match and self.isMatch(text[1:], pattern[1:])
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # return RegexAutomata(p).verify_string(s)
        return second_method(s, p)

@cache
def second_method(s:str, p: str) -> bool:
    if not p:
        return not s
    first_match = bool(s) and (p[0] == '.' or p[0] == s[0])
    if len(p)> 1 and p[1] == "*":
        return (first_match
                and (second_method(s[1:], p)
                     or second_method(s, p[2:])
                     or second_method(s[1:], p[2:]))) or (not first_match
                                                          and second_method(s, p[2:]))
        # if p[0] == '.' or p[0] == s[0]:
        #     return
        # else:
        #     return second_method(s, p[2:])

    return first_match and second_method(s[1:], p[1:])


if __name__ == "__main__":
    # TODO problem!
    s = "aaaaaaaaaaaaab"
    p = "a*a*a*a*a*a*a*a*a*a*a*a*b"
    # p = "a*a*a*a*b"
    assert Solution().isMatch(s, p) is True
