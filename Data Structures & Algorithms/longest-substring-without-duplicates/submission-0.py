class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        max_length=0
        i=0
        j=0
        while j<n:
            found=False
            for k in range(i,j):
                if s[k]==s[j]:
                    i=k+1
                    found=True
                    break
            max_length=max(max_length,j-i+1)
            j+=1
        return max_length

