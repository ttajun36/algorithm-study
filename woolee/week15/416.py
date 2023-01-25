class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        goal = sum(nums)
        if goal % 2 == 1 or len(nums) == 1:
            return False
        dp = [[False] * (len(nums) + 1) for _ in range(goal // 2 + 1)]
        for i in range(len(nums) + 1):
            dp[0][i] = True
        
        for s in range(1, goal // 2 + 1):
            for i in range(1, len(nums) + 1):
                if dp[s][i-1] or (s - nums[i - 1] >= 0 and dp[s - nums[i - 1]][i - 1]):
                    dp[s][i] = True
                else:
                    dp[s][i] = False
        # print(dp)
        return dp[-1][-1]