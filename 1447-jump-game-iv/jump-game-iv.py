from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr):
        n = len(arr)

        if n == 1:
            return 0

        graph = defaultdict(list)

        for i in range(n):
            graph[arr[i]].append(i)

        queue = deque([0])
        visited = set([0])
        steps = 0

        while queue:
            size = len(queue)

            for _ in range(size):
                i = queue.popleft()

                if i == n - 1:
                    return steps

                neighbors = graph[arr[i]] + [i - 1, i + 1]

                for nxt in neighbors:
                    if 0 <= nxt < n and nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)

                graph[arr[i]] = []

            steps += 1

        return -1