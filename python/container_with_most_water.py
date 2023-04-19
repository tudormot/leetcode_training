from typing import List


def calculate_vol (height,i,j):
    return min(height[i],height[j]) * (j-i)

def maxAreaRecursive(height, start,end):
    # print(f"calledf with start={start}, end={end}")

    if start >= end:
        return 0
    if end-start == 1:
        return 0
    if end-start == 2:
        return min(height[start],height[start+1])


    i = start
    j = end-1
    vol = 0
    while j - i > 1:
        progress_exists = False
        vol = calculate_vol(height,i,j)
        while j - i > 1:
            new_vol =  calculate_vol( height,i +1, j )
            if new_vol <= vol:
                break
            else:
                vol = new_vol
                i += 1
                progress_exists = True
        while j - i > 1 :
            new_vol =  calculate_vol(height,i, j-1 )
            if new_vol <= vol:
                break
            else:
                # print(f"progress made from j= {j}->{j-1}")
                vol = new_vol
                j -= 1
                progress_exists = True
        if not progress_exists:
            break
    # print("vol here:", vol)
    if height[i] > height[j]:
        # print("calling with j-1")
        return max(vol, maxAreaRecursive(height, i, j))
    else:
        return max(vol, maxAreaRecursive(height, i+1 , j+1))


class Solution:

    def maxArea(self, height: List[int]) -> int:
        return maxAreaRecursive(height,0,len(height))


if __name__ == "__main__":
    height = [6,4,3,1,4,6,99,62,1,2,6]
    print(Solution().maxArea(height))