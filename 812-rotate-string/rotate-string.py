class Solution:
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        
        return goal in (s + s)


if __name__ == "__main__":
    obj = Solution()
    
    print(obj.rotateString("abcde", "cdeab"))
    print(obj.rotateString("abcde", "abced"))