class Solution:
    def rotatedDigits(self, n):
        good = {2, 5, 6, 9}
        invalid = {3, 4, 7}
        
        count = 0
        
        for num in range(1, n + 1):
            x = num
            is_good = False
            
            while x > 0:
                d = x % 10
                
                if d in invalid:
                    is_good = False
                    break
                
                if d in good:
                    is_good = True
                
                x //= 10
            
            if is_good and x == 0:
                count += 1
        
        return count


if __name__ == "__main__":
    obj = Solution()
    
    print(obj.rotatedDigits(10))
    print(obj.rotatedDigits(1))
    print(obj.rotatedDigits(2))