# 2300. Successful Pairs of Spells and Potions
# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort();
        n = len(spells);
        m = len(potions);
        res = [0]*n
        for i in range(n):
            low = 0;
            high = m-1;
            pair = 0;
            while(low<=high):
                mid = (low+high)//2;
                if(potions[mid]*spells[i] >= success):
                    high = mid-1;
                    pair = max(pair, m-high-1)

                else:
                    low = mid+1;
                
            res[i] = pair;

        return res;