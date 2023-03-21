# 2348. Number of Zero-Filled Subarrays
# https://leetcode.com/problems/number-of-zero-filled-subarrays/description/

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        conseZero = 0;
        total = 0;
        for i in range(len(nums)):
            if(nums[i] == 0):
                conseZero +=1;

            if(conseZero > 0 and nums[i] != 0):
                total += (conseZero*(conseZero + 1))//2;
                conseZero = 0;
        total += (conseZero*(conseZero + 1))//2;
        return total;