class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index=0
        for ch in s:
            found=False
            for i in range(index,len(t)):
                if ch==t[i]:
                    index=i+1
                    found=True
                    break
            if not found:
                return False

        return True