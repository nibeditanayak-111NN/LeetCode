from collections import deque, defaultdict

class Solution:
    def minJumps(self, nums):
        n = len(nums)

        if n == 1:
            return 0

        max_num = max(nums)

        spf = list(range(max_num + 1))

        for i in range(2, int(max_num ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_num + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        def is_prime(x):
            return x > 1 and spf[x] == x

        factor_map = defaultdict(list)

        for i, val in enumerate(nums):
            temp = val
            factors = set()

            while temp > 1:
                p = spf[temp]
                factors.add(p)

                while temp % p == 0:
                    temp //= p

            for p in factors:
                factor_map[p].append(i)

        q = deque([0])
        visited = [False] * n
        visited[0] = True

        used_prime = set()

        steps = 0

        while q:
            for _ in range(len(q)):
                i = q.popleft()

                if i == n - 1:
                    return steps

                if i - 1 >= 0 and not visited[i - 1]:
                    visited[i - 1] = True
                    q.append(i - 1)

                if i + 1 < n and not visited[i + 1]:
                    visited[i + 1] = True
                    q.append(i + 1)

                val = nums[i]

                if is_prime(val) and val not in used_prime:

                    for nxt in factor_map[val]:
                        if not visited[nxt]:
                            visited[nxt] = True
                            q.append(nxt)

                    used_prime.add(val)

            steps += 1

        return -1