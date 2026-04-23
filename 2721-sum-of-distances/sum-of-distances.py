from collections import defaultdict
class Solution:
    def distance(self, nums):
        index_map = defaultdict(list)
        for i, num in enumerate(nums):
            index_map[num].append(i)
        
        res = [0] * len(nums)
        for indices in index_map.values():
            n = len(indices)
            prefix = [0] * (n + 1)
            for i in range(n):
                prefix[i + 1] = prefix[i] + indices[i]
            for i in range(n):
                idx = indices[i]
                left = i * idx - prefix[i]
                right = (prefix[n] - prefix[i + 1]) - (n - i - 1) * idx
                
                res[idx] = left + right
        
        return res