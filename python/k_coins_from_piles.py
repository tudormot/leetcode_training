"""
There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.

In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.

Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, and a positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.



Example 1:

Input: piles = [[1,100,3],[7,8,9]], k = 2
Output: 101
Explanation:
The above diagram shows the different ways we can choose k coins.
The maximum total we can obtain is 101.

Example 2:

Input: piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
Output: 706
Explanation:
The maximum total can be obtained if we choose all coins from the last pile.



Constraints:

    n == piles.length
    1 <= n <= 1000
    1 <= piles[i][j] <= 105
    1 <= k <= sum(piles[i].length) <= 2000


"""
from typing import List


def maxCoinsRecursive(piles, k, max_coins_l_piles, l)->int:
    acc = 0
    new_max_coins = max_coins_l_piles.copy()
    # print("start recursive")
    for i in range(1,len(piles[l])+1):
        #using i coins from this new stack

        acc += piles[l][i-1]
        for j in range(i,k+1):
            #these are the entries in new_max_coins that can be influenced by acc:
            new_max_coins[j] = max(new_max_coins[j], acc + max_coins_l_piles[j-i])

    # print(f"In Recursive: l = {l}, max_coins_l_piles = {new_max_coins}")

    if l == len(piles) -1 :
        # print("we here, termination, new_max_coins: ", new_max_coins)
        # print("debug. ", new_max_coins[-1])
        return new_max_coins[-1]
    else:
        return maxCoinsRecursive(piles,k,new_max_coins, l + 1)



class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        if len(piles) == 0 or k == 0:
            return 0
        val = maxCoinsRecursive(piles,k,[0]*(k+1), 0 )
        # print("we here, val is: ", val)
        return val

if __name__ == "__main__":
    piles = [[37,88],[51,64,65,20,95,30,26],[9,62,20],[44]]
    k = 9
    print(Solution().maxValueOfCoins(piles,k))



