"""


A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:
    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2

contains the following example double slices:

        double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
        double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
        double slice (3, 4, 5), sum is 0.

The goal is to find the maximal sum of any double slice.

Write a function:

    class Solution { public int solution(int[] A); }

that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

For example, given:
    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2

the function should return 17, because no double slice of array A has a sum of greater than 17.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [3..100,000];
        each element of array A is an integer within the range [−10,000..10,000].



"""
from typing import Generator


def modified_kadane(l: Generator[int,None,None])->Generator[int,None,None]:
    """normal kadane algo gives the maximum sum of a subarray of an array given as input, in O(n) complexity.
    This is a modified version, which returns an array of the length of the input array, containing at each index i
    maximum sum of a
    subarray that ends at index i"""
    curr_sum = 0
    for nr in l:
        yield curr_sum
        curr_sum += nr
        if curr_sum < 0:
            curr_sum = 0
def max_double_splice_sum(my_input):
    left_sums = [i for i in modified_kadane(my_input)]
    right_sums = [i for i in modified_kadane(reversed(my_input))]
    print(f"debug. left sums = {left_sums}, right_sums = {right_sums}")
    max_sum = my_input[0]
    for i in range(len(left_sums)):
        new_sum  = left_sums[i] + right_sums[i]
        if new_sum> max_sum:
            max_sum = new_sum
    return max_sum




if __name__ == "__main__":
    pass
    my_input = [3, 2, -6, -1, 4, 5, -1, 2]
    print(max_double_splice_sum(my_input)) # should be 14. and it is! GG

