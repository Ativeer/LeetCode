class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        
        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1
        
        for i in range(2, len(s)+1):
            oneDigit = int(s[i-1])
            twoDigit = int(s[i-2:i])
            
            if oneDigit > 0:
                dp[i] += dp[i-1]
            
            if twoDigit < 27 and twoDigit > 9:
                dp[i] += dp[i-2]
        return dp[len(s)]