class Solution:
    def findThePrefixCommonArray(self, A, B):
        seen = set()
        ans = []
        count = 0

        for i in range(len(A)):

            if A[i] in seen:
                count += 1
            seen.add(A[i])

            if B[i] in seen:
                count += 1
            seen.add(B[i])

            ans.append(count)

        return ans