class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        total_sum = sum(nums)
        
        F = 0
        for i in range(n):
            F += i * nums[i]
        
        ans = F
        
        for k in range(1, n):
            F = F + total_sum - n * nums[n - k]
            ans = max(ans, F)
        
        return ans


if __name__ == "__main__":
    obj = Solution()
    
    print(obj.maxRotateFunction([4,3,2,6]))
    print(obj.maxRotateFunction([100]))