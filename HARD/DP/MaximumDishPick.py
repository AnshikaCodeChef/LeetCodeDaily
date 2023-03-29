#1402. Reducing Dishes
# https://leetcode.com/problems/reducing-dishes/

def maxSatisfaction(self, satisfaction: List[int], c = 1, startIdx = 0) -> int:
        satisfaction.sort(reverse=True)
        n = len(satisfaction)
        presum, res = 0, 0
        for i in range(n):
            presum += satisfaction[i]
            if presum < 0:
                break
            res += presum
        return res