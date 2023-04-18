"""887. Reduction Operations to Make the Array Elements Equal
Medium
461
19
Companies

Given an integer array nums, your goal is to make all elements in nums equal. To complete one operation, follow these steps:

    Find the largest value in nums. Let its index be i (0-indexed) and its value be largest. If there are multiple elements with the largest value, pick the smallest i.
    Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
    Reduce nums[i] to nextLargest.

Return the number of operations to make all elements in nums equal."""
from typing import List
from collections import defaultdict

# def calculate_comb_of_2_list(n):
#     combs = [1,1]
#     for i in range(2,n+1):
#         combs.append(combs[-1] * i // 2)
#     return combs


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        if nums is None:
            return -1
        n = len(nums)
        if n <= 1:
            return 0

        # encountered = defaultdict(int)
        # max_encountered = 0
        # for num in nums:
        #     encountered[num] +=1
        #     if encountered[num] > max_encountered:
        #         max_encountered = encountered[num]
        #
        # max_red = n*(n-1)//2
        # print(f"max_red = {max_red}")
        # if max_encountered > 1:
        #     combs = calculate_comb_of_2_list(max_encountered)
        #     for _,value in encountered.items():
        #         if value > 1:
        #             print(f"combs[value] = {combs[value]}")
        #             max_red -= combs[value]

        max_red = n*(n-1)//2
        nums.sort(reverse=True)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                max_red-=i+1
        return max_red







        # return max_red


if __name__ == "__main__":
    nums = [1, 1, 1]
    print(Solution().reductionOperations(nums))