class Solution:
    def scoreOfString(self, s: str) -> int:
        i=0
        j=i+1
        sum=0
        while i<len(s) and j<len(s):
            sum+=abs(ord(s[i])-ord(s[j]))
            i+=1
            j+=1
        return sum