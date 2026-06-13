class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i=0
        j=0
        maximum=0
        while j<len(nums):
            if nums[j]==0:
                count=j-i
                if count>maximum:
                    maximum=count
                i=j+1
            j+=1
        count=j-i
        if count>maximum:
            maximum=count
        return maximum