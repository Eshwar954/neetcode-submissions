class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        current_min,current_max=1,1
        for num in nums:
            if num==0:
                current_max,current_min=1,1
                continue
            temp=current_max*num
            current_max=max(num,current_max*num,num*current_min)
            current_min=min(num,temp,num*current_min)
            res=max(current_max,res)
        return res


            