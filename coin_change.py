from typing import List

"""
322. Coin Change, medium

You are given coins of different denominations and a total amount of money
amount. Write a function to compute the fewest number of coins that you need to
make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        # Greedy algorithm doesn't work, e.g. coins = [25, 3], amount = 27
        # Use Dynamic Programming!
        # Subproblems: x(i) = min number of coins to find amount i
        # Relate: x(i) = 1 + min{x(i-coins[j]) for 0 <= j < len(coins)}
        # Base Case: x(0) = 0
        # Solution: x(amount)
        # Time: O(len(amount) * len(coins))
        # Space: O(amount) because we store x(i)

        min_coins = dict()
        min_coins[0] = 0
        for i in range(1, amount+1):
            potential = []
            for j in range(len(coins)):
                if i-coins[j] >= 0 and min_coins[i-coins[j]] != -1:
                    potential.append(min_coins[i-coins[j]])
                if len(potential) > 0:
                    min_coins[i] = 1 + min(potential)
                else:
                    min_coins[i] = -1

        return min_coins[amount]

solution = Solution()
# coins = [1, 2, 5]
# amount = 11
print("Coins: ", coins, "\nAmount: ", amount)
print("Solution: ", solution.coinChange(coins, amount))
