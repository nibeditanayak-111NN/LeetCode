class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        mapping = {
            '2': "abc", '3': "def", '4': "ghi",
            '5': "jkl", '6': "mno", '7': "pqrs",
            '8': "tuv", '9': "wxyz"
        }
        
        res = []
        
        def backtrack(index, path):
            if index == len(digits):
                res.append(path)
                return
            
            for ch in mapping[digits[index]]:
                backtrack(index + 1, path + ch)
        
        backtrack(0, "")
        return res


if __name__ == "__main__":
    obj = Solution()
    
    print(obj.letterCombinations("23"))
    print(obj.letterCombinations("2"))