"""
Example 1:

Input: nums1 = [60,60,60], nums2 = [10,90,10]
Output: 210
Explanation: Choosing left = 1 and right = 1, we have nums1 = [60,90,60] and nums2 = [10,60,10].
The score is max(sum(nums1), sum(nums2)) = max(210, 80) = 210.

Example 2:

Input: nums1 = [20,40,20,70,30], nums2 = [50,20,50,40,20]
Output: 220
Explanation: Choosing left = 3, right = 4, we have nums1 = [20,40,20,40,20] and nums2 = [50,20,50,70,30].
The score is max(sum(nums1), sum(nums2)) = max(140, 220) = 220.

Example 3:

Input: nums1 = [7,11,13], nums2 = [1,1,1]
Output: 31
Explanation: We choose not to swap any subarray.
The score is max(sum(nums1), sum(nums2)) = max(31, 3) = 31.

"""
from typing import List

def create_accumulator(l):
    # inefficient list creating with no memory preallocation but not so easy to do in python without numerical libs(IE
    # numpy)
    ct = 0
    acc = []
    for nr in l:
        ct += nr
        acc.append(ct)
    return acc

class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1 is None or len(nums1) == 0:
            return 0
        if len(nums1) == 1:
            return max(nums1[0],nums2[0])

        # print("accumulator of nums1: ", nums1_acc)
        diff = [nums1[i] - nums2[i] for i in range(len(nums1))]
        diff_acc = create_accumulator(diff)

        min_ = (0, -1) # value,index
        max_ = (0, -1)
        ideal_split_for_nums1 = ((None, None), 0)  # splitting from where to where, and value gained
        ideal_split_for_nums2 = ((None, None), 0)  # splitting from where to where, and value gained

        nums1_acc = 0
        nums2_acc = 0
        for i,nr in enumerate(diff_acc):
            nums1_acc += nums1[i]
            nums2_acc += nums2[i]
            # print(f"in loop for index: {i}")
            if max_[0] - nr >ideal_split_for_nums1[1]:
                ideal_split_for_nums1 = ((max_[1],i),max_[0] - nr)
            if nr - min_[0] > ideal_split_for_nums2[1]:
                ideal_split_for_nums2 = ((min_[1],i),nr - min_[0])
            if nr < min_[0]:
                min_ = (nr,i)
            if nr > max_[0]:
                max_ = (nr,i)
            # print(f"max_ = {max_}, min_ = {min_}")
            # print(f"ideal_split_for_nums1 = {ideal_split_for_nums1}")
            # print(f"ideal_split_for_nums2 = {ideal_split_for_nums2}")


        #now finally decide if we fo for nums1 with part of nums2 or viceversa:
        if ideal_split_for_nums1[1] != 0:
            nums1_acc += ideal_split_for_nums1[1]


        if ideal_split_for_nums2[1] != 0:
            nums2_acc += ideal_split_for_nums2[1]


        return max(nums1_acc,nums2_acc)

if __name__ == "__main__":
    nums1 = [20, 40, 20, 70, 30]
    nums2 = [50, 20, 50, 40, 20]
    print(Solution().maximumsSplicedArray(nums1,nums2))




