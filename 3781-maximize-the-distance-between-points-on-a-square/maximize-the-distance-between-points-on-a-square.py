from bisect import bisect_left

class Solution:
    def maxDistance(self, side, points, k):
        pos = []
        for x, y in points:
            if y == 0:
                pos.append(x)
            elif x == side:
                pos.append(side + y)
            elif y == side:
                pos.append(3 * side - x)
            else:
                pos.append(4 * side - y)

        pos.sort()
        n = len(pos)
        per = 4 * side
        arr = pos + [x + per for x in pos]

        def can(d):
            for i in range(n):
                count = 1
                last = arr[i]
                idx = i

                while count < k:
                    nxt = bisect_left(arr, last + d, idx + 1, i + n)
                    if nxt == i + n:
                        break

                    # ❗ circular constraint check EARLY
                    if arr[nxt] - arr[i] > per - d:
                        break

                    count += 1
                    last = arr[nxt]
                    idx = nxt

                if count == k:
                    return True

            return False

        l, r = 0, per
        ans = 0

        while l <= r:
            mid = (l + r) // 2
            if can(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans