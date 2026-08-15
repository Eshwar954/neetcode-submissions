class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_map={}
        for num in nums:
            count_map[num]=count_map.get(num,0)+1
        for value in count_map.values():
            if value>=2:
                return True
        return False
            

        