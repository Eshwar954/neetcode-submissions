class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        running_product=1
        results=[]
        for i in range(len(nums)):
            product=1
            for j in range(i+1,len(nums)):
                product*=nums[j]
            product=product*running_product
            results.append(product)
            running_product*=nums[i]
        return results

