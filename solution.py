from typing import List
from math import floor , ceil
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_full_array = self.sort_two_arrays(nums1,nums2)
        print("sorted array: ", sorted_full_array)
        if len(sorted_full_array)%2==1:
            return float(sorted_full_array[int((len(sorted_full_array)-1)/2)])
        else:
            mid:int = len(sorted_full_array)/2
            return (sorted_full_array[mid-1] + sorted_full_array[mid])/2.

    def sort_two_arrays(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 == []:
            return nums2
        if nums2 == []:
            return nums1
        if(nums1[-1]<nums2[0]):
            return nums1 + nums2
        if(nums2[-1]<nums1[0]):
            return nums2+nums1
        print("starting with: ", nums1,nums2)

        s1 = len(nums1)
        s2 = len(nums2)
        if s1==0 :
            return nums2
        if s2==0:
            return nums1
        if s1>s2:
            temp = s1
            s1 = s2
            s2 = s1
            temp = nums1
            nums1 = nums2
            nums2 = temp

        x:int = nums1[floor(s1/2)]
        nums1_0 = nums1[0:floor(s1/2)+1]  #x is at the end of this array
        nums1_1 = nums1[floor(s1/2)+1:]   #this array starts right after x


        nums2_0, nums2_1, _ = self.determine_correct_split_by_value(nums2[0:floor(s2/2)],nums2[floor(s2/2):], x)
        print("for x = ",x)
        print("split_by_value result: ",nums2_0,nums2_1)
        print("the two results")
        print(nums1_0, nums2_0)
        print(nums1_1, nums2_1)

        return self.sort_two_arrays(nums1_0, nums2_0) + self.sort_two_arrays(nums1_1, nums2_1)
    
    def determine_correct_split_by_value(self, split1,split2, x):
        if split1 == [] and split2 ==[]:
            return [], [], x

        if split1 == [] and len(split2)>0 and x<= split2[0]:
            return [], split2, x
        if split2 == [] and len(split1)>0 and x>=split1[-1]:
            return split1, [], x


        if (len(split1)> 0 and len(split2)>0 and split1[-1]<=x and split2[0]>=x):
            return split1, split2, x

        #print("### split1, split2, x = ", split1,split2,x)

        if len(split1) == 0:
            sz = len(split2)
            return self.determine_correct_split_by_value(split2[0:ceil(sz/2)], split2[ceil(sz/2):], x)

        if len(split2) == 0:
            sz = len(split1)
            return self.determine_correct_split_by_value(split1[0:floor(sz/2)-1],split1[floor(sz/2)-1:], x)
        
        if split1[-1]>x:
            sz = len(split1)
            return self.determine_correct_split_by_value(split1[0:floor(sz/2)-1],split1[floor(sz/2)-1:]+ split2, x)
        
        if  split2[0]<x :
            sz = len(split2)
            return self.determine_correct_split_by_value(split1 + split2[0:ceil(sz/2)], split2[ceil(sz/2):], x)



if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2]
    x = 99
    s = Solution()
    print(s.sort_two_arrays(nums1,nums2))
