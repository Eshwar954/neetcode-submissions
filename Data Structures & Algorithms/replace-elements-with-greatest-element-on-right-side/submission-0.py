class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result=[]
        max_element=0
        for i in range(0,len(arr),1):
            element=arr[i]
            for j in range(i+1,len(arr),1):
                if arr[j]>max_element:
                    max_element=arr[j]
            result.append(max_element)
            max_element=0
        result[-1]=-1
        return result