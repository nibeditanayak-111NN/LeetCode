class Solution:
    def minOperations(self, grid, x):
        nums = []
        for row in grid:
            nums.extend(row)
        
        rem = nums[0] % x
        for num in nums:
            if num % x != rem:
                return -1
        
        nums.sort()
        median = nums[len(nums)//2]
        
        ops = 0
        for num in nums:
            ops += abs(num - median) // x
        
        return ops


if __name__ == "__main__":
    obj = Solution()
    
    print(obj.minOperations([[2,4],[6,8]], 2))
    print(obj.minOperations([[1,5],[2,3]], 1))
    print(obj.minOperations([[1,2],[3,4]], 2))