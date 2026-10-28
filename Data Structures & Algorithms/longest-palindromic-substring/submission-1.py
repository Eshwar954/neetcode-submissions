class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        reslen=0
        k=0
        for i in range(len(s)):
            l,r=i,i
            mismatches=0
            while l>=0 and r<len(s):
                if s[l]!=s[r]:
                    mismatches+=1
                if mismatches>k:
                    break
                if r-l+1>reslen:
                    reslen=max(reslen,r-l+1)
                    res=s[l:r+1]
                l-=1
                r+=1
            l,r=i,i+1
            mismatches=0
            while l>=0 and r<len(s):
                if s[l]!=s[r]:
                    mismatches+=1
                if mismatches>k:
                    break
                if r-l+1>reslen:
                    reslen=max(reslen,r-l+1)
                    res=s[l:r+1]
                l-=1
                r+=1
        return res