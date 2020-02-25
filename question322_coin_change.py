class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount==0:
            return 0
        if amount in coins:
            return 1
        coins=sorted(coins)
        dp=[amount+1 for j in range(amount+1)]
        dp[0]=0
        for i in range(amount+1):
            for j in coins:
                if j<=i:
                    dp[i]=min(dp[i],1+dp[i-j])
                else:
                    break
        print(dp[amount])
        if dp[amount]>amount:
            return -1
        
        return dp[amount]
                    